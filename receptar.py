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

print(nacti_recept('titulek.txt'))

NAZVY_RECEPTU = os.listdir('recepty')

for recept in NAZVY_RECEPTU:
    print(nacti_recept(recept))
