# Naval chef's recipe

## Zadání

Ahoy, officer,

some of the crew started behaving strangely after eating the chef's speciality of the day - they apparently have hallucinations, because they are talking about sirens wailing, kraken on starboard, and accussed the chef being reptilian spy. Paramedics are getting crazy, because the chef refuses to reveal what he used to make the food. Your task is to find his secret recipe. It should be easy as the chef knows only security by obscurity and he has registered domain `chef-menu.galley.cns-jv.tcc`. May you have fair winds and following seas!

The chef's domain is `chef-menu.galley.cns-jv.tcc`.

Hint: Use VPN

## Řešení

- klíčové z úvodního popisu:
	- *It should be easy as the chef knows only security by obscurity*
- slepá ulička č. 1: kontrola adresářů: `gobuster dir -u https://chef-menu.galley.cns-jv.tcc -w ~/Documents/dictionaries/web/big.txt -k`
	- nic nenašel
- slepá ulička č. 2: kontrola poddomén
	- XX.chef-menu.galley.cns-jv.tcc - nic
	- XX.galley.cns-jv.tcc - nic (je třeba si do /etc/hosts přidat galley.cns-jv.tcc ukazující na stejnou IP)
- CURL na HTTP (napadlo mne kvůli podivnému přebliknutí redirectu HTTP->HTTPS při přístupu na web)
	- vrátí: `<p style="display: none">The secret ingredient is composed of C6H12O6, C6H8O6, dried mandrake, FLAG{ytZ6-Pewo-iZZP-Q9qz}, and C20H25N3O. Shake, do not mix.</p>` - prohlížeč to sice na zlomek sekundy zobrazí, ale následuje redirect

FLAG: `FLAG{ytZ6-Pewo-iZZP-Q9qz}`