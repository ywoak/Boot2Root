# Nano sudo PrivEsc

There is a lot of binary that can be used against their intended purposes/in specific unintuitive way
Sometimes its as helpful as giving us an interactive shell when we're stuck with awk for example
But when used on an account with sudo rights those types of binary hack can also be used as a PrivEsc tool
Ofc for the demonstration here all binary are allowed to be run as sudo, so it wont be as impressive considering you could just `sudo /bin/sh`
But if a user was only allowed sudo on a single/very few binary `sudo -l` it's a little privEsc technique thats still worth noting
Especially on binary when you dont think could lead to a privEsc at first glance like nano

On this box the only account that is allowed to run sudo command except for root is ft_root since its the only account thats part of the sudo groups `cat /etc/group`
So we'll need to get an euid root shell via bonus1 for example, and passwd ft_root to connect to it
Or for demonstration purpose visudo someone to sudoers on only one binary

Then from ressource "https://gtfobins.github.io/gtfobins/nano/" ->
'GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.
The project collects legitimate functions of Unix binaries that can be abused to get the f**k break out restricted shells, escalate or maintain elevated privileges, transfer files, spawn bind and reverse shells, and facilitate the other post-exploitation tasks.'

Limited SUID
If the binary has the SUID bit set, it may be abused to access the file system, escalate or maintain access with elevated privileges working as a SUID backdoor.
If it is used to run commands (e.g., via system()-like invocations) it only works on systems like Debian (<= Stretch) that allow the default sh shell to run with SUID privileges.
This example creates a local SUID copy of the binary and runs it to maintain elevated privileges.
To interact with an existing SUID binary skip the first command and run the program using its original path.
The SPELL environment variable can be used in place of the -s option if the command line cannot be changed.

sudo install -m =xs $(which nano) .

./nano -s /bin/sh
/bin/sh
^T

whoami -> root
