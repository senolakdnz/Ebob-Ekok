# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:36:30 2024

@author: Şenol AKDENİZ
"""

print("Ekok Bulma Programı")

def ekok(a,b):
    i=2
    ekok = 1
    
    while True:
        if(a%i==0 and b%i==0):
            ekok *= i
            a /= i
            b /= i
        elif(a%i==0 and b%i!=0):
            ekok *= i
            a/=i
        elif(a%i!=0 and b%i==0):
            ekok *= i
            b/=i
        else:
            i += 1
        if(a==1 and b==1):
            break
    return ekok

sayi1 = int(input("Lutfen birinci sayiyi giriniz. : "))
sayi2 = int(input("Lutfen ikinci sayiyi giriniz. : "))

print("Ekok : ",ekok(sayi1, sayi2))