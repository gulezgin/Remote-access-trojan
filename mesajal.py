#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.2.10", 7778))
print("HACKER...")

while True:
	mesaj=s.recv(1024)
	print("DOLI: "+mesaj)
	if mesaj=="0":
		print("Sunucu, Karşı taraf tarafından sonlandırıldı")
		break
	else:
		cevap=raw_input("Cevabınızı yazın: ")
		s.send(cevap)
s.close