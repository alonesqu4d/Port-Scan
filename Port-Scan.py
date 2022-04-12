#!/usr/bin/env python

import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Port Scan")
print("")
print("Coded By Alonesqu4d")
print("""
Port Taramaya Hoşgeldiniz!

1-) 1. Seviye Tarama
2-) 2. seviye Tarama
3-) 3. Seviye Tarama
""")

islemnumara = input("Tarama Seviyesini Seçiniz: ")

if (islemnumara == "1"):
	hedefip = input("Hedef İp Adresini Giriniz: ")
	os.system("nmap " + hedefip)

elif (islemnumara == "2"):
	hedefip = input("Hedef İp Adresini Giriniz: ")
	os.system("nmap -sS -sV " + hedefip)

elif (islemnumara == "3"):
	hedefip = input("Hedef İp Adresini Giriniz: ")
	os.system("nmap -O " + hedefip)

else: 
	print("Böyle Bir Seçenek Bulunamadı!")
