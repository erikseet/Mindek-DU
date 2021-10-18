def cislo():
    while True:
        cislo = input("Zadaj počet slov: ")
        try:
            return int(cislo)
        except ValueError:
            print("Nebolo zadané správne číslo")

cislo = cislo()
input = []
pocet = 0

with open('basnicka.txt', encoding='utf-8') as subor:
    for slovo in subor:
        input += slovo.split()

for i in range(cislo):
    pocet += 1
    if pocet == len(input):
        pocet -= len(input)
    with open(f"""slovo{i}""", mode="w", encoding="utf-8") as subor:
        print(input[pocet - 1], file=subor)

