#!/usr/bin/python3
from time import sleep

# ==============================================================================
# initialize functions and variables
def write(report):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())
def rwrite(report):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report)
def clear_buffer():
	write(zero*8)
zero = chr(0)
# ==============================================================================

# begin script


# wait for window focus change
sleep(5)




# 				    TEST 1
# 			      writing basic chars
# write the alphabet
for i in range(4,30):
	write(zero*2+chr(i)+zero*5)
	clear_buffer()

# write numerals
for i in range(30,40):
	write(zero*2+chr(i)+zero*5)
	clear_buffer()

# write enter
write(zero*2+chr(40)+zero*5)
clear_buffer()

# write ESC
write(zero*2+chr(41)+zero*5)
clear_buffer()

# write backspace
write(zero*2+chr(42)+zero*5)
clear_buffer()

# write tab
write(zero*2+chr(43)+zero*5)
clear_buffer()

# write enter twice for new test
write(zero*2+chr(40)+zero*5)
clear_buffer()
write(zero*2+chr(40)+zero*5)
clear_buffer()

#				    TEST 2
#			 writing obsceure chars + F*
# write misc. characters up to caps lock
for i in range(45,57):
	write(zero*2+chr(i)+zero*5)
	clear_buffer()

# write F* chars, should hear 9 boops
#for i in range(58,70):
#	write(zero*2+chr(i)+zero*5)
#	clear_buffer()
#	sleep(0.5)				# no longer active for testing

# write enter twice for new test
write(zero*2+chr(40)+zero*5)
clear_buffer()
write(zero*2+chr(40)+zero*5)
clear_buffer()

#				    TEST 3
#			       tests with caps
# write capitalized 'a' as demonstrated -- why does this work??
write(chr(32)+zero+chr(4)+zero*5)
clear_buffer()

# sub-tests
write(chr(1)+zero+chr(4)+zero*5)
clear_buffer()

