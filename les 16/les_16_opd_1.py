def get_integer(a):
    while True:
        try:
            gebruiker_invoer = input(a)
            integer = int(gebruiker_invoer)
            return integer
        except ValueError:
            print("ongeldig integer")

integer_invoer = get_integer("voer een integer in ")

print(f"je hebt {integer_invoer} ingevoerd ")
    
def get_float(b):
    while True:
        try:
            Gebruiker_invoer = input(b)
            Float = float(Gebruiker_invoer)
            return Float
        except ValueError:
            print("ongeldig float")

float_invoer = get_float("voer een float in ")

print(f"je hebt {float_invoer} ingevoerd ")

def get_string(c):
    while True:
        try:
            Gebruiker_Invoer = input(c)
            string = str(Gebruiker_Invoer)
            return string
        except ValueError:
            print("ongeldig string")

string_invoer = get_string("voer een string in ")

print(f"je hebt {string_invoer} ingevoerd ")

def get_letter(d):
    GEbruiker_invoer = input(d).lower()
    letter = (GEbruiker_invoer)
    if GEbruiker_invoer in ("a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,"):
        return letter.capitalize()
    
    else:
        print("dit zit niet in het alfabet")

letter = get_letter("voer hier een letter in ")
print(f"deze letter heb je ingevoerd: {letter} ")