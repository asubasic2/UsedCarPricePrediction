import React, { Component } from 'react';
import {BrowserRouter ,Route,Switch} from 'react-router-dom';
import HomePage from './components/HomePage/HomePage';
import './App.css';

const opis1="Naš tim web programera će dovesti vašu stranicu od koncepta do stvarnosti. Naše iskustvo u ovom poslu ćemo iskoristiti kako bi odgovorili na sve Vaše zahtjeve. Od početne ideje mi ćemo biti s Vama na svakom koraku i pomoći u razvoju dizajna i implementaciji web stranice prema Vašoj želji. U svakom trenutku ćemo se prilagoditi vašim željama, a konačnim proizvodom ćete sigurno biti zadovoljni. Vaša stranica će izgledati sjajno i biti će prilagođena današnjem turističkom tržištu. Savremena stranica je vjerovatno prvi i najvažniji korak do klijenata, a uz naše usluge će vaš prvi korak biti bez greške. Osim toga, imamo iskustva u integraciji web stranica s raznim drugim tehnologijama uključujući i našu bazu podataka koja pruža personalizirana rješenja koja ce zadovoljiti sve vaše potrebe. U svakom slučaju, desetine zadovoljnih klijenata daju nam za pravo da garantujemo da ćete našim uslugama izrade i održavanja web stranice biti zadovoljni.";
const opis2="Rezervacijski sistemi koje razvija naš tim imaju veliki značaj za poslovanje jer se ujedno pojavljuju i kao sistemi online baza podataka koji turističkim firmama omogućuju bolje upravljanje kapacitetima. Tehnologije koje koristimo u našem sistemu primjenjuju se za različite poslovne funkcije, komunikacije, pružanje usluge gostu i za same goste. Hotelsko poslovanje, sa svim svojim specifičnostima, zahtijeva maksimalnu ažurnost podataka. Naš sistem nudi mogućnosti rezervacije putem web stranice. U ovom trenutku najveći broj Vaših klijenata želi što brže i što jednostavnije rezervisati vaše kapacitete, a uz naš rezervacijski sistem to ćete sasvim sigurno i dobiti i tako ići u korak s vremenom. Nakon izrade sistema rezervacije nudimo i mogućnost održavanja sistema što uključuje ispravku bugova, unapređenje sistema i dodavanja eventualno novih funkcionalnosti. U veoma kratkom roku ćemo reagovati na sve vaše zahtjeve i sve eventualne pritužbe blagovremeno riješiti.";
const opis3="Sistem upravljanja je alat koji unapređuje i olakšava poslovanje firmi, kroz efikasnije upravljanje uposlenicima i procesima unutar firme. Isplativost uvođenja našeg sistema je velika i rezultuje značajno bržem ostvarenju poslovnih ciljeva, kroz efikasniju upotrebu resursa, povećanju ukupne produktivnosti i pouzdanosti, razvoju kompetencija uposlenih i smanjenje broja grešaka. Akcenat je na samom sistemu koji se implementira i koji doprinosi unapređenju poslovanja, a softverska podrška često olakšava implementaciju i kontinualno sprovođenje sistema. U skladu sa Vašim željama, sistem za upravljanje uposlenicima možemo prilagođavati, vodeći računa o funkcionalnosti sistema koja ne smije doći u pitanje. Sistem će prije svega biti pouzdan i pomoći će Vama u svakodnevnom poslovanju i upravljanju svim procesima unutar firme. Zahvaljujući našem sistemu svim vašim poslovnim ciljevima ćete biti barem jedan korak bliže.";
const opis4="Naše softversko rješenje namijenjeno je cjelovitom upravljanju poslovanjem hotelskih objekata. Jednostavno je za korištenje i lahko prilagodljivo različitim kategorijama, veličinama i potrebama hotela. Omogućava upravljanje poslovanjem malih, obiteljskih hotela, ali jednako tako i zahtjevnih velikih hotelskih poduzeća koja imaju potrebu za istovremenim vođenjem više odvojenih smještajnih objekata. Sve specifičnosti Vašeg hotela (lokacija, smještajni kapaciteti, kategorija, i dr.) uzet ćemo u obzir i sistem prilagoditi Vašim željama. Garantujemo Vam da će korištenje našeg sistema biti više nego jednostavno, a sasvim sigurno produktivno kada je u pitanju poslovanje Vašeg hotela. Kroz održavanje sistema, podržavamo kontinuirani razvoj istog i mogućnost uključivanja i isključivanja različitih modula po želji klijenta. U praksi, stojimo Vam na raspolaganju u svakom trenutku da u kratkom vremenskom roku izvršimo promjene na sistemu kako bi korištenje istog bilo što je moguće pouzdanije i produktivnije.";

const Home = () => (
  <HomePage  />
);

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
        
          <Route exact path="/" component={Home} />

        </Switch>
      </BrowserRouter>
    );
  }
}

export default App;