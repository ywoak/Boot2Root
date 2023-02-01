# Init overwrite in syslinux shell

To be fair from what i understood afterward this isnt supposed to be a legitimate method depending on who's asking
Because the test box was made into an iso this wasnt protected but it wasnt an intended vulnerability at first
However i believe that :
1. For the sake of the readme to be complete
4. Since its not like im reading or modifying the iso in itself
2. Since it still thought me quite a bit
3. Since i used something very similar on my personnal setup a few days ago when i locked myself out of my display manager and my wm
i'll include it here

When the box is at its booting phase we can get into the boot prompt of syslinux (hold shift)
(i think its the one we're using on this system) and instead of just booting from live (since its not a persistent setup)
We can do it while specifying kernel parameter, one of them is init
So just live init='/bin/bash' and instead of letting init be called by the kernel as its last setup stage
and call /etc/rc.d/rcS.conf -> /etc/rc.d/rc.sysinit -> inittab -> getty
We can just force it to launch a root shell (since system isnt mounted or anything with the overwrite)
Its a 'rescue' technique that can be used by sysadmins when intended

Ressource: my beloved arch-wiki of course
bootloader page, syslinux/isolinux page, init page, kernel_parameter page
