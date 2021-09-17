#Game Version 0.0.2

import random
import time
import sys
from dataclasses import dataclass

#Monster spawner
@dataclass
class Monster:

    hp: int
    damage: int

#Starting location
go_north = 0
go_south = 0
go_east = 0
go_west = 0

#loot table

weapn_loot = {"Wooden sword" : 10, "Stone Sword" : 50, "Steel Sword" : 200, "Emerald Sword" : 600}

armor_loot_try = [
    ["Robe of power", 30, 90],
    ["Robe of doom", 40, 110],
    ["Robe of fire", 60, 140],
    ["Robe of wind", 80, 160],
    ["Robe of air", 100, 180],
    ["Robe of elementals", 120, 200],
    ["Robe of water", 140, 230],
    ["Robe of mages", 160, 260],
    ["Robe of wisdom", 180, 290],
    ["Robe of nothing", 200, 300],
    ["Hazzard suit", 500, 1500]
]

#inventory
inventory = [["Potion"], ["Potion"], ["Potion"], ["Potion"], ["Potion"]]

#Equipment
armor_slot = [["Noob armor", 20, 30]]
weapon_slot = weapn_loot.get("Wooden sword")

#Char stats
char_level = 1
char_hp = char_level * 100 + armor_slot[0][1]
char_max_hp = char_level * 100 + armor_slot[0][1]
char_xp = 1
char_name = ""

#Game start
potion_dealer_asked = 0
char_name = input("Enter your character name: ")

#Check for level up.
while True:
    no_moster_spawn = True
    #char_dmg = char_level + weapon_slot * char_level
    xp_to_level = char_level * (char_level * 100)
    if char_xp >= xp_to_level:
        char_level += 1
        char_hp = char_level * 100 + armor_slot[0][1]
        print(f'DING! {char_name} is now level {char_level}')

#Ask player where to go.
    print("Where do you want to go? Use n, s, e, w for movement, i to see inventory.")
    movement = input("> ")
    allowed_movement = ["N", "S", "E", "W", "I", "n", "s", "e", "w", "i"]
    while movement not in allowed_movement:
        print("Wrong input...")
        movement = input("Where do you want to go?, N, S, E, W: ")
 
#Update cords.
    if movement.upper() == "N":
        if go_north <= 9 and go_south == 0:
            go_north += 1
            no_moster_spawn = False
            spawn_monster = random.randint(1, 50)
        elif go_south > 0:
            go_south -= 1
        else:
            no_moster_spawn = True
            print(f'You can\'t go more north, out of bounds')
    elif movement.upper() == "S":
        if go_south <= 9 and go_north == 0:
            go_south += 1
            no_moster_spawn = False
            spawn_monster = random.randint(1, 50)
        elif go_north > 0:
            go_north -= 1
        else:
            no_moster_spawn = True
            print(f'You can\'t go more south, out of bounds')
    elif movement.upper() == "E":
        if go_east <= 9 and go_west == 0:
            go_east += 1
            no_moster_spawn = False
            spawn_monster = random.randint(1, 50)
        elif go_west > 0:
            go_west -= 1
        else:
            no_moster_spawn = True
            print(f'You can\'t go more east, out of bounds')
    elif movement.upper() == "W":
        if go_west <= 9 and go_east == 0:
            go_west += 1
            no_moster_spawn = False
            spawn_monster = random.randint(1, 50)
        elif go_east > 0:
            go_east -= 1
        else:
            no_moster_spawn = True
            print(f'You can\'t go more west, out of bounds')
    elif movement.upper() == "I":
        no_moster_spawn = True
        spawn_monster = 10
        for i in range(len(inventory)):
            print(i+1,inventory[i])
        while True:
            print("What do you want to do?\n(1)Equip item\n(2)Close inventory.")
            inv_input = input('> ')
            try:
                if int(inv_input) == 1:
                    print('What item do you want to equip? asnwear by typing the number of the line:')
                    item_equip = int(input('> '))
                    if item_equip -1 < 0:
                        print("That's not an item")
                    elif inventory[item_equip -1] == ["Potion"]:
                        print("You can't equip a potion as armor.")
                    else:
                        armor_slot.clear()
                        armor_slot.append(inventory[item_equip -1])
                        print(f'You have equiped {armor_slot}')
                        inventory.remove(inventory[item_equip -1])
                        break
                elif int(inv_input) == 2:
                    print("Inventory closed")
                    break
                else:
                    print("Wrong input.")
            except ValueError:
                print("Wrong input!")

    print(f'{char_name} is now at position:\nNorth: {go_north}, South: {go_south}, East: {go_east}, West: {go_west}')
    
    if go_north == 3 and go_east == 3:
        spawn_monster = 10
        print("You have arrived at a potion dealer.")
        print("Talk (1)\nAsk for a free potion (2)")
        action_to_take = input('> ')
        if int(action_to_take) == 1:
            print(f'Potion dealer: Welcome {char_name}, Nice day isn\'t it?')
        elif int(action_to_take) == 2:
            if potion_dealer_asked > 9:
                print("You asked me 10 times already!! Go away!!")
            else:
                give_hp_potion = random.randint(0,100)
                if give_hp_potion > 95:
                    inventory.append(["Potion"])
                    print(f'You now have {inventory.count(["Potion"])} Hp potions')
                    potion_dealer_asked += 1
                else:
                    print(f'Potion dealer: I don\'t give away free HP potions just like that.')
                    potion_dealer_asked += 1
        elif int(action_to_take) == 000:
            weapon_slot = weapn_loot.get("Emerald Sword")
            print(weapon_slot)
            print("Potion dealer: CHEATER!!... But here, take my sword.")
            print("You know have the Emerald Sword.")   

    elif go_north == 0 and go_south == 0 and go_east == 0 and go_west == 0:
        spawn_monster = 10
        print("You're at the starting location'.")
    elif no_moster_spawn == False:
        spawn_monster = random.randint(1,50)

