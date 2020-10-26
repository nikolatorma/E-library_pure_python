import pymysql

from tables.Bibliotekar import Bibliotekar
from tables.Clan import Clan
from tables.Knjiga import Knjiga
from tables.Menadzer import Menadzer
from tables.Zaduzenje import Zaduzenje

db = pymysql.connect(host="localhost", user="root", password="Garfield9597", db="test")

cursor = db.cursor()


def login(username_clana, password_clana):
    cursor.execute("SELECT * FROM Clan WHERE email =%s AND clasnkiBroj =%s", [username_clana, password_clana])
    korisnik = cursor.fetchone()
    if korisnik is None:
        print("Korisnik nije clan.")
        return
    clan = Clan(korisnik[0], korisnik[1], korisnik[2], korisnik[3], korisnik[4], korisnik[5], korisnik[6], korisnik[7])
    return clan


def log_menadzer(username_menadzera, password_menadzera):
    cursor.execute("SELECT * FROM Menadzer WHERE usernameMenadzera =%s AND passwordMenadzera =%s",
                   [username_menadzera, password_menadzera])
    korisnik = cursor.fetchone()
    if korisnik is None:
        print("Korisnik nije menadzer. Pogresno unet username i/ili password, pokusajte ponovo.")
        return
    menadzer = Menadzer(korisnik[0], korisnik[1], korisnik[2], korisnik[3], korisnik[4])
    return menadzer


def log_bibliotekar(username_bibliotekara, password_bibliotekara):
    cursor.execute("SELECT * FROM Bibliotekar WHERE usernameBibliotekara =%s AND passwordBibliotekara =%s",
                   [username_bibliotekara, password_bibliotekara])
    korisnik = cursor.fetchone()
    if korisnik is None:
        print("Korisnik nije bibliotekar.")
        return
    bibliotekar = Bibliotekar(korisnik[0], korisnik[1], korisnik[2], korisnik[3], korisnik[4])
    return bibliotekar


def dodaj_clana(clanski_broj_clana, email_clana, ime_clana, prezime_clana, adresa_clana,
                datum_rodjenja_clana, datum_uclanjenja_clana):
    sql = ("INSERT INTO Clan (clasnkiBroj, email, imeClana, prezimeClana, adresaClana, datumRodjenja, "
           "datumUclanjenja) VALUES(%s, %s, %s, %s, %s, %s, %s)")
    val = (clanski_broj_clana, email_clana, ime_clana, prezime_clana, adresa_clana,
           datum_rodjenja_clana, datum_uclanjenja_clana)
    cursor.execute(sql, val)
    db.commit()
    print("Clan dodat, ID clana je: ", cursor.lastrowid)


def dodaj_knjigu(naziv_nove_knjige, autor_knjige, izdavac_knjige, godina_izdanja_knjige, zanr_knjige,
                 vrsta_poveza_knjige, broj_strana_knjige, pismo_knjige, broj_primeraka_knjige,
                 broj_izdavanja_knjige):
    sql = ("INSERT INTO Knjiga (nazivKnjige, autorKnjige, izdavac, godinaIzdanja, zanr, vrstaPoveza, brojStrana, pismo,"
           "brojPrimeraka, brojIzdavanja) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    val = (naziv_nove_knjige, autor_knjige, izdavac_knjige, godina_izdanja_knjige, zanr_knjige,
           vrsta_poveza_knjige, broj_strana_knjige, pismo_knjige, broj_primeraka_knjige,
           broj_izdavanja_knjige)
    cursor.execute(sql, val)
    db.commit()
    id_k = cursor.lastrowid
    print("Knjiga je uspesno dodata, ID knjige je: ", id_k)
    for i in range(int(broj_primeraka_knjige)):
        sqlp = "INSERT INTO Primerak (Knjiga_idKnjige) VALUES (%s)"
        valp = id_k
        cursor.execute(sqlp, valp)
        db.commit()
        print("Primerak je uspesno dodat, ID primerka je: ", cursor.lastrowid)


def dodaj_bibliotekara(username_bibliotekara, password_bibliotekara, ime_bibliotekara, prezime_bibliotekara):
    sql = ("INSERT INTO Bibliotekar (usernameBibliotekara, passwordBibliotekara, imeBibliotekara, prezimeBibliotekara)"
           "VALUES(%s, %s, %s, %s)")
    val = (username_bibliotekara, password_bibliotekara, ime_bibliotekara, prezime_bibliotekara)
    cursor.execute(sql, val)
    db.commit()
    print("Bibliotekar je uspesno dodat, ID bibliotekara je: ", cursor.lastrowid)


