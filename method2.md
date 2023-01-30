# CVE-2016-5195 Dirty Cow -- Pokemon Edition

With some PrivEsc tool scan of our system on any of our account (see scripts and scp them)
a recurring theme is the kernel vulnerability of the DirtyCow vulnerability and DirtyCow2
Here we use the DirtyCow2 firefart version of the PoC based on the pokemon vulnerability (again just check the file in /Scripts)
Once our user is created, su on it, swap back /etc/passwd with the .bak in /tmp and voila we're root on a interactive shell with a new user



(Credit for the LiveOverflow youtube video on DirtyCow for 1. The idea, 2. Understanding of it)
