import copy
import pandas as pd
import re


class OcistiPodatke(object):

    def __init__(self, csv):
        df = pd.read_csv(csv, dtype={'Cijena': str, 'Godiste': str},
                         names=['Proizvodjac', 'Model', 'Godiste', 'Kilometara', 'Gorivo', 'Kilovata',
                                'Kubikaza', 'Tip', 'Konja', 'Pogon', 'Emisija', 'BrojVrata', 'Mjenjac', 'Cijena'],
                         encoding='utf-8')
        self.df2 = df.dropna(
            subset=['Godiste', 'Kilometara', 'Proizvodjac', 'Model', 'Gorivo', 'Kubikaza', 'BrojVrata'])
        self.df2 = self.__koloneUString()
        self.df2 = self.__ocistiKilometreModelGodisteCijenu()

    def __only_numerics(self, seq):
        numeric_string = re.sub("[^0-9]", "", seq)
        return numeric_string

    def __sracunajKilovate(self, konji):
        return int(float(konji) * 0.745699872)

    def __most_frequent(self, List):
        if len(List) == 0:
            return "Nema"
        counter = 0
        num = List[0]

        for i in List:
            curr_frequency = List.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                num = i

        return num

    def __koloneUString(self):
        self.df2['Godiste'] = self.df2['Godiste'].astype(str)
        self.df2['Kilovata'] = self.df2['Kilovata'].astype(str)
        self.df2['Kubikaza'] = self.df2['Kubikaza'].astype(str)
        self.df2['Emisija'] = self.df2['Emisija'].astype(str)
        self.df2['Tip'] = self.df2['Tip'].astype(str)
        self.df2['Pogon'] = self.df2['Pogon'].astype(str)
        self.df2['Mjenjac'] = self.df2['Mjenjac'].astype(str)
        self.df2['Konja'] = self.df2['Konja'].astype(str)
        return self.df2

    def __ocistiKilometreModelGodisteCijenu(self):
        self.df2['Cijena'] = self.df2['Cijena'].apply(lambda x: x.replace('.', '')).apply(
            lambda x: x.replace(',', '.')).astype(
            float)
        self.df2 = self.df2[self.df2.Kilometara < 400000]
        self.df2 = self.df2[self.df2.Kilometara > 0.0]
        self.df2 = self.df2[self.df2.Model != "Drugi"]
        r = re.compile(r'^[0-9]+$')
        filter = self.df2['Godiste'].apply(lambda x: bool(r.match(x)))
        self.df2 = self.df2[filter]
        self.df2['Godiste'] = self.df2['Godiste'].astype(int)
        self.df2 = self.df2[self.df2.Godiste >= 2000]
        return self.df2

    def __ocistiKilovate(self):
        konji = self.df2.iloc[:, 8].values
        kilovati = self.df2.iloc[:, 5].values
        kubika = self.df2.iloc[:, 6].values
        jedinstveni = self.df2["Kubikaza"].unique()

        for i in range(len(kilovati)):
            if kilovati[i] != "nan":
                kilovati[i] = self.__only_numerics(kilovati[i])
                if len(kilovati[i]) == 0:
                    kilovati[i] = "nan"
                if kilovati[i] != "nan":
                    if int(kilovati[i]) < 40 or int(kilovati[i]) > 400:
                        kilovati[i] = "nan"

        for i in range(len(konji)):
            if konji[i] != "nan":
                konji[i] = self.__only_numerics(konji[i])
                if len(konji[i]) == 0:
                    konji[i] == "nan"

        for i in range(len(kilovati)):
            if kilovati[i] == "nan" and konji[i] != 'nan' and konji[i] != "":
                kilovati[i] = str(self.__sracunajKilovate(konji[i]))

        prosjecno = []
        for i in range(len(jedinstveni)):
            broj = 0
            temp = 0
            for j in range(len(kubika)):
                if jedinstveni[i] == kubika[j]:
                    if kilovati[j] != "nan":
                        broj += 1
                        temp += float(kilovati[j])
            if broj != 0:
                prosjecno.append(int(temp / broj))
            else:
                prosjecno.append(0)

        for i in range(len(jedinstveni)):
            for j in range(len(kilovati)):
                if kilovati[j] == "nan":
                    if jedinstveni[i] == kubika[j]:
                        kilovati[j] = str(prosjecno[i])

        for i in range(len(kilovati)):
            if int(kilovati[i]) < 40 or int(kilovati[i]) > 500:
                kilovati[i] = "nan"

        self.df2 = self.df2.drop(columns=['Kilovata', 'Konja'])
        self.df2['Kilovata'] = kilovati
        self.df2 = self.df2[self.df2.Kilovata.apply(lambda x: x.isnumeric())]
        self.df2['Kilovata'] = self.df2['Kilovata'].astype(int)

    def __ocistiModelTipIPogon(self):
        model = self.df2.iloc[:, 1].values
        tip = self.df2.iloc[:, 6].values
        pogon = self.df2.iloc[:, 7].values
        mjenjac = self.df2.iloc[:, 10].values
        modeli = self.df2["Model"].unique()

        for i in range(len(modeli)):
            maxTip = []
            maxPogon = []
            maxMjenjac = []
            for j in range(len(model)):
                if model[j] == modeli[i]:
                    if tip[j] != "nan":
                        maxTip.append(tip[j])
                    if pogon[j] != "nan":
                        maxPogon.append(pogon[j])
                    if mjenjac[j] != "nan":
                        maxMjenjac.append(mjenjac[j])
            for k in range(len(model)):
                if model[k] == modeli[i]:
                    if tip[k] == "nan":
                        tip[k] = self.__most_frequent(maxTip)
                    if pogon[k] == "nan":
                        pogon[k] = self.__most_frequent(maxPogon)
                    if mjenjac[k] == "nan":
                        mjenjac[k] = self.__most_frequent(maxMjenjac)

        self.df2 = self.df2.drop(columns=['Tip', 'Pogon', 'Mjenjac'])
        self.df2['Tip'] = tip
        self.df2['Pogon'] = pogon
        self.df2['Mjenjac'] = mjenjac
        self.df2 = self.df2[self.df2.Tip != "Nema"]
        self.df2 = self.df2[self.df2.Pogon != "Nema"]
        self.df2 = self.df2[self.df2.Mjenjac != "Nema"]

    def __ocistiEmisiju(self):
        godiste = self.df2.iloc[:, 2].values
        emisija = self.df2.iloc[:, 6].values

        for i in range(len(emisija)):
            if emisija[i] == "nan":
                if int(godiste[i]) < 2004:
                    emisija[i] = "Euro 3"
                if 2004 <= int(godiste[i]) < 2007:
                    emisija[i] = "Euro 4"
                if 2007 <= int(godiste[i]) < 2012:
                    emisija[i] = "Euro 5"
                if int(godiste[i]) >= 2012:
                    emisija[i] = "Euro 6"

        self.df2 = self.df2.drop(columns=['Emisija'])
        self.df2['Emisija'] = emisija

    def __ocistiCijenuIKilometre(self):
        self.df2 = self.df2[self.df2.Cijena > 3000]
        df6 = self.df2[(self.df2.Godiste < 2017) & (self.df2.Kilometara > 40000) != False]
        df7 = self.df2[(self.df2.Godiste >= 2017) & (self.df2.Kilometara >= 0) != False]
        self.df2 = pd.concat([df6, df7], axis=0, join='outer', ignore_index=False, keys=None,
                             levels=None, names=None, verify_integrity=False, copy=True)
        df8 = self.df2[(self.df2.Godiste < 2006) & (self.df2.Kilometara > 120000) != False]
        df9 = self.df2[(self.df2.Godiste >= 2006) & (self.df2.Kilometara >= 0) != False]
        self.df2 = pd.concat([df8, df9], axis=0, join='outer', ignore_index=False, keys=None,
                             levels=None, names=None, verify_integrity=False, copy=True)

    def __ocistiGodisteSaCijenom(self):
        df6 = self.df2[(self.df2.Godiste < 2006) & (self.df2.Cijena < 20000) != False]
        df7 = self.df2[(self.df2.Godiste >= 2006) & (self.df2.Cijena >= 0) != False]
        self.df2 = pd.concat([df6, df7], axis=0, join='outer', ignore_index=False, keys=None,
                             levels=None, names=None, verify_integrity=False, copy=True)
        df6 = self.df2[(self.df2.Godiste < 2010) & (self.df2.Cijena < 60000) != False]
        df7 = self.df2[(self.df2.Godiste >= 2010) & (self.df2.Cijena >= 0) != False]
        self.df2 = pd.concat([df6, df7], axis=0, join='outer', ignore_index=False, keys=None,
                             levels=None, names=None, verify_integrity=False, copy=True)
        df6 = self.df2[(self.df2.Godiste < 2013) & (self.df2.Cijena < 100000) != False]
        df7 = self.df2[(self.df2.Godiste >= 2013) & (self.df2.Cijena >= 0) != False]
        self.df2 = pd.concat([df6, df7], axis=0, join='outer', ignore_index=False, keys=None,
                             levels=None, names=None, verify_integrity=False, copy=True)
        df6 = self.df2[(self.df2.Godiste < 2016) & (self.df2.Cijena < 110000) != False]
        df7 = self.df2[(self.df2.Godiste >= 2016) & (self.df2.Cijena >= 0) != False]
        self.df2 = pd.concat([df6, df7], axis=0, join='outer', ignore_index=False, keys=None,
                             levels=None, names=None, verify_integrity=False, copy=True)
        df6 = self.df2[(self.df2.Godiste < 2017) & (self.df2.Cijena < 160000) != False]
        df7 = self.df2[(self.df2.Godiste >= 2017) & (self.df2.Cijena >= 0) != False]
        self.df2 = pd.concat([df6, df7], axis=0, join='outer', ignore_index=False, keys=None,
                             levels=None, names=None, verify_integrity=False, copy=True)
        df6 = self.df2[(self.df2.Godiste > 2015) & (self.df2.Cijena > 18000) != False]
        df7 = self.df2[(self.df2.Godiste <= 2015) & (self.df2.Cijena >= 0) != False]
        self.df2 = pd.concat([df6, df7], axis=0, join='outer', ignore_index=False, keys=None,
                             levels=None, names=None, verify_integrity=False, copy=True)

    def ocistiCsv(self):
        self.__ocistiKilovate()
        self.__ocistiModelTipIPogon()
        self.__ocistiEmisiju()
        self.__ocistiCijenuIKilometre()
        self.__ocistiGodisteSaCijenom()
        print(self.df2.head())

    def spremiUCsv(self):
        self.df2.to_csv(r"C:\Users\Admir\Django\procjena\vrijednost\Automobili.csv", mode='a', index=False, header=False)

    def spremiUXls(self):
        self.df2.to_excel("Automobili.xlsx", index=False, header=False)
