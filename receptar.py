import os.path
import os

def nacti_recept(jmeno):
    """
    Když této funkci dáš jméno textového souboru ze složky recepty,
    tak vrátí text receptu jako řetězec.
    """
    tenhle_script = __file__
    adresar_projektu = os.path.dirname(tenhle_script)
    adresar_receptu = os.path.join(adresar_projektu, 'recepty')
    cesta_k_receptu = os.path.join(adresar_receptu, jmeno)
    with open(cesta_k_receptu, 'r', encoding='utf-8') as f:
        return f.read()

def projdi_recept(ingredience,jmeno):
    """
    Když této funkci dáš ingredienci, projde recepty, jestli v nich někde je
    """
    tenhle_script = __file__
    adresar_projektu = os.path.dirname(tenhle_script)
    adresar_receptu = os.path.join(adresar_projektu, 'recepty')
    cesta_k_receptu = os.path.join(adresar_receptu, jmeno)

    ingredience = ingredience.lower()
    with open(cesta_k_receptu, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        if ingredience in text:
            print("V receptu {} je ingredience {}".format(jmeno,ingredience))
            return True
        else:
            return False

print(nacti_recept('titulek.txt'))

NAZVY_RECEPTU = os.listdir('recepty')

for recept in NAZVY_RECEPTU:
    if "titulek.txt" not in recept:
        print(nacti_recept(recept))

ingredience = input("Zadej nazev ingredience: ")

for recept in NAZVY_RECEPTU:
    projdi_recept(ingredience,recept)
