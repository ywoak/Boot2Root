# SSH Username Enum attack

On our openssh version (OpenSSH_5.9p1) there is a vulnerability that allow an attacker to perform an username enumeration attack
Less flashy than a password vulnerability i'll admit
The CVE assigned to this issue is CVE-2018-15473
And its also an easier way to exploit openssh than the previous timing attacks used to perform username enumeration

This is because of this bit of code ```
  87 static int
  88 userauth_pubkey(struct ssh *ssh)
  89 {
 ...
 101         if (!authctxt->valid) {
 102                 debug2("%s: disabled because of invalid user", __func__);
 103                 return 0;
 104         }
 105         if ((r = sshpkt_get_u8(ssh, &have_sig)) != 0 ||
 106             (r = sshpkt_get_cstring(ssh, &pkalg, NULL)) != 0 ||
 107             (r = sshpkt_get_string(ssh, &pkblob, &blen)) != 0)
 108                 fatal("%s: parse request failed: %s", __func__, ssh_err(r));```

As explained very clearly by the Qualys Security Advisory Team :
 The attacker can try to authenticate a user with a malformed packet (for
example, a truncated packet), and:

- if the user is invalid (it does not exist), then userauth_pubkey()
  returns immediately, and the server sends an SSH2_MSG_USERAUTH_FAILURE
  to the attacker;

- if the user is valid (it exists), then sshpkt_get_u8() fails, and the
  server calls fatal() and closes its connection to the attacker.


To run the exploit (which was publicly available, credit in the exploit file header)
type `python CVE-2018-15473.py --port 22 --username {username/userlit to test} {boxip}`

For example with zaz we get : zaz is a valid user!
And with false we get : false is not a valid user!
