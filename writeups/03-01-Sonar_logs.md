# Sonar logs

Ahoy, officer,
each crew member must be able to operate the sonar and understand its logs. Your task is to analyze the given log file, and check out what the sonar has seen.

May you have fair winds and following seas!

Download [the logs](https://owncloud.cesnet.cz/index.php/s/5ZpEExdDf4ZBW1E/download).  
(MD5 checksum: `b946f87d0231fcbdbc1e76e27ebf45c7`)

Hint: The entry in the log consists of two parts - the timestamp and the message.

Hint2: Update: Be aware that some devices do not use up-to-date libraries - this sonar, for example, is based on python and uses an old `pytz` library version 2020.4.

## Řešení

- na konci některých řádek "(0xAB)"
- teze vedoucí ke správnému řešení
	- řádek logu s "0xAB" je 25 == počet znaků v "FLAG{...}"
	- řádky jsou ve špatném pořadí - časová značka bude to co je seřadí
	- časové značky jsou v různých časových pásmech - třeba je sjednotit do UTC
- postup
	1. grepnout všechny řádky s "(0xAB)"
	2. kód Pythonu convert_to_utc.py
		1. načte grepnuté řádky jako CSV s mezerou jako oddělovačem
		2. převede timestamp
		3. na výstup vypíše timestamp v UTC a převedený znak
	3. pro zjednodušení/zrychlení výstup ze skriptu zapsán do Excelu
	4. seřazení A->Z podle času
	5. vyčtení FLAGu
- když jsem začal řešit, nebyl dostupný Hint ohledně verze knihovny Pytz, FLAG vycházel špatně
- reinstalace knihovny Pytz `pip install pytz==2020.04`
- spuštění Python skriptu výše již vrátil správný FLAG
- FLAG: `FLAG{3YAG-2rbj-KWoZ-LwWm}`