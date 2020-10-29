# Zad 1 i 2
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Piotr"
nazwisko = "Sternik"
litera_1 = imie[2]
litera_2 = nazwisko[3]
liczba_liter_1 = tekst.count(litera_1)
liczba_liter_2 = tekst.count(litera_2)
print(f"W tekście jest {liczba_liter_1} liter i oraz {liczba_liter_2} liter e.")
# Zad 3
print('{:>7}'.format(imie))
print('{:.50}'.format(tekst))
print('{:15.7}'.format(tekst))
print('{:03.02f}'.format(7.519013532))
print('{:^7}'.format(nazwisko))
# Zad 4
print(dir(imie))
help(imie.strip)
# Zad 5
print(f"{nazwisko[::-1]} {imie[::-1]}")
# Zad 6
lista1 = list(range(1, 11))
print(lista1)
lista2 = lista1[5:]
for i in range(5):
    lista1.pop()
print(f"Lista1 {lista1}")
print(f"Lista2 {lista2}")
# Zad 7
lista1 = lista1 + lista2
lista1.insert(0, 0)
print(lista1)
# Zad 8
krotka = (153120, "Jan", "Nowak", 147431, "Ania", "Kowalska")
lista_studentow = list(krotka)
print(lista_studentow)
# Zad 9
#slownik = dict(lista_studentow)
#print(slownik.values())
# Zad 10
lista_nr_telefonow = set([501249188, 502321449, 501249188, 503771992, 501249188])
print(lista_nr_telefonow)
# Zad 11
for i in range(1, 11):
    print(i)
print("---------------")
# Zad 12
for i in range(100, 15, -5):
    print(i)
# Zad 13
slownik1 = {1: "Mam", 2: "na", 3: "imie", 4: "Piotr"}
slownik2 = {1: "Mieszkam", 2: "w", 3: "Olsztynie"}
lista3 = list(slownik1)
lista4 = list(slownik2)
lista5 = lista3 + lista4
print(lista5)
