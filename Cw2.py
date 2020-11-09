#Zad1
text = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz " \
       "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków " \
       "później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. " \
       "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty " \
       "Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji " \
       "druków na komputerach osobistych, jak Aldus PageMaker"

#Zad2
name = "Kornel"
Sname = "Stanulewicz"
letter_1 = name[2]
letter_2 = Sname[3]
number_letters_1 = text.count(letter_1)
number_letters_2 = text.count(letter_2)
print(f"W tekście jest {number_letters_1} liter o oraz {number_letters_2} liter a.")

#Zad3
print('{} {:.4}'.format(name, Sname))
print('{:10.3} {}'.format(text, name))
print('{} {:^20} {}'.format(name, Sname, "II"))
print('{:f}'.format(number_letters_1))
print('{} {:.10} {} {:02.02f} {}'.format('w tekście', text, 'jest', number_letters_2, 'liter a'))

#Zad4
print(dir(name))
help(name.swapcase)

#Zad5
print(f"{name[::-1]} {Sname[::-1]}")

#Zad6
list_1 = list(range(1, 11))
list_2 = list_1[5:]
for i in range(5):
    list_1.pop()
print("List_1", list_1)
print("List_2", list_2)

#Zad7
list_1 = list_1 + list_2
list_1.insert(0, 0)
print(list_1)

#Zad8
student_list = [(142465, "Kornel", "Stanulewicz"), (102137, "Janusz", "Zielony")]
print(student_list)

#Zad9
dict_student = {
    "1Student": {
        "Index" : student_list[0][0],
        "Name" : student_list[0][1],
        "Second Name" : student_list[0][2],
        "Age" : 23,
        "Email" : "kornel@gmail.com",
        "Year of birth" : 1997,
        "Address" : "Klebark",
    },
    "2Student": {
        "Index" : student_list[1][0],
        "Name" : student_list[1][1],
        "Second Name" : student_list[1][2],
        "Age" : 22,
        "Email" : "niekornel@gmail.com",
        "Year of birth" : 1998,
        "Address" : "Olsztyn",
    }
}
print(dict_student)

#Zad10
tel_list = set([111111111, 111111111, 111222111, 111222333, 111222111])
print(tel_list)

#Zad11
for i in range(1, 11):
    print(i)
print("")

#Zad12
for i in range(100, 15, -5):
    print(i)

#Połącz całą wiedzę wydobytą z zajęć (i zadań) i stwórz program
# wypisujący dane z listy, która zawiera kilka słowników (dane wypisz w postaci jednego string'a odpowiednio go formatując).

#Zad13
dict_1 = {
    "Nice": {
        "Index" : 12,
        "Name" : "Jurek",
        "Second Name" : "Karolak",
    }
}
dict_2 = {
    "Great": {
        "Index" : 14,
        "Name" : "Ala",
        "Second Name" : "Jeziorak",
    }
}


list_3 = list(dict_1.values())
list_4 = list(dict_2.values())
list_5 = list_3 + list_4
print(list_5)