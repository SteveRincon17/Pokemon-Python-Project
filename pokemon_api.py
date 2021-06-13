import csv
import os

Root = os.getcwd()
DatasetPath = os.path.join(Root, "datasets")
PokemonDataset = os.path.join(DatasetPath, "pokemon.csv")

def ImportAndConstructPokemon():
    with open(PokemonDataset) as ExcelFile:
        CsvReader = csv.reader(ExcelFile)
        Pokemen = {}
        try:
            for row in CsvReader:
                ThisPokemon = row
                if not row[29] in Pokemen:
                    Pokemen[row[29]] = ThisPokemon
        except csv.Error as e:
            print(e)

        return Pokemen
    
print (ImportAndConstructPokemon())