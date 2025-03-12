# class Pokemon:
#     def __init__(self, name, types, evolution = None):
#         self.name = name
#         self.types = types
#         self.is_caught = False
#         self.evolution = evolution
#     def print_pokemon(self):
#         print({
#             "name": self.name,
#             "types": self.types,
#             "is_caught": self.is_caught
#         })
#     def catch(self):
#         self.is_caught = True
#     def choose(self):
#         if self.is_caught: print(self.name, " I choose you!")
#         else: print(self.name, " is wild! Catch them if you can!")
#     def add_type(self, new_type):
#         self.types.append(new_type)

# def get_evolutionary_line(starter_pokemon):
#     evoList = []
#     pkPtr = starter_pokemon
#     evoList.append(starter_pokemon.name)
#     while pkPtr.evolution:
#         pkPtr = pkPtr.evolution
#         evoList.append(pkPtr.name)
#     return evoList
# def get_by_type(my_pokemon, pokemon_type):
#     hasType = []
#     for pk in my_pokemon:
#         if pokemon_type in pk.types:
#             hasType.append(pk)
#     return hasType
# Problems 1-6
# my_pokemon = Pokemon("Pikachu", ["Electric"])
# squirtle = Pokemon("Squirtle", ["Water"])
# squirtle.is_caught = True
# squirtle.print_pokemon()
# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()
# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()
# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()

# Problem 7 # initializing pokemons
# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)

# Problem 8
# charizard = Pokemon("Charizard", ["fire", "flying"])
# charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
# charmander = Pokemon("Charmander", ["fire"], charmeleon)

# charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

# charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

# charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def print_linked_list(head):
    ptr = head
    while ptr:
        print(ptr.value, end = '')
        if ptr.next:
            print('->', end = '')
        ptr = ptr.next


# node_one = Node('a')
# node_two = Node('b')
# node_one.next = node_two
# print(node_one.value) 
# print(node_one.next.value) 
# print(node_two.value) 

node_4 = Node("Toad")
node_3 = Node("Wario", node_4)
node_2 = Node("Luigi", node_3)
node_1 = Node("Mario", node_2)

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)

print_linked_list(node_1)