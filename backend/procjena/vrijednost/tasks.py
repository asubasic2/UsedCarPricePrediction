from background_task import background
from background_task.models import Task
import os
from .Scraper import Scraper
from .CiscenjePodataka import OcistiPodatke


@background(schedule=3600*24)
def scrapeaj(repeat=Task.DAILY, repeat_until=None):
    test = "https://www.olx.ba/pretraga?vrsta=samoprodaja&sort_order=desc&kategorija=18&stanje=2&sort_po=datum&sacijenom" \
           "=sacijenom&stranica="  # 90
    s = Scraper(test)
    df = s.URLAutomobilaUcsv(90)
    s.ScrapeajDetalje("Automobili.csv", df)
    o = OcistiPodatke(r'C:\Users\Admir\Django\procjena\vrijednost\Scrapeani.csv')
    o.ocistiCsv()
    o.spremiUCsv()
    os.remove(r'C:\Users\Admir\Django\procjena\vrijednost\Scrapeani.csv')
