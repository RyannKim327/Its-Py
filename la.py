import time

a = [
	[8, 4, 2, 1],
	[8, 4, 2, 1],
	[8, 4, 2, 1],
	[8, 4, 2, 1]
]


def getTime():
	timer = time.ctime()
	time1 = timer.split(" ")[3]
	return tuple(time1.split(":"))

def convert(a):
	if a.isdigit():
		return int(a) % 12
	else:
		return 0

def start():
	