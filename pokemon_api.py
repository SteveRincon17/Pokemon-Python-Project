import csv
import os
import re
import pokemon as pk

Root = os.getcwd()
PokemonDataset = os.path.join(Root, "datasets\\pokemon_stats\\pokemon.csv")
LowerBounds = {
    "hp": 1,
    "attack": 5,
    "defense": 5 ,
    "sp_attack": 10,
    "sp_defense": 20,
    "speed": 5,
}
UpperBounds = {
    "hp": 255,
    "attack": 190,
    "defense": 230,
    "sp_attack": 194,
    "sp_defense": 230,
    "speed": 180,
}
# I got this from stack overflow to convert rgb to hex because matplotlib uses hex values
def rgb_to_hex(rgb_color):
    #0 rgb(1, 1, 1)
    #1 "(1, 1, 1)"
    #2 "1,1,1"
    rgb_color = re.search('\(.*\)', rgb_color).group(0).replace(' ', '').lstrip('(').rstrip(')')
    [r, g, b] = [int(x) for x in rgb_color.split(',')] # [1, 1, 1]
    # check if in range 0~255
    assert 0 <= r <= 255
    assert 0 <= g <= 255
    assert 0 <= b <= 255
 
    r = hex(r).lstrip('0x')
    g = hex(g).lstrip('0x')
    b = hex(b).lstrip('0x')
    # re-write '7' to '07'
    r = (2 - len(r)) * '0' + r
    g = (2 - len(g)) * '0' + g
    b = (2 - len(b)) * '0' + b
 
    hex_color = '#' + r + g + b
    return hex_color

def FindPokemonByName(name, data = None):
    if data is None:
        data = ImportAndConstructPokemon()
    name = name.lower()
    return data[name] if name in data else None

def FindAllPokemonByType(types, data = None):
    if data is None:
        data = ImportAndConstructPokemon()
    types = [types] if not isinstance(types, list) else types
 
    PokemonByType = []
    for pokemon in data:
        ThisPokemon = data[pokemon]
        if ThisPokemon.type1 in types or ThisPokemon.type2 in types:
            PokemonByType.append(ThisPokemon)

    return PokemonByType


def ImportAndConstructPokemon():
    with open(PokemonDataset) as ExcelFile:
        CsvReader = csv.reader(ExcelFile)
        Pokemen = {}
        try:
            for row in CsvReader:
                ThisPokemon = pk.Pokemon(row)
                if not ThisPokemon.name in Pokemen:
                    Pokemen[ThisPokemon.name] = ThisPokemon
        except csv.Error as e:
            print(e)

        return Pokemen
pokemonData = ImportAndConstructPokemon()
def GetStatWeight(statType, amount):
    if statType in UpperBounds:
        return amount / UpperBounds[statType]

def GetColorOfStatWeight(statType, amount, hex = False):
    r, g = 1, 0
    weight = GetStatWeight(statType, amount)
    color = r - weight, g + weight, 0, 1
    hexString = ""
    if hex:
        hexString += f"rgb({int(color[0]*255)},{int(color[1]*255)},{int(color[2]*255)})"
        # hexString = rgb_to_hex(hexString)
    return color if not hex else rgb_to_hex(hexString)

def GetPictureForPokemon(pokemon):
    files = [f for f in os.listdir("datasets\\pokemon_photos") if os.path.isfile(os.path.join("datasets\\pokemon_photos", f))]
    if isinstance(pokemon, pk.Pokemon):
        for thisFile in files:
            if pokemon.name.lower() in thisFile:
                return os.path.join(os.getcwd(), "datasets\\pokemon_photos", thisFile)

def GetPictureForType(pokemonType):
    files = [f for f in os.listdir("datasets\\pokemon_types") if os.path.isfile(os.path.join("datasets\\pokemon_photos", f))]
    for thisFile in files:
        if pokemonType.lower() in thisFile:
            return os.path.join(os.getcwd(), "datasets\\pokemon_types", thisFile)

testPokemon = FindPokemonByName("Charizard")
# print(GetColorOfStatWeight("hp", 50, hex = True))
