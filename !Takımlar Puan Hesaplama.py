# -*- coding: utf-8 -*-
import re


print("\n")
print("Süperlig = s , 1.lig = 1 , 2.lig = 2 ..")

lig = input("Lig İsmini Giriniz : ")

maç_dict = {"s" : "SUPERLIG", "1" : "1.LIG" , "2" : "2.LIG"}

takım_dict = {"s": "T_SUPERLIG" , "1": "T_1.LIG" , "2" : "T_2.LIG"}

maç_dosya = "{0}".format(maç_dict[lig]) + ".txt"

takım_dosya = "{0}".format(takım_dict[lig]) + ".txt"

def RemoveDuplicates(liste):
    
    new = []
    
    for i in range(len(liste)):
        
        
        if liste[i] not in new:
            new.append(liste[i])
            
    liste = new
    
    return new

class Takım:
    def __init__(self,isim,galibiyet,mağlubiyet,beraberlik,atg,yeg):
        self.isim = isim
        self.galibiyet = galibiyet
        self.mağlubiyet = mağlubiyet
        self.beraberlik = beraberlik
        self.atg = atg
        self.yeg = yeg

        
#TAKIMLARI LİSTELEME VE CLASS LARA ATAMA İŞLEMLERİ

t_dosya = open(takım_dosya,"r",encoding="utf-8")
    
takımlar = t_dosya.read().splitlines()

if lig == "s":
    takımlar[0] = 'Alanyaspor'
elif lig == "1":
    takımlar[0] = 'Ümraniyespor'
    
Takımlar = []

for i in range(18):
    Takımlar.append(Takım(takımlar[i],0,0,0,0,0))
   
t_dosya.close()

#MAÇLARI ANALİZ ETME

m_dosya = open(maç_dosya,"r",encoding="utf-8")

for line in m_dosya.readlines():
    
    satır = r"{0}".format(line)
    
    sayılar = r"[0-9]"

    boşluk = r" "
    
    skorlar = re.findall(sayılar,satır)
    
    skorlar[0] = int(skorlar[0])
    
    skorlar[1] = int(skorlar[1])
    
    rakip1 = ""
    
    rakip2 = ""
    
    for char in satır:
        
        if char != "-":
            rakip1 = rakip1 + char
        else:
            break
    
    satır = satır.replace(rakip1 + "-","")        #satırdan ilk rakibi sil 
    
    for char in satır:
        
        if char != "=":
            rakip2 = rakip2 + char
        else:
            break
        
    rakip1 = rakip1.strip("\ufeff") 
    
    rakipTakım = ""
    
    for i in range(18):
        
        if Takımlar[i].isim == rakip2:
            
            Takımlar[i].atg += skorlar[1]
            
            Takımlar[i].yeg += skorlar[0]
            
            if skorlar[1] == skorlar[0]:
                
                Takımlar[i].beraberlik += 1
            
            elif skorlar[1] < skorlar[0]:
                
                Takımlar[i].mağlubiyet += 1
                
            elif skorlar[1] > skorlar[0]:
                
                Takımlar[i].galibiyet += 1
            
            
            
    for i in range(18):
        
        if Takımlar[i].isim == rakip1:
            
            Takımlar[i].atg += skorlar[0]
            
            Takımlar[i].yeg += skorlar[1]
            
            if skorlar[0] > skorlar[1]:
                
                Takımlar[i].galibiyet += 1
                
            elif skorlar[0] == skorlar[1]:
                
                Takımlar[i].beraberlik += 1
                
            elif skorlar[0] < skorlar[1]:
                
                Takımlar[i].mağlubiyet += 1
                
        
m_dosya.close()

takım_sıralaması = []

puanlar = []

puan_sıralaması = []

Takım_Sıralaması = []
#puanları listele
for i in range(18):
    
    takım = Takımlar[i]
    
    takım.oynananOyunlar = takım.galibiyet + takım.mağlubiyet + takım.beraberlik
    
    takım.averaj = takım.atg - takım.yeg
    takım.oynanan_oyunlar = takım.galibiyet + takım.mağlubiyet + takım.beraberlik
    takım.puan = (3 * takım.galibiyet) + takım.beraberlik
    
    puanlar.append(takım.puan)
