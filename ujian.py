from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
data=requests.get('http://digidb.io/digimon-list/')
soup=BeautifulSoup(data.content,'html.parser')
data = soup.find('table', id='digiList')
kolom=[]
for i in soup.find_all('th'):
    kolom.append(i.string)
# print(kolom)
digimon=[]
data=data.find_all('tr')
for item in data[1:]:
    no=item.td.string
    nama=item.a.string
    gambar=item.img['src']
    stage=item.center.string
    typeDigi=item.td.find_next_sibling().find_next_sibling().find_next_sibling()
    attribute=item.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
    memory=attribute.find_next_sibling()
    equip=memory.find_next_sibling()
    HP=equip.find_next_sibling()
    SP=HP.find_next_sibling()
    attack=SP.find_next_sibling()
    defense=attack.find_next_sibling()
    intellegence=defense.find_next_sibling()
    speed=intellegence.find_next_sibling()
    x={
        'No':int(no),
        'Nama':nama,
        'Pic':gambar,
        'Stage':stage,
        'Type':typeDigi.string,
        'attribute':attribute.string,
        'memory':memory.string,
        'equip':equip.string,
        'HP':HP.string,
        'SP':SP.string,
        'attack':attack.string,
        'defense':defense.string,
        'intellegence':intellegence.string,
        'speed': speed.string}
    digimon.append(x)
# print(digimon)
#Save to Json
import json
with open('dataDigi.json','w') as x:
    x.write(str(digimon).replace("'",'"'))


    