def obrisi_clana(clan_za_brisanje):
    obrisi_zaduzenje_prilikom_brisanja_clana(clan_za_brisanje)
    sql = "DELETE FROM Clan WHERE clasnkiBroj = %s"
    val = clan_za_brisanje
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, " clan je uspesno izbrisan.")


def obrisi_zaduzenje_prilikom_brisanja_clana(zaduzenje_clana):
    sql = "DELETE z.* FROM Zaduzenje z INNER JOIN Clan c on z.clan_idClana = c.idClana WHERE c.clasnkiBroj = %s"
    val = zaduzenje_clana
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, " zaduzenja je uspesno izbrisano.")


def obrisi_primerak(primerak_za_brisanje):
    cursor.execute("DELETE p.* FROM Primerak p "
                   "INNER JOIN Knjiga k on p.knjiga_idKnjige = k.idKnjige "
                   "WHERE k.nazivKnjige = %s", primerak_za_brisanje)
    db.commit()
    print(cursor.rowcount, " primerka su uspesno izbrisana.")


def obrisi_knjigu(knjiga_za_brisanje):
    primerak_za_brisanje = str(knjiga_za_brisanje)
    obrisi_primerak(primerak_za_brisanje)
    sql = "DELETE FROM Knjiga WHERE nazivKnjige = %s"
    val = knjiga_za_brisanje
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, " knjiga je uspesno izbrisana.")


def obrisi_zaduzenje(zaduzenje_za_brisanje):
    cursor.execute("SELECT * FROM Knjiga k INNER JOIN Primerak p on k.idKnjige = p.knjiga_idKnjige "
                   "INNER JOIN Zaduzenje z on p.invBroj = z.primerak_invBroj WHERE z.idZaduzenja = %s",
                   zaduzenje_za_brisanje)
    knjigaz = cursor.fetchone()
    sqlu = ("UPDATE Knjiga k INNER JOIN Primerak p on k.idKnjige = p.knjiga_idKnjige "
            "INNER JOIN Zaduzenje z on p.invBroj = z.primerak_invBroj SET brojPrimeraka = %s WHERE z.idZaduzenja = %s")
    knjiga = Knjiga(knjigaz[0], knjigaz[1], knjigaz[2], knjigaz[3], knjigaz[4], knjigaz[5], knjigaz[6],
                    knjigaz[7], knjigaz[8], knjigaz[9], knjigaz[10])
    broj_primeraka = knjiga.brojPrimeraka
    broj_primeraka += 1
    valu = (broj_primeraka, zaduzenje_za_brisanje)
    cursor.execute(sqlu, valu)
    db.commit()
    print(cursor.rowcount, " parametar izmenjen.")
    sql = "DELETE FROM Zaduzenje WHERE idZaduzenja = %s"
    val = zaduzenje_za_brisanje
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, " zaduzenje je uspesno izbrisano.")


def obrisi_bibliotekara(bibliotekar_za_brisanje_ime, bibliotekar_za_brisanje_prezime):
    sql = "DELETE FROM Bibliotekar WHERE imeBibliotekara = %s AND prezimeBibliotekara = %s"
    val = (bibliotekar_za_brisanje_ime, bibliotekar_za_brisanje_prezime)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, " bibliotekar je uspesno izbrisan.")


