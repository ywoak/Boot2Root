# Ret2Libc

When we follow the standard path until the zaz executable we can not only exploit it with shellcode like we did in the mandatory part
But also with a standard Ret2Libc exploitation
Since `ldd .exploit_me` show us the libc in use and linked to the program, as well as `info func` inside gdb
And the kernel aslr isnt activated so it will be a huge help for an easy ret2libc

## Info
We first need to load the program into gdb so that the libc is loaded and the virtual mem is assigned to the program
Then we need to get info on the location of libc function and get a str pointer to a shell for system future argument
`file ./exploit_me` `print &system, print &exit, find &system, +99999999, "/bin/sh"`
We could have also used an env variable in which we store "/bin/sh" if we couldnt find the str* in memory
We store the info in our python script (check the Script folder -> r2lc.py)

## Offset
We determine how much the offset to overwrite is until the saved eip before the main stack frame
(we already did the shellcode method so its easier but for the sake of this readme lets assume not)
First method i used was just typing randomly 'A' *x until our program execution segfault
Smarter is `i r` `info frame` so we can either sub address of $eip to $esp
Or just `print $ebp+4` since before the ebp push the next thing on the stack was the saved eip

## Payload
The payload is a standard Ret2Libc payload, with system + exit + /bin/sh
When we overwrite the saved eip it changes the address that the return instruction jumps to
Here we replaced it with system() with "/bin/sh" argument, and the return address is exit
Exit is just to make it clean because since we're not going to return after the system("/bin/sh")
It might also prevent a sysadmin to notify a segfault in an imaginary world so why not

./exploit_me $(python r2lc.py) -> `whoami` -> `root`

By the way the shell we get with this is interactive but we're still under the ruid of zaz
and only the euid of root, as its often the case with suid binary privEsc (`id` to verify that)
To make it fully interactive as a native root process just add zaz to sudo group so you can sudo su
Then passwd everything for easier post exploit manipulation
