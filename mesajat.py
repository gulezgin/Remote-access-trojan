#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
from colorama import Fore, init
init(autoreset="true")

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL.SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("10.0.2.10", 7778))
s.listen(1)
print(Fore.WHITE+ "Kurbanın Bağlantı Kurması Bekleniyor.")
kurban, ip=s.accept()
print(Fore.GREEN+ "Kurban İle Bağlantı Sağlandı!")
print(Fore.BLUE+ "Kurban: %s" % str(ip))
print(Fore.CYAN+ "0 ==> Mesajlaşmayı bitir")

while True:
	mesaj=raw_input("Mesajınızı Yazın: ")
	if mesaj=="0":
		kurban.send(mesaj)	
		print(Black.RED+ "Programdan Çıkış Yapıldı")
		break
	else:
		kurban.send(mesaj)	
		cevap=kurban.recv(1024)
		print(Fore.YELLOW+ "HEDEF: "+cevap)
s.close