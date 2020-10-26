import queries.queries as queries
import matplotlib.pyplot as plt
import numpy as np


def pocetna_clan():
    print("Odaberite funkcionalnost koju biste zeleli:")
    print("1) Ukoliko zelite da izlistate sve knjige.")
    print("2) Ukoliko zelite da izlistate knjige odredjenog zanra.")
    print("3) Ukoliko zelite da izlistate knjige odredjenog izdavaca.")
    print("4) Ukoliko zelite da izlistate knjige odredjene vrste pisma")
    print("5) Ukoliko zelite da izlistate spisak knjiga koje ste zaduzili.")
    print("6) Ukoliko zelite da vidite graf knjiga sa brojem dosadasnjih izdavanja.")
    print("7) Ukoliko zelite da vidite graf knjiga sa trenutnim brojem slobodnih primeraka.")


def pocetna_bibliotekar():
    print("Odaberite funkcionalnost koju biste zeleli:")
    print("1) Ukoliko zelite da izlistate sve knjige.")
    print("2) Ukoliko zelite da izlistate knjige odredjenog zanra.")
    print("3) Ukoliko zelite da izlistate knjige odredjenog izdavaca.")
    print("4) Ukoliko zelite da izlistate knjige odredjene vrste pisma")
    print("7) Ukoliko zelite da vidite graf broja primeraka i broja izdavanja knjiga.")
    print("8) Ukoliko zelite da dodate novog clana.")
    print("9) Ukoliko zelite da dodate novu knjigu.")
    print("10) Ukoliko zelite da dodate novo zaduzenje.")
    print("11) Ukoliko zelite da izbrisete postojeceg clana.")
    print("12) Ukoliko zelite da izbrisete postojecu knjigu.")
    print("13) Ukoliko zelite da izbrisete postojece zaduzenje.")
    print("16) Ukoliko zelite da izlistate sve clanove.")
    print("17) Ukoliko zelite da izlistate sva zaduzenja clanova.")


def pocetna_menadzer():
    print("Odaberite funkcionalnost koju biste zeleli:")
    print("1) Ukoliko zelite da izlistate sve knjige.")
    print("2) Ukoliko zelite da izlistate knjige odredjenog zanra.")
    print("3) Ukoliko zelite da izlistate knjige odredjenog izdavaca.")
    print("4) Ukoliko zelite da izlistate knjige odredjene vrste pisma.")
    print("7) Ukoliko zelite da vidite graf broja primeraka i broja izdavanja knjiga.")
    print("8) Ukoliko zelite da dodate novog clana.")
    print("9) Ukoliko zelite da dodate novu knjigu.")
    print("10) Ukoliko zelite da dodate novo zaduzenje.")
    print("11) Ukoliko zelite da izbrisete postojeceg clana.")
    print("12) Ukoliko zelite da izbrisete postojecu knjigu.")
    print("13) Ukoliko zelite da izbrisete postojece zaduzenje.")
    print("14) Ukoliko zelite da dodate novog bibliotekara.")
    print("15) Ukoliko zelite da izbrisete postojeceg bibliotekara.")
    print("16) Ukoliko zelite da izlistate sve clanove.")
    print("17) Ukoliko zelite da izlistate sva zaduzenja clanova.")
    print("18) Ukoliko zelite da izlistate sve bibliotekare.")


def lista_knjiga():
    knjige = queries.get_knjige()
    j = 1
    for i in knjige:
        print(j, ") Knjiga: ", i.nazivKnjige, ", autor Knjige: ", i.autorKnjige, ", izdavac: ", i.izdavac,
              ", godina izdanja: ", i.godinaIzdanja, ", zanr: ", i.zanr, ", vrsta pisma: ", i.pismo)
        j = j + 1


def lista_clanova():
    clanovi = queries.get_clanovi()
    j = 1
    for i in clanovi:
        print(j, ") Clanski broj clana: ", i.clanskiBroj, ", email: ", i.email, ", ime clana: ", i.imeClana,
              ", prezime clana: ", i.prezimeClana, ", adresa clana: ", i.adresaClana,
              ", datum rodjenja clana: ", i.datumRodjenja, " datum uclanjenja clana: ", i.datumUclanjenja)
        j = j + 1


def lista_bibliotekara():
    bibliotekari = queries.get_bibliotekari()
    j = 1
    for i in bibliotekari:
        print(j, ") Bibliotekar: ", i.imeBibliotekara, "", i.prezimeBibliotekara)
        j = j + 1


def lista_zaduzenja():
    zaduzenja = queries.get_sva_zaduzenja()
    j = 1
    for i in zaduzenja:
        print(j, ") Zaduzenje: ", i.idZaduzenja, ", datum zaduzivanja: ", i.datumZaduzenja,
              ", datum do kada je potrebno vratiti knjigu: ", i.datumVracanja, ", id clana: ", i.idClana,
              ", inventarni broj knjige: ", i.invBroj)
        j = j + 1


