# Captain's password

## Zadání

Ahoy, officer,
our captain has had too much naval espresso and is temporary unfit for duty. The chief officer is in command now, but he does not know the captain's passwords for key ship systems. Good news is that the captain uses password manager and ship chief engineer was able to acquire captain's computer memory crash dump. Your task is to acquire password for signalization system.

Hint: At first, identify the password manager.

## Řešení

- pro práci s pamětí lze použít nástroj volatility
	- existují dvě verze - volatility pro Python2 či volatility2 pro Python3
- nejjednodušeji rozchození Volatility přes Docker
- podle přípony dostupného souboru rozpoznáno jako Keepass
- detekce profilu > seznam procesů > dump paměti procesu Keepassu
```
docker pull phocean/volatility

# run docker

sudo docker run -t -i --rm --entrypoint=/bin/bash -v /home/kali/Documents/CTF/CATCH/2023/04-01-Captains_password/docker_data:/data phocean/volatility

$ python vol.py -f /data/crashdump.dmp imageinfo

Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : VirtualBoxCoreDumpElf64 (Unnamed AS)
                     AS Layer3 : FileAddressSpace (/data/crashdump.dmp)
                      PAE type : PAE
                           DTB : 0x185000L
                          KDBG : 0x82730c28L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0x82731c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2023-06-12 22:37:09 UTC+0000
     Image local date and time : 2023-06-13 00:37:09 +0200



# --- seznam procesu a hledání Keepassu ---

$ python vol.py -f /data/crashdump.dmp --profile Win7SP1x86_23418 pslist

...
0x85f15030 KeePass.exe             592   1448     16      374      1      0 2023-06-12 22:35:44 UTC+0000
...

=> PID=592

# --- export paměti procesu Keepassu ---

python vol.py -f /data/crashdump.dmp --profile Win7SP1x86_23418 memdump -p 592 -D /data/memdump/
```
- slepá ulička č. 1: kontrola schránky (není implementované v Volatility2), protože v jiném CTF s veřejně dostupným write-upem to byl klíč k řešení:
```
# --- prohledavani schránky ---

$ python vol.py -f /data/crashdump.dmp --profile Win7SP1x86_23418 clipboard -v
Volatility Foundation Volatility Framework 2.6.1                                                                    
NIC TAM NENÍ
```
- vyexportování Keepassu  a spuštění ve Win
    - syntaxe volatility pro export souboru `python vol.py -f DUMP.dmp --profile PROFILE dumpfiles -Q HANDLER --name NAME -D /DIR_TO_EXPORT_DUMP/`
	- při kliku na About to hází chybu, ale z chybové hlášky je patrná verze "2.35.0.20042"
- kontrola verze na exploity: [CVE-2023-32784](https://www.cvedetails.com/cve/CVE-2023-32784/ "CVE-2023-32784 security vulnerability details")
	- do verze 2.54 lze zjistit z dumpu paměti master heslo
- stažení exploitu:  https://github.com/vdohney/keepass-password-dumper
- přetažení image Keepassu do Windows hosta a doinstalování Dotnet SDK
- přesun do adresáře s Gitem exploitu a spuštění exploitu: `dotnet run ..\592.dmp`
	- výstup exploitu: `Combined: ●{a, )}ssword4mypreciousship`
- správné master heslo: `password4mypreciousship` (první dva znaky je třeba odhadnout)
- otevření souboru správce hesel, který jsme dostali se zadáním
- prostou kontrolou záznamů nalezen "Main Flag System": `FLAG{pyeB-941A-bhGx-g3RI}`