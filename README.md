# Boot2Root

After downloading the vulnerable iso and mouting it on a fresh linux vm
We notice that we dont have an ip nor any login quickly available
First step would be to get those

# Get vulnerable machine IP
Configure network in bridged (Easiest to setup but NAT or host-only is possible) in VBox Settings

# Scan whole network
`nmap -n -sV foundip-254`
Will get us the machine ip and scan for open port on it to give us a potential access point
Alternatively we can just scan for lan device with `nmap -sn ip/24` for an ip
Then `nmap machineip` for a similar/faster result
