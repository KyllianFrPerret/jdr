import random

def lire_txt():
    liste=[]
    with open ("text.txt",'r',encoding="utf-8") as fichier :
        i= fichier.readlines()
    return i



def tourpartour(pvmc, pvmonstre,objet,min,max,vie):
    while not (pvmc <0 or pvmonstre <0 ):
        print(f'pv enemie:{pvmonstre} \npv :{pvmc}\nattaque: a \ndouble lancée: d \ndéfense: n \nobjet: o ')
        a= input (":")
        while not (a=="a" or a=="d" or a=="n" or a=="o"):
            print("choix invalide\n")
            a= input (":")
        attaquemc=0
        attaqueméchant=random.randint(min, max)
        if a=="a":
            attaquemc= random.randint(7, 15)
            pvmonstre=pvmonstre-attaquemc
            print (f'attaque inflige {attaquemc}')
        if a=="d":
            for i in range (2):
                attaquemc= random.randint(8, 14)
                print (f'attque {i+1}fait {attaquemc}')
                pvmonstre=pvmonstre-attaquemc
        if a=="n":
            attaqueméchant= attaqueméchant // 2
        if a=="o":
            if objet==[]:
                print("inventaire vide")
            else:
                b=input("voulez vous utiliser cette objet \n y/n\n")
                if b=="y":
                    pvmc=pvmc+10
        pvmc=pvmc-attaqueméchant
        print(f"l'enemi vous inflige {attaqueméchant} dégats\n")
    if pvmc<0:
        vie=False
        print("mort\n")
    return vie , pvmc, objet



def etape1(moral,pvmc,objet,vie,text):
    choix1="p"
    print(text[5])
    while not (choix1=="o" or choix1=="n" ):
        print(text[6])
        choix1=input("o/n\n")
    if choix1=="o":
        print(text[7])
        vie , pvmc, objet=tourpartour(pvmc, 10,objet,0,1,vie)
        print(text[8])
        moral=moral+1
    if choix1=="n":
            print(text[9])
    if vie==True:
        print(text[10])
        test=0
        choix1b="p"
        print(text[11])
        while not (choix1b=="o"):
            if test==0:
                print(text[12])
            if test==1:
                print(text[13])
            if test==3:
                print(text[14])
            if test==4:
                print(text[15])
            if test>4:
                print(text[16])
            choix1b=input("o/n\n")
            test=test+1
    print(text[17])
    return vie,pvmc,objet,vie,moral






def etape2(text):
    print(text[18])
    choix2="o"
    while not (choix2=="g" or choix2=="d" ):
        print(text[19])
        choix2=input("g/d\n")
    return choix2



def etape3(choix2,enfant,objet,pvmc,vie,moral,text):
    choix3G="p"
    choix3D="p"
    if choix2=="g":
        choix3G="p"
        print(text[20])
        while not (choix3G=="o" or choix3G=="n" ):
            print(text[21])
            choix3G=input("o/n\n")
        if choix3G=="o":
            print(text[22])
            enfant=1
    if choix2=="d":
        choix3D="p"
        print(text[23])
        while not (choix3D=="o" or choix3D=="n" ):
            print(text[24])
            choix3D=input("o/n\n")
        if choix3D=="o":
            print(text[25])
            vie , pvmc, objet=tourpartour(pvmc, 100,objet,6,15,vie)
            print(text[26])
            moral=moral+1
        if choix3D=="n":
            print(text[27])
    return enfant,objet,pvmc,vie,moral,choix3D






def etape4(choix2,enfant,objet,pvmc,vie,moral,choix3D,text):
    choix4D="p"
    choix4G="p"
    if choix2=="g":
        if enfant==0:
            print(text[47])
            vie , pvmc, objet=tourpartour(pvmc, 120,objet,4,17,vie)
            print(text[48])
        if enfant==1:
            choix4G="p"
            print(text[28])
            while not (choix4G=="o" or choix4G=="n" ):
                print(text[29])
                choix4G=input("o/n\n")
            if choix4G=="n":
                print(text[30])
                vie , pvmc, objet=tourpartour(pvmc, 120,objet,4,17,vie)
                print(text[31])
            if choix4G=="o":
                moral=moral+1
                print(text[32])
                enfant=0
    if choix2=="d":
        choix4D="p"
        if choix3D=="o":
            while not (choix4D=="o" or choix4D=="n"):
                print(text[33])
                choix4D=input("o/n\n")
            if choix4D=="o":
                print(text[34])
                objet=objet.append("potion")
            if choix4D=="n":
                print(text[35])
    return enfant,objet,pvmc,vie,moral,choix4D










def etape5(text):
    choix5="y"
    print(text[36])
    while not (choix5=="o" or choix5=="n"):
        print(text[37])
        choix5=input("o/n\n")
    return choix5



def etape6(pvmc,objet,choix4D,text):
    choix6="y"
    while not (choix6=="o" or choix6=="n"):
        print(text[38])
        choix6=input("o/n\n")
    if choix4D=="o":
            if choix6=="o":
                print(text[39])
                pvmc=pvmc+15
                objet=[]
            if choix6=="n":
                print(text[40])
    else:
            print(text[41])
    return objet,pvmc








def etape7(pvmc,objet,vie,text):
    print(text[42])
    vie,pvmc,objet=tourpartour(pvmc, 150,objet,10,20,vie)
    return vie



def etape8(moral,vie,text):
    if vie==True:
        if moral==0:
            print(text[43])
        if moral==1:
            print(text[44])
        if moral==2:
            print(text[45])
    if vie==False:
        print(text[46])




def jeu():
    text=lire_txt()
    pvmc= 90
    moral=0
    objet=[]
    print(text[1])
    print(text[2])
    nom=input(text[3])
    print(text[4]+nom)
    vie=True
    enfant=0
    vie,pvmc,objet,vie,moral=etape1(moral,pvmc,objet,vie,text)
    if vie==True:
        choix2=etape2(text)
    if vie==True:
        enfant,objet,pvmc,vie,moral,choix3D=etape3(choix2,enfant,objet,pvmc,vie,moral,text)
    if vie==True:
        enfant,objet,pvmc,vie,moral,choix4D=etape4(choix2,enfant,objet,pvmc,vie,moral,choix3D,text)
    if vie==True :
        choix5=etape5(text)
    if choix5=="o"and vie==True:
        objet,pvmc=etape6(pvmc,objet,choix4D,text)
    if vie==True :
        vie=etape7(pvmc,objet,vie,text)
    etape8(moral,vie,text)
    return



jeu()

#pip install ursina






