import os
from datetime import datetime
now = datetime.now()
time = now.strftime("%Y.%m.%d.")

data = []
data_o = open("data.txt", encoding="utf-8")
data_o.readline() 
for row in data_o.readlines():
    data_s = row.strip().split(";")
    re = {}
    re["szam"] = int(data_s[0])
    re["nev"] = data_s[1]
    re["szul_ido"] = data_s[2]
    data.append(re)

szov = []
szov_o = open("szoveg.txt", "r", encoding="utf-8")
for row in szov_o.readlines():
    szov_d = row.strip().split(" ")
    szov.append(szov_d)


def fileContent(data, szov, sajatAdat):
    szoveg =""
    for x in range(len(szov)):
        g = ' '.join(szov[x])
        szoveg += g + "\n"
    
    fsad0 = szoveg.replace("x.nev", sajatAdat[0])
    fsad1 = fsad0.replace("x.szul", sajatAdat[1])
    return fsad1


def findFile(mappa_hely, fajl_nev):
    for root,dirs, files in os.walk(mappa_hely):
        for file in files:
            if file == fajl_nev:
                return True

def newFolder(data, fajl_nev, mappa_hely, szov, sajatAdat):
    os.makedirs(mappa_hely, exist_ok=True)
    

    file_content = fileContent(data, szov, sajatAdat)
    file_path = os.path.join(mappa_hely,fajl_nev)
    with open(file_path, 'a', encoding="utf-8") as file:
        file.write(file_content)


def fileCreate(data, szov):
    mappa_hely = "./nevek/"
    for x in data:

        sajatAdat = []
        sajatAdat.append(x["nev"])
        sajatAdat.append(x["szul_ido"])


        fajl_nev = x["nev"] + ".txt"


        igaz = findFile(mappa_hely,fajl_nev)
        if igaz == True:
            print("van ilyen fájl")
        else:
            newFolder(data, fajl_nev, mappa_hely, szov, sajatAdat)


fileCreate(data, szov)