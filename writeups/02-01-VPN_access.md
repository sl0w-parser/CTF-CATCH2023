# VPN Access

## Zadání

Ahoy, deck cadet,

a lot of ship systems is accessible only via VPN. You have to install and configure OpenVPN properly. Configuration file can be downloaded from CTFd's link VPN. Your task is to activate VPN and visit the testing page.

May you have fair winds and following seas!

Testing page is available at http://vpn-test.cns-jv.tcc.

Hint 1: https://openvpn.net/community-resources/reference-manual-for-openvpn-2-4/

Hint 2: Do not run more different VPNs at once.

## Řešení

1. stáhnout ctfd_ovpn.ovpn soubor
     * lze si na to udělat i spouštěč na plochu:
```
[Desktop Entry]
Version=1.0
Type=Application
Name=CATCH2022
Comment=
Exec="sudo /usr/sbin/openvpn /home/kali/Documents/CTF/CATCH/2023/ctfd_ovpn.ovpn"
Icon=/home/kali/Documents/CTF/CATCH/cesnet_catch.png
Path=/home/kali/Documents/CTF/CATCH
Terminal=true
StartupNotify=false
```
	 
2. přidat si do /etc/resolv.conf server 10.99.0.1 např. pomocí skriptu: `sudo bash -c "echo 'nameserver 10.99.0.1' > /etc/resolv.conf"`
     * úprava ctfd_ovpn.ovpn souboru pro přidání nastavení DNS mně nefungovala
3. zobrazit si požadovanou stránku z URL
4. `FLAG{smna-m11d-hhta-ONOs}`