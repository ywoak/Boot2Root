# Boot2Root

We're given a vulnerable iso, and the end goal is to root it
The mandatory part of the project specify we need 2 methods to do it, if we find more method they're considered bonuses

We download the vulnerable iso, mout it on a fresh linux vm, launch the vm
There is no ip displayed in the vm attached to it 
Lets first retrive the machine ip

# Get vulnerable machine IP and scan for open ports
In the vm settings configure the network: we'll use bridge since its easy to setup
Get host ip address with something like `ip a`, then scan our local network
Then scan our network with `nmap -n -sV foundip-254`
This will get us the machine ip and scan for open port on it to give us a potential access point
Alternatively we can just scan for lan device with `nmap -sn ip/24` for an ip
Then `nmap machineip` for port scanning on the vuln machine ip

PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
143/tcp open  imap
443/tcp open  https
993/tcp open  imaps

# Scan webserver, get a broader picture of whats happening and where
imap and imaps are new to me, we'll use the ftp server and the ssh server for connection when we'll get credential
For now lets see what webserver is running on port 80 & 443, lets open it in a browser
Its a basic web page, lets scan the web content and try to get info on the system running
`dirb ip` --> `enum4linux -U -o ip`
Now we have a better picture of whats running what
With https (ports 443) there are some interesting url directory accessible -> /forum /webmail /phpmyadmin
The web server is apache v2.2.22
The webmail service is squirrelmail version 1.4.22
The forum service is mylittleforum version 2.3.4
If we find database credential its most likely phpmyadmin credential

## Now search for entrypoint and then look for PrivEsc vector if needed to root the system
Check readme of different method in the repo for different writeup
