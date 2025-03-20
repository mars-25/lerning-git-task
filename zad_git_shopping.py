shopping = {
    'warzywniak': ['marchewka', 'pietruszka'],
    'miesny': ['kielbasa', 'pasztet', 'szynka'],
    'zoologiczny': ['python', 'myszy', 'motyle'],
}

licznik = 0
for sklep, produkty in shopping.items():
    print(f"Idę do {sklep.title()} i kupuję tem:")
    for produkt in produkty:
        print(f"\t{produkt.title()}")
        licznik +=1

print(f"\nW sumie kupuję {licznik} produktów.")
#komentarz
print("Zmiana poprzez dodanie komentarza aby wrzucić commita.")
#kolejna zmiana 
print("Kolejna zmiana.")