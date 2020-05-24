text = "Lista zakupów" '\n'
lista_zakupów = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"],
    "cukiernia": ["rogalik", "beza", "sernik"]
}
n=0

for key, values in lista_zakupów.items():
    text += f"Idę do {key.title()}, kupuję tam: {values}. \n"
    n = n + len(values)

text += f"W sumię kupuję {n} produktów, gdyz wstąpiłam do cukierni. \n"


text += "Cięzko jest to ogarnąć, ale walczę dzielnie! Pozdrowienia :)"
print(text)