def get_knjige():
    global knjige
    knjige = []
    cursor.execute("SELECT * FROM Knjiga")
    for i in cursor.fetchall():
        knjige.append(Knjiga(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    return knjige


def get_clanovi():
    global clanovi
    clanovi = []
    cursor.execute("SELECT * FROM Clan")
    for i in cursor.fetchall():
        clanovi.append(Clan(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
    return clanovi


def get_bibliotekari():
    global bibliotekari
    bibliotekari = []
    cursor.execute("SELECT * FROM Bibliotekar")
    for i in cursor.fetchall():
        bibliotekari.append(Bibliotekar(i[0], i[1], i[2], i[3], i[4]))
    return bibliotekari


def get_sva_zaduzenja():
    global zaduzenja
    zaduzenja = []
    cursor.execute("SELECT * FROM Zaduzenje")
    for i in cursor.fetchall():
        zaduzenja.append(Zaduzenje(i[0], i[1], i[2], i[3], i[4]))
    return zaduzenja


def get_knjige_zanr(zanr):
    global knjige_zanr
    knjige_zanr = []
    cursor.execute("SELECT * FROM Knjiga WHERE zanr =%s", zanr)
    for i in cursor.fetchall():
        knjige_zanr.append(Knjiga(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    return knjige_zanr


def get_knjige_izdavac(izdavac):
    global knjige_izdavac
    knjige_izdavac = []
    cursor.execute("SELECT * FROM Knjiga WHERE izdavac =%s", izdavac)
    for i in cursor.fetchall():
        knjige_izdavac.append(Knjiga(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    return knjige_izdavac


def get_knjige_pismo(pismo):
    global knjige_pismo
    knjige_pismo = []
    cursor.execute("SELECT * FROM Knjiga WHERE pismo =%s", pismo)
    for i in cursor.fetchall():
        knjige_pismo.append(Knjiga(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    return knjige_pismo


def get_knjige_zaduzenja(id_clana):
    global knjige_zaduzenja
    knjige_zaduzenja = []
    cursor.execute("SELECT * FROM Knjiga k INNER JOIN Primerak p on k.idKnjige = p.knjiga_idKnjige "
                   "INNER JOIN Zaduzenje z on p.invBroj = z.primerak_invBroj "
                   "INNER JOIN Clan c on z.clan_idClana = c.idClana WHERE c.idClana =%s", id_clana)
    for i in cursor.fetchall():
        knjige_zaduzenja.append(Knjiga(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
    return knjige_zaduzenja


def dodaj_zaduzenje(datum_zaduzenja, datum_vracanja, id_clanaz, inventarni_broj_knjige):
    cursor.execute("SELECT * FROM Knjiga k INNER JOIN Primerak p on k.idKnjige = p.knjiga_idKnjige WHERE p.invBroj = %s"
                   , inventarni_broj_knjige)
    knjigai = cursor.fetchone()
    knjiga_inv = Knjiga(knjigai[0], knjigai[1], knjigai[2], knjigai[3], knjigai[4], knjigai[5], knjigai[6],
                        knjigai[7], knjigai[8], knjigai[9], knjigai[10])
    primerak = int(knjiga_inv.brojPrimeraka)
    if primerak > 0:
        sql = ("INSERT INTO Zaduzenje (datumZaduzenja, datumVracanja, Clan_idClana, Primerak_invBroj)"
               "VALUES(%s, %s, %s, %s)")
        val = (datum_zaduzenja, datum_vracanja, id_clanaz, inventarni_broj_knjige)
        cursor.execute(sql, val)
        db.commit()
        print("Zaduzenje je uspesno dodato, ID zaduzenja je: ", cursor.lastrowid)
        id_zaduzenja = cursor.lastrowid
        cursor.execute("SELECT * FROM Knjiga k INNER JOIN Primerak p on k.idKnjige = p.knjiga_idKnjige "
                       "INNER JOIN Zaduzenje z on p.invBroj = z.primerak_invBroj WHERE z.idZaduzenja = %s",
                       id_zaduzenja)
        knjigaz = cursor.fetchone()
        sqlu = ("UPDATE Knjiga k INNER JOIN Primerak p on k.idKnjige = p.knjiga_idKnjige SET brojPrimeraka = %s, "
                "brojIzdavanja = %s "
                "WHERE p.invBroj = %s")
        knjiga = Knjiga(knjigaz[0], knjigaz[1], knjigaz[2], knjigaz[3], knjigaz[4], knjigaz[5], knjigaz[6],
                        knjigaz[7], knjigaz[8], knjigaz[9], knjigaz[10])
        broj_primeraka = knjiga.brojPrimeraka
        broj_izdavanja = knjiga.brojIzdavanja
        broj_primeraka -= 1
        broj_izdavanja += 1
        valu = (broj_primeraka, broj_izdavanja, inventarni_broj_knjige)
        cursor.execute(sqlu, valu)
        db.commit()
        print(cursor.rowcount + 1, " parametra izmenjena.")
    else:
        print("Za odabranu knjigu na zalost nema primeraka na stanju.")
