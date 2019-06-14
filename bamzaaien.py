# Bamzaaien voor 2 personen. Beide personen krijgen 3 lucifers. Het doel van het spel is totale aantal lucifers te raden dat in het spel is. Elke speler kan 0-3 lucifers selecteren. Om beurten raden de spelers hoeveel er totaal in het spel zijn. Spelers moeten niet laten zien hoeveel lucifers ze in hun hand hebben. De winnende speler behoud zijn/haar lucifers, de verliezende speler verliest 1 lucifer.Het spel gaat door tot dat 1 speler al zijn lucifers kwijt is, die speler verliest het spel.

def speel_bamzaaien():
    lucifers_speler_1 = 3
    lucifers_speler_2 = 3

    while lucifers_speler_1 != 0 and lucifers_speler_2 != 0:
        winnaar = speel_ronde(lucifers_speler_1, lucifers_speler_2)
        if winnaar == 1:
            lucifers_speler_1 = lucifers_speler_1 - 1
        elif winnaar == 2:
            lucifers_speler_2 = lucifers_speler_2 - 1


    if lucifers_speler_1 == 0:
        print("Speler 1 heeft het spel gewonnen!")
    else:
        print("Speler 2 heeft gewonnen!")


def speel_ronde(lucifers_speler_1, lucifers_speler_2):
    aantal_gepakte_lucifers_1 = int(input("Speler 1 mag nu een aantal lucifers aangeven om in te zetten:"))

    while aantal_gepakte_lucifers_1 > lucifers_speler_1:
        aantal_gepakte_lucifers_1 = int(input("Uw aantal lucifers is teveel, kies een juist aantal:"))

    aantal_gepakte_lucifers_2 = int(input("Speler 2 mag nu een aantal lucifers aangeven om in te zetten:"))

    while aantal_gepakte_lucifers_2 > lucifers_speler_2:
        aantal_gepakte_lucifers_2 = int(input("Uw aantal lucifers is teveel, kies een juist aantal:"))

    totaal_aantal_lucifers = aantal_gepakte_lucifers_1 + aantal_gepakte_lucifers_2

    lucifers_in_spel_1 = int(input("Speler 1 mag nu het aantal lucifers in het spel geven:"))
    lucifers_in_spel_2 = int(input("Speler 2 mag nu het aantal lucifers in het spel geven:"))
    while lucifers_in_spel_2 == lucifers_in_spel_1:
        lucifers_in_spel_2 = int(input("Uw gekozen aantal lucifers is hetzelfde als dat van speler 1, kies een ander getal:"))

    if lucifers_in_spel_1 == totaal_aantal_lucifers:
        print("Speler 1 heeft gewonnen!")
        print("")
        return 1

    elif lucifers_in_spel_2 == totaal_aantal_lucifers:
        print("Speler 2 heeft gewonnen!")
        print("")
        return 2

    else:
        print("Niemand heeft deze ronde gewonnen!")
        print("")
        return 0

speel_bamzaaien()