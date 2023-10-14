import time, os
from tkinter import *

def getTime():
	timer = time.ctime()
	time1 = timer.split(" ")[3]
	return time1.split(":")

def convert(a):
	if a.isdigit():
		b = int(a)
		return b
	else:
		return 0

def algo(a):
	b = [
		[32, 16, 8, 4, 2, 1],
		[32, 16, 8, 4, 2, 1],
		[32, 16, 8, 4, 2, 1]
	]
	c = []
	d = ""
	a1 = "[1]"
	b1 = "[0]"
	for e in b[0]:
		c.append(a // e)
		a %= e
	for e in c:
		d += f"[{e}]"
	
	return d

def run():
	timer = getTime()
	hr =  convert(timer[0])
	min = convert(timer[1])
	sec = convert(timer[2])
	print(algo(hr))
	print(algo(min))
	print(algo(sec))
	time.sleep(.1)
	os.system("cls")

def start():
	base = Tk()
	base.geometry("500x500")

	h = Label(base, text="32", font=("", 20), width=5)
	h.grid(row=0, column=0)

	h1 = Label(base, text="16", font=("", 20), width=5)
	h1.grid(row=0, column=1)
	
	h2 = Label(base, text="8", font=("", 20), width=5)
	h2.grid(row=0, column=2)

	h3 = Label(base, text="4", font=("", 20), width=5)
	h3.grid(row=0, column=3)

	h4 = Label(base, text="2", font=("", 20), width=5)
	h4.grid(row=0, column=4)

	h5 = Label(base, text="1", font=("", 20), width=5)
	h5.grid(row=0, column=5)

	m = Label(base, text="32", font=("", 20), width=5)
	m.grid(row=1, column=0)

	m1 = Label(base, text="16", font=("", 20), width=5)
	m1.grid(row=1, column=1)
	
	m2 = Label(base, text="8", font=("", 20), width=5)
	m2.grid(row=1, column=2)

	m3 = Label(base, text="4", font=("", 20), width=5)
	m3.grid(row=1, column=3)

	h4 = Label(base, text="2", font=("", 20), width=5)
	h4.grid(row=1, column=4)

	h5 = Label(base, text="1", font=("", 20), width=5)
	h5.grid(row=0, column=5)

	h = Label(base, text="32", font=("", 20), width=5)
	h.grid(row=0, column=0)

	h1 = Label(base, text="16", font=("", 20), width=5)
	h1.grid(row=0, column=1)
	
	h2 = Label(base, text="8", font=("", 20), width=5)
	h2.grid(row=0, column=2)

	h3 = Label(base, text="4", font=("", 20), width=5)
	h3.grid(row=0, column=3)

	h4 = Label(base, text="2", font=("", 20), width=5)
	h4.grid(row=0, column=4)

	h5 = Label(base, text="1", font=("", 20), width=5)
	h5.grid(row=0, column=5)


	base.mainloop()

	
if __name__ == "__main__":
	start()