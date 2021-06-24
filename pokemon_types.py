import os

# Static class for pokemon types, so I dont have to grab this data constantly
class PokemonTypes():
    def __init__(self):
        # Initiate all types that I care about
        self.types = ["bug", "dark","dragon","electric","fairy","fighting","fire","flying","ghost","grass","ground","ice","normal","poison","psychic","rock","steel", "water"]
        # List comprehension to check which files we have pictures for
        tempFilePath = [x for x in self.types if os.path.isfile(os.path.join(os.getcwd(), "type", x + ".png"))]
        self.filePaths = {}
        # Convert the list to a dictionary with the file paths
        for thisFile in tempFilePath:
            self.filePaths[thisFile] = os.path.join(os.getcwd(), "type", thisFile + ".png")
    

    # Check if we have the type we are searching for from the static class, and if we do, then return the file path.
    def GetFilePathForType(self, *pokemonType):
        for thisType in pokemonType:
            if not thisType in self.types:
                return None
            for thisFile in self.filePaths:
                if thisFile == thisType:
                    return self.filePaths[thisFile]

        

AllPokemonTypes = PokemonTypes()
        