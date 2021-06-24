import pokemon_api as pokeapi

class Pokemon:
    def __init__(self, payload):
        self.abilities = payload[0]
        self.against_coefficients = {
            "bug": float(payload[1]),
            "dark": float(payload[2]),
            "dragon": float(payload[3]),
            "electric": float(payload[4]),
            "fairy": float(payload[5]),
            "fighting": float(payload[6]),
            "fire": float(payload[7]),
            "flying": float(payload[8]),
            "ghost": float(payload[9]),
            "grass": float(payload[10]),
            "ground": float(payload[11]),
            "ice": float(payload[12]),
            "normal": float(payload[13]),
            "poison": float(payload[14]),
            "psychic": float(payload[15]),
            "rock": float(payload[16]),
            "steel": float(payload[17]),
            "water": float(payload[18])
        }
        self.attack = float(payload[19])
        self.base_egg_steps = float(payload[20])
        self.base_happiness = float(payload[21])
        self.base_total = float(payload[22])
        self.capture_rate = float(payload[23])
        self.classfication = payload[24]
        self.defense = float(payload[25])
        self.experience_growth = float(payload[26])
        self.height_m = float(payload[27])
        self.hp = float(payload[28])
        self.name = payload[29].lower()
        self.percentage_male = float(payload[30])
        self.pokedex_number = float(payload[31])
        self.sp_attack = float(payload[32])
        self.sp_defense = float(payload[33])
        self.speed = float(payload[34])
        self.type1 = payload[35]
        self.type2 = payload[36]
        self.weight_kg = float(payload[37])
        self.generation = payload[38]
        self.is_legendary = payload[39]
    def IsWeakAgainst(self, pokemon_type):
        # print("Weak: ", pokemon_type, self.against_coefficients[pokemon_type] if pokemon_type in self.against_coefficients else False)
        if not pokemon_type in self.against_coefficients or isinstance(self.against_coefficients[pokemon_type], str):
            return False
        return self.against_coefficients[pokemon_type] > 1 or False
    def IsWeakerThan(self, pokemon):
        Weaker = 0
        AttributeCount = 0
        if pokemon.type1 is not None and pokemon.type1 in self.against_coefficients:
            AttributeCount += 1
            Weaker += self.against_coefficients[pokemon.type1]
        if pokemon.type2 is not None and pokemon.type2 in self.against_coefficients:
            AttributeCount += 1
            Weaker += self.against_coefficients[pokemon.type2]
        return Weaker / AttributeCount > 1

    def IsStrongAgainst(self, pokemon_type):
        # print("Strong: ", pokemon_type, self.against_coefficients[pokemon_type] if pokemon_type in self.against_coefficients else False)
        if not pokemon_type in self.against_coefficients or isinstance(self.against_coefficients[pokemon_type], str):
            return False
        return self.against_coefficients[pokemon_type] < 1 or False
    
    def IsStrongerThan(self, pokemon):
        Stronger = 0
        AttributeCount = 0
        if pokemon.type1 is not None and pokemon.type1 in self.against_coefficients:
            AttributeCount += 1
            Stronger += self.against_coefficients[pokemon.type1]
        if pokemon.type2 is not None and pokemon.type2 in self.against_coefficients:
            AttributeCount += 1
            Stronger += self.against_coefficients[pokemon.type2]
        return Stronger / AttributeCount < 1


    def IsNeutralAgainst(self, pokemon_type):
        # print("Neutral: ", pokemon_type, self.against_coefficients[pokemon_type] if pokemon_type in self.against_coefficients else False)
        if not pokemon_type in self.against_coefficients or isinstance(self.against_coefficients[pokemon_type], str):
            return False
        return self.against_coefficients[pokemon_type] == 1.0 or self.against_coefficients[pokemon_type] == 1 or False

    def IsNeutralTo(self, pokemon):
        Neutral = 0
        AttributeCount = 0
        if pokemon.type1 is not None and pokemon.type1 in self.against_coefficients:
            AttributeCount += 1
            Neutral += self.against_coefficients[pokemon.type1]
        if pokemon.type2 is not None and pokemon.type2 in self.against_coefficients:
            AttributeCount += 1
            Neutral += self.against_coefficients[pokemon.type2]
        return Neutral / AttributeCount == 1

    def WeakerToTypes(self):
        return [x for x in self.against_coefficients if self.against_coefficients[x] > 1]

    def StrongToTypes(self):
        return [x for x in self.against_coefficients if self.against_coefficients[x] < 1]

    def GetPicture(self):
        self.picture = pokeapi.GetPictureForPokemon(self)
        return self.picture




