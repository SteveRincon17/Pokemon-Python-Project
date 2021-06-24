import matplotlib.pyplot as plt
import pokemon_api as pokeapi
import pandas as pd

boundsData = { "Upper": pokeapi.UpperBounds, "Lower": pokeapi.LowerBounds }
pokemonData = pokeapi.pokemonData
testPokemon = "Charizard"
thisPokemon = pokeapi.FindPokemonByName(testPokemon)


def GetGraphDataForPokemon(pokemon):
    data = [["attack", "defense", "hp", "speed", "sp_attack", "sp_defense"], [pokemon.attack, pokemon.defense, pokemon.hp, pokemon.speed, pokemon.sp_attack, pokemon.sp_defense], []]
    for i in range(len(data[0])):
        statType = data[0][i]
        thisStat = data[1][i]
        data[2].append(pokeapi.GetColorOfStatWeight(statType, thisStat, hex = True))
    dataFrame = pd.DataFrame({"stat": data[0], "value": data[1]})
    return [dataFrame, data]

def DrawPlotFromData(dataFrame, pokemon, **plotArgs):
    # print(plotArgs)
    dataFrame.plot(**plotArgs)
    plt.title(pokemon.name)
    plt.xlim(right = 255)
    plt.xticks(range(0, 255, 25))
    plt.ylabel('Stat')
    plt.xlabel('Value') 
    plt.show()








