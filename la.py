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

def algo(a, w):
	b = [
		[32, 16, 8, 4, 2, 1],
		[32, 16, 8, 4, 2, 1],
		[16, 8, 4, 2, 1]
	]
	c = []
	d = ""
	a1 = "[1]"
	b1 = "[0]"
	for e in b[0]:
		c.append(a // e)
		a %= e
	for e in range(len(c)):
		# d += f"[{e}]"
		if c[e] == 1:
			w[e].config(bg="#aaaaaa", fg="#131320")
		else:
			w[e].config(bg="#131320", fg="#131320")

def run():
	global hs, ms, ss
	timer = getTime()
	hr =  convert(timer[0])
	min = convert(timer[1])
	sec = convert(timer[2])
	algo(hr, hs)
	algo(min, ms)
	algo(sec, ss)
	base.after(1, run)

def start():
	global hs
	global ms
	global ss
	global base
	
	base = Tk()
	base.geometry("500x500")

	fh = Frame(base)

	h = Label(fh, text="32", bg="red", font=("", 20))
	h.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h1 = Label(fh, text="16", bg="blue", font=("", 20))
	h1.pack(padx=1, pady=1, side='left', fill='both', expand=True)
	
	h2 = Label(fh, text="08", bg="red", font=("", 20))
	h2.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h3 = Label(fh, text="04", bg="red", font=("", 20))
	h3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h4 = Label(fh, text="02", bg="red", font=("", 20))
	h4.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h5 = Label(fh, text="01", bg="red", font=("", 20))
	h5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	fh.pack(padx=1, pady=1, fill='both', expand=True)

	fm = Frame(base)

	m = Label(fm, text="32", bg="red", font=("", 20))
	m.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m1 = Label(fm, text="16", bg="blue", font=("", 20))
	m1.pack(padx=1, side='left', fill='both', expand=True)
	
	m2 = Label(fm, text="08", bg="red", font=("", 20))
	m2.pack(padx=1, side='left', fill='both', expand=True)

	m3 = Label(fm, text="04", bg="red", font=("", 20))
	m3.pack(padx=1, side='left', fill='both', expand=True)

	m4 = Label(fm, text="02", bg="red", font=("", 20))
	m4.pack(padx=1, side='left', fill='both', expand=True)

	m5 = Label(fm, text="01", bg="red", font=("", 20))
	m5.pack(padx=1, side='left', fill='both', expand=True)

	fm.pack(padx=1, fill='both', expand=True)

	fs = Frame(base)

	s = Label(fs, text="32", bg="red", font=("", 20))
	s.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s1 = Label(fs, text="16", bg="blue", font=("", 20))
	s1.pack(padx=1, pady=1, side='left', fill='both', expand=True)
	
	s2 = Label(fs, text="08", bg="red", font=("", 20))
	s2.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s3 = Label(fs, text="04", bg="red", font=("", 20))
	s3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s4 = Label(fs, text="02", bg="red", font=("", 20))
	s4.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s5 = Label(fs, text="01", bg="red", font=("", 20))
	s5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	fs.pack(padx=1, pady=1, fill='both', expand=True)

	hs = [h, h1, h2, h3, h4, h5]
	ms = [m, m1, m2, m3, m4, m5]
	ss = [s, s1, s2, s3, s4, s5]

	run()

	base.mainloop()

def start2():
	base = Tk()
	base.geometry("500x500")

	fh = Frame(base)

	h = Label(fh, text="32", bg="red", font=("", 20))
	h.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h1 = Label(fh, text="16", bg="blue", font=("", 20))
	h1.pack(padx=1, pady=1, side='left', fill='both', expand=True)
	
	m = Label(fm, text="32", bg="red", font=("", 20))
	m.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	m1 = Label(fm, text="16", bg="blue", font=("", 20))
	m1.pack(padx=1, side='left', fill='both', expand=True)
	
	h2 = Label(fh, text="08", bg="red", font=("", 20))
	h2.pack(padx=1, pady=1, side='left', fill='both', expand=True)



	h3 = Label(fh, text="04", bg="red", font=("", 20))
	h3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h4 = Label(fh, text="02", bg="red", font=("", 20))
	h4.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	h5 = Label(fh, text="01", bg="red", font=("", 20))
	h5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	fh.pack(padx=1, pady=1, fill='both', expand=True)

	fm = Frame(base)

	
	m2 = Label(fm, text="08", bg="red", font=("", 20))
	m2.pack(padx=1, side='left', fill='both', expand=True)

	m3 = Label(fm, text="04", bg="red", font=("", 20))
	m3.pack(padx=1, side='left', fill='both', expand=True)

	m4 = Label(fm, text="02", bg="red", font=("", 20))
	m4.pack(padx=1, side='left', fill='both', expand=True)

	m5 = Label(fm, text="01", bg="red", font=("", 20))
	m5.pack(padx=1, side='left', fill='both', expand=True)

	fm.pack(padx=1, fill='both', expand=True)

	fs = Frame(base)

	s = Label(fs, text="32", bg="red", font=("", 20))
	s.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s1 = Label(fs, text="16", bg="blue", font=("", 20))
	s1.pack(padx=1, pady=1, side='left', fill='both', expand=True)
	
	s2 = Label(fs, text="08", bg="red", font=("", 20))
	s2.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s3 = Label(fs, text="04", bg="red", font=("", 20))
	s3.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s4 = Label(fs, text="02", bg="red", font=("", 20))
	s4.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	s5 = Label(fs, text="01", bg="red", font=("", 20))
	s5.pack(padx=1, pady=1, side='left', fill='both', expand=True)

	fs.pack(padx=1, pady=1, fill='both', expand=True)
	
if __name__ == "__main__":
	start2()