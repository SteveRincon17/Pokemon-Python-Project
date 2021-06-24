import pokemon_api as pokeapi
import pokemon as pk
from pokemon_types import AllPokemonTypes
from graphs import GetGraphDataForPokemon, DrawPlotFromData
from PIL import Image
commands = ["pokemon"]
def PrintMenuOptions():
    print("Please select from the following options: ")
    print("[0] Pokemon")

if __name__ == "__main__":
    # Initialize the pokemon data
    PokemonData = pokeapi.ImportAndConstructPokemon()
    if PokemonData: # if PokemonData is not None and pokemonData is not False
        # Get input from user
        PrintMenuOptions()
        mode = None
        userInput = int(input("Please make a selection: "))
        if userInput < 3 and userInput >= 0:
            mode = commands[userInput]
        while mode is None:
            userInput = int(input("Please make another selection: "))
            if userInput < 3 and userInput >= 0:
                mode = commands[userInput]
        
        if userInput == 0:
            PokemonInput = input("Choose a pokemon: ")
            MyPokemon = pokeapi.FindPokemonByName(PokemonInput)
            while MyPokemon is None:
                PokemonInput = input("Please choose another pokemon: ")
                MyPokemon = pokeapi.FindPokemonByName(PokemonInput)

            data = {
                "Name": MyPokemon.name.capitalize(), 
                "Types": [MyPokemon.type1, MyPokemon.type2],  
                "Stats": [
                    # Cast floats to integers to remove rounding, then to string to format later
                    "hp", int(MyPokemon.hp), str(int(pokeapi.GetStatWeight("hp", MyPokemon.hp) * 100)), 
                    "atk", int(MyPokemon.attack), str(int(pokeapi.GetStatWeight("attack", MyPokemon.attack) * 100)), 
                    "def", int(MyPokemon.defense), str(int(pokeapi.GetStatWeight("defense", MyPokemon.defense) * 100)), 
                    "s_atk", int(MyPokemon.sp_attack), str(int(pokeapi.GetStatWeight("sp_attack", MyPokemon.sp_attack) * 100)), 
                    "s_def", int(MyPokemon.sp_defense), str(int(pokeapi.GetStatWeight("sp_defense", MyPokemon.sp_defense) * 100)), 
                    "spd", int(MyPokemon.speed), str(int(pokeapi.GetStatWeight("speed", MyPokemon.speed) * 100))
                ],
                "Stronger": MyPokemon.StrongToTypes(),
                "Weaker": MyPokemon.WeakerToTypes(),
                "Picture": MyPokemon.GetPicture()
            }
            print("{:-^114}".format(""))
            for key in data:
                # Title Column
                builder = "{0:<10}|".format(key)
                value = data[key]
                if isinstance(value, list):
                    if key != "Stats":
                        for i in range(len(value)):
                            thisItem = str(value[i])
                            builder += "{0:>15} |".format(thisItem)
                    else:
                        # Iterate in steps of 3 because every 0th, 1st and 2nd index are all the same, 0th is the same as 3rd, which is the same as 6th, etc.
                        for i in range(0, len(value) - 1, 3):
                            thisItem = value[i] + ": " + str(value[i + 1]) + " (" + value[i + 2] + "%)"
                            builder += "{0:>15} |".format(thisItem)
                else:
                    if key != "Picture":
                        builder += "{0:>15} |".format(str(value))
                    else:
                        builder += "{0:^66} |".format(str(value))
                        pass
                print(builder)
            print("{:-^114}".format(""))
            # Create the graph for the stats
            graphdata = GetGraphDataForPokemon(MyPokemon)
            DrawPlotFromData(graphdata[0], MyPokemon, kind = "barh", x = "stat", y = "value", color = graphdata[1][2])
            # Uses native image program with operating system, such as the Photos application from windows. (Will take a few seconds to load)
            pokemonImage = Image.open(data["Picture"])
            pokemonImage.show()
        #elif userInput == 1:                
        #else:
   









       
        





