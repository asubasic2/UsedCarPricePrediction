import pandas as pd
from sklearn.ensemble import RandomForestRegressor


class Prediktor(object):

    def __init__(self, csv):
        self.__df = pd.read_csv(csv, names=['Proizvodjac', 'Model', 'Godiste', 'Kilometara', 'Gorivo', 'Kubikaza',
                                          'BrojVrata', 'Cijena', 'Kilovata', 'Tip', 'Pogon', 'Mjenjac', 'Emisija'],  encoding='utf-8')
        self.__pripremiDataset()
        self.__KodirajUBrojeve()
        self.__model = RandomForestRegressor(max_depth=25, random_state=0, n_estimators=100)
        self.__X = self.__df[['Proizvodjac', 'Model', 'Godiste', 'Kilometara', 'Kubikaza', 'Kilovata', 'Gorivo',
                              'BrojVrata', 'Tip', 'Pogon', 'Mjenjac', 'Emisija']]
        self.__y = self.__df['Cijena']
        self.__model.fit(self.__X, self.__y)
        self.__izracunajPadZaKilometar()

    def __pripremiDataset(self):
        # Izbaci cijene koje su veće od 160000
        self.__df = self.__df[self.__df.Cijena < 160000]
        # Izbaci razmake
        self.__df.Pogon = self.__df.Pogon.str.replace(' S', 'S')
        self.__df.Pogon = self.__df.Pogon.str.replace(' Z', 'Z')
        self.__df.Emisija = self.__df.Emisija.str.replace(' E', 'E')
        # Izbaci elektro i plon/benzin automobile (nema ih dovoljno)
        self.__df = self.__df[self.__df.Gorivo != "Elektro"]
        self.__df = self.__df[self.__df.Gorivo != "Plin/Benzin"]
        # Izbaci premale i prevelike kubikaže
        self.__df = self.__df[self.__df.Kubikaza <= 5]
        self.__df = self.__df[self.__df.Kubikaza >= 1]
        # Izbaci kilovate veće od 300
        self.__df = self.__df[self.__df.Kilovata <= 300]

    # Pomoćna funkcija koja kodira vrijednosti
    def __nesto(self, lista, x):
        listaNova = []
        for i in range(len(lista)):
            listaNova.append((lista[i], i))

        for i in range(len(listaNova)):
            if listaNova[i][0] == x:
                x = listaNova[i][1]

        return x

    # Pomoćna funkcija koja vraća vrijednost i njen odgovarajući preslikani broj
    def __preslikaj(self, lista):
        listaNova = []
        for i in range(len(lista)):
            listaNova.append((lista[i], i))

        return listaNova

    # Kodira kolone zapisane u stringu u obliku broja (jednostavno kodiranje rednim brojem)
    def __KodirajUBrojeve(self):
        Proizvodjac = self.__df.Proizvodjac.unique()
        Model = self.__df.Model.unique()
        Gorivo = self.__df.Gorivo.unique()
        BrojVrata = self.__df.BrojVrata.unique()
        Tip = self.__df.Tip.unique()
        Pogon = self.__df.Pogon.unique()
        Mjenjac = self.__df.Mjenjac.unique()
        Emisija = self.__df.Emisija.unique()

        self.__df['Gorivo'] = self.__df['Gorivo'].apply(lambda x: self.__nesto(Gorivo, x))
        self.__df['Emisija'] = self.__df['Emisija'].apply(lambda x: self.__nesto(Emisija, x))
        self.__df['Mjenjac'] = self.__df['Mjenjac'].apply(lambda x: self.__nesto(Mjenjac, x))
        self.__df['Model'] = self.__df['Model'].apply(lambda x: self.__nesto(Model, x))
        self.__df['Proizvodjac'] = self.__df['Proizvodjac'].apply(lambda x: self.__nesto(Proizvodjac, x))
        self.__df['Tip'] = self.__df['Tip'].apply(lambda x: self.__nesto(Tip, x))
        self.__df['Pogon'] = self.__df['Pogon'].apply(lambda x: self.__nesto(Pogon, x))
        self.__df['BrojVrata'] = self.__df['BrojVrata'].apply(lambda x: self.__nesto(BrojVrata, x))

        self.__gorivoPreslikano = self.__preslikaj(Gorivo)
        self.__standardPreslikano = self.__preslikaj(Emisija)
        self.__mjenjacPreslikano = self.__preslikaj(Mjenjac)
        self.__modelPreslikano = self.__preslikaj(Model)
        self.__brendPreslikano = self.__preslikaj(Proizvodjac)
        self.__tipPreslikano = self.__preslikaj(Tip)
        self.__pogonPreslikano = self.__preslikaj(Pogon)
        self.__vrataPreslikano = self.__preslikaj(BrojVrata)
        df6 = self.__df[(self.__df.Kilometara > 0) & (self.__df.Cijena < 130000) != False]
        df7 = self.__df[(self.__df.Kilometara <= 0) & (self.__df.Cijena >= 0) != False]
        self.__df = pd.concat([df6, df7], axis=0, join='outer', ignore_index=False, keys=None,
                            levels=None, names=None, verify_integrity=False, copy=True)

    # Računa procentualno koliko će vozilo izgubiti na vrijednosti za svakih 60000 kilometara
    def __izracunajPadZaKilometar(self):
        i = 0
        j = 60000
        cijena2 = []
        tmp = []
        while j <= 360000:
            test = self.__df.loc[self.__df['Kilometara'] < j]
            test = test.loc[test['Kilometara'] > i]
            test2 = self.__df.loc[self.__df['Kilometara'] < j + 60000]
            test2 = test2.loc[test2['Kilometara'] > i + 60000]
            cijena2.append(abs((test2['Cijena'].mean() / test['Cijena'].mean()) - 1))
            tmp.append(test['Cijena'].mean())
            i += 60000
            j += 60000

        cijena3 = [0]

        l = 0
        k = 0
        while k < len(cijena2):
            cijena3.append(cijena2[k] / 3)
            k += 1

        self.__cijena4 = [(20000, 0)]
        k = 0
        while k < len(cijena3):
            if 2 <= k < 3:
                cijena3[k] += cijena3[1] - 0.06
                self.__cijena4.append((80000, cijena3[k]))
            elif 3 <= k < 4:
                cijena3[k] += cijena3[2] - 0.05
                self.__cijena4.append((140000, cijena3[k]))
            elif 4 <= k < 5:
                cijena3[k] += cijena3[3] - 0.06
                self.__cijena4.append((200000, cijena3[k]))
            elif 5 <= k < 6:
                cijena3[k] += cijena3[4] - 0.04
                self.__cijena4.append((280000, cijena3[k]))
            elif k >= 6:
                cijena3[k] += cijena3[5]
                self.__cijena4.append((320000, cijena3[k]))
            k += 1

    # Skida sa osnovne cijene po pređenom kilometru
    def __kazniKilometre(self, cijena, procjena, kilometraza):
        temp = 0.
        for i in range(len(procjena)):
            if i == 0:
                if kilometraza < procjena[i + 1][0]:
                    temp = cijena - procjena[i][1] * cijena
                    break
            elif i == (len(procjena) - 1):
                temp = cijena - procjena[len(procjena) - 1][1] * cijena
            if kilometraza < procjena[i][0]:
                temp = cijena - procjena[i][1] * cijena
                break

        return temp

    # Pomoćna za public funkciju Predvidi
    def __pomocna(self, lista1, auto, k):
        temp = lista1[0][1]
        for i in range(len(lista1)):
            if lista1[i][0] == auto[k]:
                temp = lista1[i][1]
                break
        return temp

    # Vraća procijenjenu vrijednost automobila
    def Predvidi(self, auto):
        lista = [self.__brendPreslikano, self.__modelPreslikano, [], [], [], [], self.__gorivoPreslikano, self.__vrataPreslikano,
                 self.__tipPreslikano, self.__pogonPreslikano, self.__mjenjacPreslikano, self.__standardPreslikano]

        pred = []
        for i in range(len(lista)):
            if 2 <= i < 6:
                pred.append(auto[i])
            else:
                pred.append(self.__pomocna(lista[i], auto, i))

        #return self.__kazniKilometre(self.__model.predict([pred])[0], self.__cijena4, auto[3])
        return self.__model.predict([pred])[0]

    def PredvidiMin(self, auto):
        lista = [self.__brendPreslikano, self.__modelPreslikano, []]
        x = self.__df[['Proizvodjac', 'Model', 'Godiste']]
        y = self.__df['Cijena']
        pred = []
        for i in range(len(lista)):
            if i == 2:
                pred.append(auto[i])
                break
            pred.append(self.__pomocna(lista[i], auto, i))
        model = RandomForestRegressor(max_depth=25, random_state=0, n_estimators=100)
        model.fit(x, y)
        return model.predict([pred])[0]
