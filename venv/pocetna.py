import queries.queries as queries
import funkcionalnosti

print("Dobro dosli! Unesite Vas email i clanski broj ako ste clan/username i password ukoliko ste zaposleni.")
while True:
    username = input("Vas email/username je: ")
    password = input("Vas clanski broj/password je: ")
    clan = queries.login(username, password)
    bibliotekar = queries.log_bibliotekar(username, password)
    menadzer = queries.log_menadzer(username, password)
    if clan is not None:
        print("Uspesno ste se ulogovali pod imenom ", clan.imeClana, ".")
        break
    if bibliotekar is not None:
        print("Uspesno ste se ulogovali, ", bibliotekar.usernameBibliotekara, ".")
        break
    if menadzer is not None:
        print("Uspesno ste se ulogovali, ", menadzer.usernameMenadzera, ".")
        break

while True:
    if clan is not None:
        funkcionalnosti.pocetna_clan()
        id_clana = clan.idClana
        n = int(input())
        while n == 1:
            print("Lista dostupnih knjiga:")
            funkcionalnosti.lista_knjiga()
            break
        while n == 2:
            zanr = input("Upisite vrstu zanra za koji zelite da izlistate knjige ("
                         "drama/komedija/publicistika/istorijski roman/realizam): ")
            funkcionalnosti.lista_knjiga_zanr(zanr)
            break
        while n == 3:
            izdavac = input("Upisite vrstu izdavaca za kojeg zelite da izlistate knjige (Laguna/Vulkan/Evro Giunti): ")
            funkcionalnosti.lista_knjiga_izdavac(izdavac)
            break
        while n == 4:
            pismo = input("Upisite vrstu pisma za koje zelite da izlistate knjige (cirilica/latinica): ")
            funkcionalnosti.lista_knjiga_pismo(pismo)
            break
        while n == 5:
            funkcionalnosti.spisak_zaduzenja(id_clana)
            break
        while n == 6:
            funkcionalnosti.broj_izdavanja()
            break
        while n == 7:
            funkcionalnosti.broj_primeraka()
            break
    elif bibliotekar is not None:
        funkcionalnosti.pocetna_bibliotekar()
        n = int(input())
        while n == 1:
            print("Lista dostupnih knjiga:")
            funkcionalnosti.lista_knjiga()
            break
        while n == 2:
            zanr = input("Upisite vrstu zanra za koji zelite da izlistate knjige ("
                         "drama/komedija/publicistika/istorijski roman/realizam): ")
            funkcionalnosti.lista_knjiga_zanr(zanr)
            break
        while n == 3:
            izdavac = input("Upisite vrstu izdavaca za kojeg zelite da izlistate knjige (Laguna/Vulkan/Evro Giunti): ")
            funkcionalnosti.lista_knjiga_izdavac(izdavac)
            break
        while n == 4:
            pismo = input("Upisite vrstu pisma za koje zelite da izlistate knjige (cirilica/latinica): ")
            funkcionalnosti.lista_knjiga_pismo(pismo)
            break
        while n == 7:
            funkcionalnosti.broj_primeraka_izdavanja()
            break
        while n == 8:
            print("Upisite podatke za dodavanje novog clana:")
            clanski_broj_clana = input("Clanski broj: ")
            email_clana = input("Email: ")
            ime_clana = input("Ime clana: ")
            prezime_clana = input("Prezime clana: ")
            adresa_clana = input("Adresa clana: ")
            datum_rodjenja_clana = input("Datum rodjenja clana: ")
            datum_uclanjenja_clana = input("Datum uclanjenja clana: ")
            queries.dodaj_clana(clanski_broj_clana, email_clana, ime_clana, prezime_clana, adresa_clana,
                                datum_rodjenja_clana, datum_uclanjenja_clana)
            break
        while n == 9:
            print("Upisite podatke za dodavanje nove knjige:")
            naziv_nove_knjige = input("Naziv knjige: ")
            autor_knjige = input("Autor knjige: ")
            izdavac_knjige = input("Izdavac: ")
            godina_izdanja_knjige = input("Godina izdanja: ")
            zanr_knjige = input("Zanr: ")
            vrsta_poveza_knjige = input("Vrsta poveza(tvrd/mek): ")
            broj_strana_knjige = input("Broj strana: ")
            pismo_knjige = input("Pismo(cirilica/latinica): ")
            broj_primeraka_knjige = input("Broj primeraka: ")
            broj_izdavanja_knjige = input("Broj izdavanja: ")
            queries.dodaj_knjigu(naziv_nove_knjige, autor_knjige, izdavac_knjige, godina_izdanja_knjige, zanr_knjige,
                                 vrsta_poveza_knjige, broj_strana_knjige, pismo_knjige, broj_primeraka_knjige,
                                 broj_izdavanja_knjige)
            break
        while n == 10:
            print("Upisite podatke za dodavanje novog zaduzenja:")
            datum_zaduzenja = input("Datum zaduzenja: ")
            datum_vracanja = input("Datum do kada treba da se vrati: ")
            id_clanaz = input("Id clana: ")
            inventarni_broj_knjige = input("Inventarni broj knjige: ")
            queries.dodaj_zaduzenje(datum_zaduzenja, datum_vracanja, id_clanaz, inventarni_broj_knjige)
            break
        while n == 11:
            clan_za_brisanje = input("Upisite clanski broj clana kojeg zelite da obrisete: ")
            queries.obrisi_clana(clan_za_brisanje)
            break
        while n == 12:
            knjiga_za_brisanje = input("Upisite naziv knjige koju zelite da obrisete: ")
            queries.obrisi_knjigu(knjiga_za_brisanje)
            break
        while n == 13:
            zaduzenje_za_brisanje = input("Upisite id zaduzenja koje zelite da obrisete: ")
            queries.obrisi_zaduzenje(zaduzenje_za_brisanje)
            break
        while n == 16:
            print("Spisak clanova biblioteke:")
            funkcionalnosti.lista_clanova()
            break
        while n == 17:
            print("Spisak zaduzenja clanova biblioteke:")
            funkcionalnosti.lista_zaduzenja()
            break
    else:
        funkcionalnosti.pocetna_menadzer()
        n = int(input())
        while n == 1:
            print("Lista dostupnih knjiga:")
            funkcionalnosti.lista_knjiga()
            break
        while n == 2:
            zanr = input("Upisite vrstu zanra za koji zelite da izlistate knjige ("
                         "drama/komedija/publicistika/istorijski roman/realizam): ")
            funkcionalnosti.lista_knjiga_zanr(zanr)
            break
        while n == 3:
            izdavac = input("Upisite vrstu izdavaca za koji zelite da izlistate knjige (Laguna/Vulkan/Evro Giunti): ")
            funkcionalnosti.lista_knjiga_izdavac(izdavac)
            break
        while n == 4:
            pismo = input("Upisite vrstu pisma za koji zelite da izlistate knjige (cirilica/latinica): ")
            funkcionalnosti.lista_knjiga_pismo(pismo)
            break
        while n == 7:
            funkcionalnosti.broj_primeraka_izdavanja()
            break
        while n == 8:
            print("Upisite podatke za dodavanje novog clana:")
            clanski_broj_clana = input("Clanski broj: ")
            email_clana = input("Email: ")
            ime_clana = input("Ime clana: ")
            prezime_clana = input("Prezime clana: ")
            adresa_clana = input("Adresa clana: ")
            datum_rodjenja_clana = input("Datum rodjenja clana: ")
            datum_uclanjenja_clana = input("Datum uclanjenja clana: ")
            queries.dodaj_clana(clanski_broj_clana, email_clana, ime_clana, prezime_clana, adresa_clana,
                                datum_rodjenja_clana, datum_uclanjenja_clana)
            break
        while n == 9:
            print("Upisite podatke za dodavanje nove knjige:")
            naziv_nove_knjige = input("Naziv knjige: ")
            autor_knjige = input("Autor knjige: ")
            izdavac_knjige = input("Izdavac: ")
            godina_izdanja_knjige = input("Godina izdanja: ")
            zanr_knjige = input("Zanr: ")
            vrsta_poveza_knjige = input("Vrsta poveza(tvrd/mek): ")
            broj_strana_knjige = input("Broj strana: ")
            pismo_knjige = input("Pismo(cirilica/latinica): ")
            broj_primeraka_knjige = input("Broj primeraka: ")
            broj_izdavanja_knjige = input("Broj izdavanja: ")
            queries.dodaj_knjigu(naziv_nove_knjige, autor_knjige, izdavac_knjige, godina_izdanja_knjige, zanr_knjige,
                                 vrsta_poveza_knjige, broj_strana_knjige, pismo_knjige, broj_primeraka_knjige,
                                 broj_izdavanja_knjige)
            break
        while n == 10:
            print("Upisite podatke za dodavanje novog zaduzenja:")
            datum_zaduzenja = input("Datum zaduzenja: ")
            datum_vracanja = input("Datum do kada treba da se vrati: ")
            id_clanaz = input("Id clana: ")
            inventarni_broj_knjige = input("Inventarni broj knjige: ")
            queries.dodaj_zaduzenje(datum_zaduzenja, datum_vracanja, id_clanaz, inventarni_broj_knjige)
            break
        while n == 11:
            clan_za_brisanje = input("Upisite clanski broj clana kojeg zelite da obrisete: ")
            queries.obrisi_clana(clan_za_brisanje)
            break
        while n == 12:
            knjiga_za_brisanje = input("Upisite naziv knjige koju zelite da obrisete: ")
            queries.obrisi_knjigu(knjiga_za_brisanje)
            break
        while n == 13:
            zaduzenje_za_brisanje = input("Upisite id zaduzenja koje zelite da obrisete: ")
            queries.obrisi_zaduzenje(zaduzenje_za_brisanje)
            break
        while n == 14:
            print("Upisite podatke za dodavanje novog bibliotekara:")
            username_bibliotekara = input("Korisnicko ime bibliotekara: ")
            password_bibliotekara = input("Sifra bibliotekara: ")
            ime_bibliotekara = input("Ime bibliotekara: ")
            prezime_bibliotekara = input("Prezime bibliotekara: ")
            queries.dodaj_bibliotekara(username_bibliotekara, password_bibliotekara, ime_bibliotekara,
                                       prezime_bibliotekara)
            break
        while n == 15:
            bibliotekar_za_brisanje_ime = input("Upisite ime bibliotekara kojeg zelite da obrisete: ")
            bibliotekar_za_brisanje_prezime = input("Upisite prezime bibliotekara kojeg zelite da obrisete: ")
            queries.obrisi_bibliotekara(bibliotekar_za_brisanje_ime, bibliotekar_za_brisanje_prezime)
            break
        while n == 16:
            print("Spisak uclanjenih u biblioteku:")
            funkcionalnosti.lista_clanova()
            break
        while n == 17:
            print("Spisak zaduzenja clanova biblioteke:")
            funkcionalnosti.lista_zaduzenja()
            break
        while n == 18:
            print("Spisak trenutno zaposlenih bibliotekara:")
            funkcionalnosti.lista_bibliotekara()
            break
