import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import copy
import pandas as pd
import datetime


class Scraper(object):
    def __init__(self, url):
        self.url = url

    def URLAutomobilaUcsv(self, iteracije):
        i = 1
        automobili = []
        danas = datetime.datetime.today()
        uso = False
        while i < iteracije:
            # Connect to the URL
            response = requests.get(self.url + str(i))
            temp = []
            # Parse HTML and save to BeautifulSoup object¶
            soup = BeautifulSoup(response.text, "html.parser")
            for data in soup.findAll('div', id='rezultatipretrage'):
                for text in data.findAll('div', {'class': "kada"}):
                    datum = text.get('title')
                    if datum is None:
                        continue
                    datum = datum.replace('u ', '')
                    date_time_obj = datetime.datetime.strptime(datum, '%d.%m.%Y. %H:%M')
                    yesterday = danas - datetime.timedelta(days=1)
                    if date_time_obj <= yesterday:
                        uso = True
                        break

                if uso:
                    break
                for link in data.findAll('a'):
                    temp.append(link['href'])
            if uso:
                break
            temp = list(dict.fromkeys(temp))
            automobili.extend(temp)
            print("Obrađeno: " + str(len(automobili)) + " automobila.")
            # time.sleep(0.5)
            i += 1

        automobili = list(set(automobili))
        df = pd.DataFrame(automobili)
        return df

    def ScrapeajDetalje(self, link, df):
        data = df
        auto = data.iloc[:, 0].values

        i = 0
        while i < len(auto):
            proizvodjac = []
            model = []
            Godiste = []
            Kilometara = []
            Gorivo = []
            Kilovata = []
            kubikaza = []
            Tip = []
            Konja = []
            Pogon = []
            Emisija = []
            BrojVrata = []
            cijena = []
            mjenjac = []
            response = requests.get(auto[i])
            soup = BeautifulSoup(response.text, "html.parser")
            uso = False
            for data in soup.findAll('div', {'class': "op mobile-stanje"}):
                if data.text[31:len(data.text) - 9] != "Korišteno":
                    uso = True
                    i += 1
                    continue
            if uso:
                continue
            nemaTe = False
            for data in soup.findAll('div', {'class': "op pop ispod"}):
                proizvodjac.append(data.text[13:len(data.text) - 2])
                nemaTe = True
            if not nemaTe:
                i += 1
                continue
            nemaTe = False
            for data in soup.findAll('p',
                                     {"style": "font-size:25px;font-weight:500;;background-color:#9dab50;color:#fff;"}):
                cijena.append(data.text[1:len(data.text) - 5])
                nemaTe = True
            if not nemaTe:
                i += 1
                continue
            nemaTe = False
            for data in soup.findAll('div', {'class': "op ispod"}):
                model.append(data.text[8:len(data.text) - 2])
                nemaTe = True
                break
            if not nemaTe:
                i += 1
                continue

            gor = False
            broj = False
            god = False
            kil = False
            kilovat = False
            kubi = False
            tip = False
            konj = False
            pog = False
            ems = False
            mj = False
            for data in soup.findAll('div', {'id': "dodatnapolja1"}):
                for text in data.findAll('div', {'class': "df rp"}):
                    for j in range(len(text.findAll('div', {'class': "df1"}))):
                        if text.findAll('div', {'class': "df1"})[j].text == "Gorivo":
                            Gorivo.append(text.findAll('div', {'class': "df2"})[j].text)
                            gor = True
                        elif text.findAll('div', {'class': "df1"})[j].text == 'Broj vrata':
                            BrojVrata.append(text.findAll('div', {'class': "df2"})[j].text)
                            broj = True
                        elif text.findAll('div', {'class': "df1"})[j].text == 'Godište':
                            Godiste.append(text.findAll('div', {'class': "df2"})[j].text)
                            god = True
                        elif text.findAll('div', {'class': "df1"})[j].text == 'Kilometraža':
                            Kilometara.append(text.findAll('div', {'class': "df2"})[j].text)
                            kil = True
                        elif text.findAll('div', {'class': "df1"})[j].text == 'Kilovata (KW)':
                            Kilovata.append(text.findAll('div', {'class': "df2"})[j].text)
                            kilovat = True
                        elif text.findAll('div', {'class': "df1"})[j].text == 'Kubikaža':
                            kubikaza.append(text.findAll('div', {'class': "df2"})[j].text)
                            kubi = True
                for text in data.findAll('div', {'class': 'df'}):
                    for j in range(len(text.findAll('div', {'class': "df1"}))):
                        if text.findAll('div', {'class': "df1"})[j].text == "Tip":
                            Tip.append(text.findAll('div', {'class': "df2"})[j].text)
                            tip = True
                        elif text.findAll('div', {'class': "df1"})[j].text == "Konjskih snaga":
                            Konja.append(text.findAll('div', {'class': "df2"})[j].text)
                            konj = True
                        elif text.findAll('div', {'class': "df1"})[j].text == "Pogon":
                            Pogon.append(text.findAll('div', {'class': "df2"})[j].text)
                            pog = True
                        elif text.findAll('div', {'class': "df1"})[j].text == "Emisioni standard":
                            Emisija.append(text.findAll('div', {'class': "df2"})[j].text)
                            ems = True
                        elif text.findAll('div', {'class': "df1"})[j].text == "Transmisija":
                            mjenjac.append(text.findAll('div', {'class': "df2"})[j].text)
                            mj = True
            if not tip:
                Tip.append("NULL")
            if not konj:
                Konja.append("NULL")
            if not gor:
                Gorivo.append("NULL")
            if not god:
                Godiste.append("NULL")
            if not broj:
                BrojVrata.append("NULL")
            if not kil:
                Kilometara.append("NULL")
            if not kilovat:
                Kilovata.append("NULL")
            if not kubi:
                kubikaza.append("NULL")
            if not pog:
                Pogon.append("NULL")
            if not ems:
                Emisija.append("NULL")
            if not mj:
                mjenjac.append("NULL")
            if i % 100 == 0:
                print(link + ": " + str(i))
            i += 1
            lista = [proizvodjac, model, Godiste, Kilometara, Gorivo, Kilovata,
                     kubikaza, Tip, Konja, Pogon, Emisija, BrojVrata, mjenjac, cijena]
            labele = {
                'Proizvodjac': lista[0],
                'Model': lista[1],
                'Godiste': lista[2],
                'Kilometara': lista[3],
                'Gorivo': lista[4],
                'Kilovata': lista[5],
                'Kubikaza': lista[6],
                'Tip': lista[7],
                'Konja': lista[8],
                'Pogon': lista[9],
                'Emisija': lista[10],
                'BrojVrata': lista[11],
                'Mjenjac': lista[12],
                'Cijena': lista[13]
            }
            df = pd.DataFrame(labele, columns=['Proizvodjac', 'Model', 'Godiste', 'Kilometara', 'Gorivo', 'Kilovata',
                                               'Kubikaza', 'Tip', 'Konja', 'Pogon', 'Emisija', 'BrojVrata', 'Mjenjac',
                                               'Cijena'])
            if i == 0:
                df.to_csv(r"C:\Users\Admir\Django\procjena\vrijednost\Scrapeani.csv" + link + ".csv", mode='a', index=False, header=True)
            else:
                df.to_csv(r"C:\Users\Admir\Django\procjena\vrijednost\Scrapeani.csv", mode='a', index=False, header=False)

