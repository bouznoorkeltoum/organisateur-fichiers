from pathlib import Path 

dossier = Path(".")

for element in dossier.iterdir():
    print(element)
    