def lista_knjiga_zanr(zanr):
    knjige_zanr = queries.get_knjige_zanr(zanr)
    if len(knjige_zanr) == 0:
        print("Ne postoje knjige tog zanra. Pokusajte ponovo uneti naziv zanra.")
        return
    j = 1
    for i in knjige_zanr:
        print(j, ") Knjiga: ", i.nazivKnjige, ", autor Knjige: ", i.autorKnjige, ", izdavac: ", i.izdavac,
              ", godina izdanja: ", i.godinaIzdanja, ", zanr: ", i.zanr, ", vrsta pisma: ", i.pismo)
        j = j + 1


def lista_knjiga_izdavac(izdavac):
    knjige_izdavac = queries.get_knjige_izdavac(izdavac)
    if len(knjige_izdavac) == 0:
        print("Ne postoje knjige tog izdavaca. Pokusajte ponovo uneti naziv izdavaca.")
        return
    j = 1
    for i in knjige_izdavac:
        print(j, ") Knjiga: ", i.nazivKnjige, ", autor Knjige: ", i.autorKnjige, ", izdavac: ", i.izdavac,
              ", godina izdanja: ", i.godinaIzdanja, ", zanr: ", i.zanr, ", vrsta pisma: ", i.pismo)
        j = j + 1


def lista_knjiga_pismo(pismo):
    knjige_pismo = queries.get_knjige_pismo(pismo)
    if len(knjige_pismo) == 0:
        print("Ne postoje knjige te vrste pisma. Pokusajte ponovo uneti naziv pisma.")
        return
    j = 1
    for i in knjige_pismo:
        print(j, ") Knjiga: ", i.nazivKnjige, ", autor Knjige: ", i.autorKnjige, ", izdavac: ", i.izdavac,
              ", godina izdanja: ", i.godinaIzdanja, ", zanr: ", i.zanr, ", vrsta pisma: ", i.pismo)
        j = j + 1


def spisak_zaduzenja(id_clana):
    knjige_zaduzenja = queries.get_knjige_zaduzenja(id_clana)
    j = 1
    for i in knjige_zaduzenja:
        print(j, ") Knjiga: ", i.nazivKnjige, ", autor Knjige: ", i.autorKnjige, ", izdavac: ", i.izdavac,
              ", godina izdanja: ", i.godinaIzdanja, ", zanr: ", i.zanr, ", vrsta pisma: ", i.pismo)
        j = j + 1


def broj_izdavanja():
    knjige = queries.get_knjige()
    knjiga_br_izdavanja = []
    knjiga_naziv = []
    j = 1
    for i in knjige:
        knjiga_br_izdavanja.append(i.brojIzdavanja)
        knjiga_naziv.append(i.nazivKnjige)
        print(j, ") Knjiga: ", i.nazivKnjige, ", broj izdavanja: ", i.brojIzdavanja)
        j = j + 1
    plt.bar(knjiga_naziv, knjiga_br_izdavanja)
    plt.xlabel('Knjige')
    plt.xticks(rotation=90)
    plt.ylabel('Broj izdavanja')
    plt.show()


def broj_primeraka():
    knjige = queries.get_knjige()
    knjiga_br_primeraka = []
    knjiga_naziv = []
    j = 1
    for i in knjige:
        knjiga_br_primeraka.append(i.brojPrimeraka)
        knjiga_naziv.append(i.nazivKnjige)
        print(j, ") Knjiga: ", i.nazivKnjige, ", broj primeraka: ", i.brojPrimeraka)
        j = j + 1
    plt.bar(knjiga_naziv, knjiga_br_primeraka)
    plt.xlabel('Knjige')
    plt.xticks(rotation=90)
    plt.ylabel('Broj primeraka')
    plt.show()


def brojevi():
    plt.plot(range(10))
    plt.show()


def broj_primeraka_izdavanja():
    knjige = queries.get_knjige()
    knjiga_br_primeraka = []
    knjiga_br_izdavanja = []
    knjiga_naziv = []
    knjiga_id = []
    j = 1
    for i in knjige:
        knjiga_br_primeraka.append(i.brojPrimeraka)
        knjiga_br_izdavanja.append(i.brojIzdavanja)
        knjiga_naziv.append(i.nazivKnjige)
        knjiga_id.append(i.idKnjige)
        print(j, ") Knjiga: ", i.nazivKnjige, ", broj primeraka: ", i.brojPrimeraka, ", broj izdavanja : "
              , i.brojIzdavanja)
        j = j + 1
    x = np.arange(len(knjiga_naziv))
    width = 0.30
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, knjiga_br_primeraka, width, label='Broj primeraka')
    rects2 = ax.bar(x + width / 2, knjiga_br_izdavanja, width, label='Broj izdavanja')
    ax.set_ylabel('Broj primeraka i izdavanja')
    ax.set_title('Broj primeraka i izdavanja po knjigama')
    ax.set_xticks(x)
    ax.set_xticklabels(knjiga_id)
    ax.legend()
    plt.show()

