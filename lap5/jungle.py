class animal:
    def __init__(self, name, kind_of, food, hunt, drink):
        self.name = name
        self.kind = kind_of
        self.food = food
        self.hunt = hunt
        self.drink = drink
    
    def hunting(self):
        if self.hunt == 'hunter':
            return f"when i'm hungry i look aruond for some prey to hunt and eata there {self.food}"
        elif self.hunt == 'hunted':
            return f"i sleep all night and wake up early in the morning going to the farm to eat my {self.food} breakfast"
        else:
            return f"i eat everyday {self.food}"
        
    def description(self):
        if self.name == 'Sultan the lion':
            return f"My name is {self.name} i love i live to hunt my food and drint {self.drink} from the river, i'm from {self.kind}"
        elif self.name == 'Hanem the cow':
            return f"Nice to meet you i'm {self.name} i help the farmer with a lot of things cuz he give me {self.food} and {self.drink}, i'm from {self.kind}"
        elif self.name == 'Saeed the shark':
            return f"My name is {self.name} i'm the big boss in the sea when my father the biger shark give me this name he knows that i'm going to rule this sea some day, i love to eat {self.food} and i drink the {self.drink} and a gland in my digestive system gets rid of excess salt, some people think i'm from Mammals but no i'm {self.kind}"
    
Lion = animal('Sultan the lion', 'Mammals', 'meat', 'hunter', 'water')
cow = animal('Hanem the cow', 'Mammals', 'Grass', 'hunted', 'water')
shark = animal('Saeed the shark', 'fish', 'meat', 'hunter', 'seawater')

print(Lion.hunting())
print(cow.hunting())
print(shark.hunting())

print(Lion.description())
print(cow.description())
print(shark.description())

class cat(animal):
    def __init__(self, name, kind_of, food, hunt, drink):
        super().__init__(name, kind_of, food, hunt, drink)

    def meow(self):
        return "cat1: meow meow meow, cat2: MEOW!, cat1: meow meow meow meow, cat2: mmmm meow meow meow"
    
kitty = cat('Kitty cat', 'Mammals', 'meat', 'hunter', 'milk')

print(kitty.meow())
print(kitty.hunting())