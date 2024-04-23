# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:23:54 2024

@author: Şenol AKDENİZ
"""

print("Ebob Bulma Programı")

def ebob(a,b):
    i = 1
    ebob = 1
    while(i<=a and i<=b):
        if(a%i==0 and b%i==0):
            ebob = i
        i += 1
    return ebob

sayi1 = int(input("Lutfen birinci sayiyi giriniz. : "))
sayi2 = int(input("Lutfen ikinci sayiyi giriniz. : "))

print("Ebob : ",ebob(sayi1, sayi2))