# Ship web server

## Zadání

Ahoy, deck cadet,
there are rumors that on the ship web server is not just the official presentation. Your task is to disprove or confirm these rumors.

May you have fair winds and following seas!

Ship web server is available at [http://www.cns-jv.tcc](http://www.cns-jv.tcc).

Hint 1: Use VPN to get access to the ship web server.

Hint 2: Check the content of the certificate of the web.

Hint 3: Visit the other web sites hosted on the same server. Don't let non-existent DNS records to stop you.

## Řešení

- URL s úkolem: http://www.cns-jv.tcc
	- nevalidní SSL certifikát
	- subject alt names:
		- 10.99.0.64	documentation.cns-jv.tcc
		- 10.99.0.64	home.cns-jv.tcc
		- 10.99.0.64	pirates.cns-jv.tcc
		- 10.99.0.64	structure.cns-jv.tcc
- dané URL nelze resolvovat (NXDOMAIN)
- na spodu stránky je BASE64 `ver. RkxBR3sgICAgLSAgICAtICAgIC0gICAgfQ==` což je `FLAG{    -    -    -    }`
	- tedy úvaha, že budu hledat 4 části, které mi každá dají část FLAGu
- slepá ulička č. 1: listování možných adresářů ukázalo prázdné podstránky (gobuster)
	- /documentation
	- /home
	- /structure
- slepá ulička č. 2: hledání poddomén (gobuster) nic nenašlo
- ze zkušenosti z jiného CTF, je třeba si přidat dané záznamy do `/etc/hosts`
	- k tomu se vztahuje Hint 3 - v době mého řešení, ale ještě nebyl publikovaný
- na každé ze stránek je část FLAGu
	- documentation.cns-jv.tcc
		- dole část FLAGu `RkxBR3sglCAgLSAglCAtlCAglC1nTXdjfQ==` což je `FLAG{  -   -  -gMwc}`
		- je to jako obrázek, OCR nedopadá dobře a není jasné, jestli "l" je malé "L". Díky tomu, že nás z toho zajímá jen konec, tak lze chyby ignorovat.
	- home.cns-jv.tcc
		- v Cathy je část FLAGu `RkxBR3tlamlpLSAgICAtICAgIC0gICAgfQ==` což je `FLAG{ejii-    -    -    }`
	- pirates.cns-jv.tcc
		- dole část FLAGu `RkxBR3sgICAgLSAgICAtUTUzQy0gICAgfQ==` což je `FLAG{    -    -Q53C-    }`
- structure.cns-jv.tcc
		- dole část FLAGU: `RkxBR3sgICAgLXBsbVEtICAgIC0gICAgfQ==` což je `FLAG{    -plmQ-    -    }`
- spojeno dohromady: `FLAG{ejii-plmQ-Q53C-gMwc}`