#puanları sıralama    
for i in range(18):
    
    max_puan = max(puanlar)
    puan_sıralaması.append(max_puan)
    puanlar.remove(max_puan)    

puan_sıralaması = list(set(puan_sıralaması)) #duplicate leri sil

puan_sıralaması.reverse()

#takımları puana göre sırala
while (True):
    try:
        for i in range(18):
                
            takım = Takımlar[i]
                
            if takım.puan == puan_sıralaması[0]:
                    
                takım_sıralaması.append(takım)
        
        puan_sıralaması.remove(puan_sıralaması[0])
    except IndexError:
        break
 
averajlar = []

averaj_sıralaması = []

running = True

while running:

        for i in range(18):
            
                takım = takım_sıralaması[i]
                
                if i != 0:
                    
                    önceki_takım = takım_sıralaması[i-1]
                    
                if i != 17:
                    sonraki_takım = takım_sıralaması[i + 1]
                        
                if takım.puan != sonraki_takım.puan:
                    
                    averajlar.append(takım.averaj)
                    
                        
                    for i in range(len(averajlar)):
                            
                        max_av = max(averajlar)
                           
                        averaj_sıralaması.append(max_av)
                            
                        averajlar.remove(max_av)
                    
                    averaj_sıralaması.append("|")
                    
                    averajlar = []
                        
                else:
                        
                    averajlar.append(takım.averaj)
                    
                if i == 17:
                    
                    #print(averajlar)
                    
                    for i in range(len(averajlar)):
                        
                        max_av = max(averajlar)
                        
                        averaj_sıralaması.append(max_av)
                        
                        averajlar.remove(max_av)

                    averaj_sıralaması.append("|")
                    
                    
                    running = False
                    




averaj_grupları = []

Averaj_Grupları = []

takım_grupları = []

index = 0

access = True

Takım_Sıralaması = []

for i in range(len(averaj_sıralaması)):
    
    averaj1 = averaj_sıralaması[i]
    
    if averaj1 != "|":
        
        averaj_grupları.append(averaj1)
        
    else:
        
        
        
        for i in range(len(averaj_grupları)):
            
            
            takım = takım_sıralaması[index]
            
            takım_grupları.append(takım)
            
            index += 1
         
        
        for i in range(len(averaj_grupları)):
            
            max_Av = max(averaj_grupları)
            
            Averaj_Grupları.append(max_Av)
            
            averaj_grupları.remove(max_Av) 
            
        
        Averaj_Grupları = RemoveDuplicates(Averaj_Grupları)
        
        
        
        for i in range(len(Averaj_Grupları)):
            
            Averaj = Averaj_Grupları[i]
            
            for i in range(len(takım_grupları)):
                
                takım = takım_grupları[i]
                
                if takım.averaj == Averaj:
                    
                    Takım_Sıralaması.append(takım)
            

        
        takım_grupları = []
        
        averaj_grupları = []
        
        Averaj_Grupları = []
    
             


print("TAKIM ADI                OyM   G   B   M   ATG   YEG   Avj.   Puan")
print("-------------------------------------------------------------------")
for i in range(len(Takım_Sıralaması)):
    
    takım = Takım_Sıralaması[i]
    
    if(takım.averaj < 0):
        print("{0}".format(takım.isim) + (" " * (26-len(takım.isim))) + "{0}    {1}   {2}   {3}    {4}     {5}    {6}       {7}".format(takım.oynananOyunlar,takım.galibiyet,takım.beraberlik,takım.mağlubiyet,takım.atg,takım.yeg,takım.averaj,takım.puan))
        
    else:
        print("{0}".format(takım.isim) + (" " * (26-len(takım.isim))) + "{0}    {1}   {2}   {3}    {4}     {5}     {6}       {7}".format(takım.oynananOyunlar,takım.galibiyet,takım.beraberlik,takım.mağlubiyet,takım.atg,takım.yeg,takım.averaj,takım.puan))
    
    print("-------------------------------------------------------------------")                                              


























