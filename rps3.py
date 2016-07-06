#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import random
os.system('clear')

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	def disable(self):
		self.HEADER = ''
		self.OKBLUE = ''
		self.OKGREEN = ''
		self.WARNING = ''
		self.FAIL = ''
		self.ENDC = ''
print bcolors.FAIL + "Taş Kağıt Makas oyununa hoşgeldiniz!" + bcolors.ENDC
o=input(bcolors.OKBLUE + "Oyuncu sayısını girin:" + bcolors.ENDC)
if o == 0:
	exit()
x=input(bcolors.OKBLUE + "Oyun  kaçta biter?:" + bcolors.ENDC)

print " "
#taş(t)
#kağıt(k)
#makas(m)
oyuncu=[]
puan=[]
sira=[]
r=0
s=1
f=0
tas=["m"]
kagit=["t"]
makas=["k"]

if o == 1:
	o=2
	r=1

for i in range (0,o):
	oyuncu.append(i)
	puan.append(0)

def tas():
	#print sira.index("t")
	#print sira.count("m")
	try:
		#puan[sira.index("t")] = int(puan[sira.index("t")]) + int(sira.count("m"))
		for i in range (0,o):
			if sira[i] == "t":
				puan[i] = int(puan[i]) + int(sira.count("m"))
	except ValueError:
		pass
def kagit():
	#print sira.index("k")
	#print sira.count("t")
	try:
		#puan[sira.index("k")] = int(puan[sira.index("k")]) + int(sira.count("t"))
		for i in range (0,o):
			if sira[i] == "k":
				puan[i] = int(puan[i]) + int(sira.count("t"))
	except ValueError:
		pass
def makas():
	#print sira.index("m")
	#print sira.count("k")
	try:
		#puan[sira.index("m")] = int(puan[sira.index("m")]) + int(sira.count("k"))
		for i in range (0,o):
			if sira[i] == "m":
				puan[i] = int(puan[i]) + int(sira.count("k"))
	except ValueError:
		pass

print "Oyuncular: %s" %(oyuncu)
#puan[0]=9
print "Puanlar: %s" %(puan)

while r != 1:
	print " "
	print "%s. tur" %(s)
	for i in range (0,o):
		print "TAŞ:t KAĞIT:k MAKAS:m"
		sira.append(raw_input(bcolors.OKBLUE + "HANGİSİ:" + bcolors.ENDC))
		os.system('clear')
	tas()
	kagit()
	makas()
	print sira
	del sira[:]
	s=s+1
	print "Puan: %s" %(puan)
	for i in range (0,o):
		if puan[i] >= x:
			print bcolors.FAIL + "%s. oyuncu kazandı"  %(int(i)+1) + bcolors.ENDC
			r=1

while f != 1:
	print " "
	print "%s. tur" %(s)
	print "TAŞ:t KAĞIT:k MAKAS:m"
	sira.append(raw_input(bcolors.OKBLUE + "HANGİSİ:" + bcolors.ENDC))
	sira.append(random.choice(["t","k","m"]))
	os.system('clear')
	tas()
	kagit()
	makas()
	print sira
	del sira[:]
	s=s+1
	print "Puan: %s" %(puan)
	for i in range (0,o):
		if puan[i] >= x:
			if i == 0:
				print bcolors.FAIL + "1. oyuncu kazandı." + bcolors.ENDC
			if i == 1:
				print bcolors.FAIL + "Bilgisayar kazandı." + bcolors.ENDC
			f=1
			exit()