#Is fight?
    if spawn_monster > 30:

        #Spawn a monster with the attributes (HP, Damage)

        new_monster = Monster(char_level * 100, round(char_level * 200 / armor_slot[0][2]))

        while True:
                char_dmg = char_level + weapon_slot * char_level
                char_dmg += random.randint(5,15)
                new_monster.damage = round(char_level * 200 / armor_slot[0][2]) + random.randint(1,5)
                print (f'You\'re in a fight. What do you want to do?\n(1)Attack\n(2)Use HP Potion. You have {inventory.count(["Potion"])} HP potions')
                action_to_take = input('> ')
                try:
                    if int(action_to_take) == 1:
                        if new_monster.hp > 0:
                            new_monster.hp -= char_dmg
                            if new_monster.hp <= 0:
                                char_xp += 20 * char_level
                                print(f'{char_name} hits monster for {char_dmg}')
                                print("The monster dies.\n")
                                print(char_name,"gains 20 xp\n")
                                drop_hp_potion = random.randint(1,100)
                                if drop_hp_potion < 70:
                                    print("You found a HP potion")
                                    inventory.append(["Potion"])
                                    if char_level < 3:
                                        armor_to_loot = armor_loot_try[random.randint(0,1)]
                                        print(armor_to_loot[0], 'dropped.') 
                                    elif char_level > 2 and char_level < 5:
                                        armor_to_loot = armor_loot_try[random.randint(2,3)]
                                        print(armor_to_loot[0], 'dropped.') 
                                    elif char_level > 4 and char_level < 7:
                                        armor_to_loot = armor_loot_try[random.randint(4,5)]
                                        print(armor_to_loot[0], 'dropped.') 
                                    elif char_level > 6 and char_level < 9:
                                        armor_to_loot = armor_loot_try[random.randint(6,7)]
                                        print(armor_to_loot[0], 'dropped.') 
                                    elif char_level > 8 and char_level < 11:
                                        armor_to_loot = armor_loot_try[random.randint(8,9)]
                                        print(armor_to_loot[0], 'dropped.') 
                                    else:
                                        armor_to_loot = armor_loot_try[10]
                                        print(armor_to_loot[0], 'dropped.') 
                                    if armor_to_loot in inventory:
                                        print(armor_to_loot, 'is already in your inventory. Unable to loot.')
                                    elif armor_to_loot in armor_slot:
                                        print(armor_to_loot, 'is already equipped. Unable to loot')
                                    else:
                                        inventory.append(armor_to_loot)
                                    print(f'You have {inventory.count(["Potion"])} HP potion(s) now.')                                                      
                                time.sleep(1)
                                break
                            else:
                                print(f'{char_name} hits monster for {char_dmg}\n')
                                print(f'Monster hp is now {new_monster.hp}\n')
                                char_hp -= new_monster.damage
                                if char_hp <= 0:
                                    print(f'{char_name} died! lol xD\n')
                                    sys.exit()
                                else:
                                    print(f'Monster hits {char_name} for {new_monster.damage}\n')
                                    print(f'{char_name} health is now {char_hp}\n')
                    elif int(action_to_take) == 2:
                        char_max_hp = char_level * 100 + armor_slot[0][1]
                        if ["Potion"] in inventory:
                            if char_hp <= char_max_hp * 0.80:
                                char_hp = char_hp + round((char_hp * 0.20))
                                print(f'{char_name} is being healed.')
                                print(f'{char_name} is now at {char_hp} HP.')
                                inventory.remove(["Potion"])
                            elif char_hp <= char_max_hp -1:
                                char_hp = char_level * 100 + armor_slot[0][1]
                                print(f'{char_name} is now at {char_hp} HP.')
                                inventory.remove(["Potion"])
                            else:
                                print("You are already at full life.")
                        else:
                            print("You are out of HP potions.")
                    else:
                        print(f'Unknown command {action_to_take}')
                except ValueError:
                    print(f'Unknown command {action_to_take}')