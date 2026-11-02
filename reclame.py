from algemene_functies import mijn_functie_2
def aanbieding_1(smaak,prijs,korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

def inkomsten_totaal(inkomsten,btw):
    totaal = sum(inkomsten)
    bedrag = float(totaal * btw)
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer

def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    uitvoer = [laag,hoog]
    return uitvoer

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    gemiddelde = totaal / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return uitvoer

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer