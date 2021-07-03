from classes.game import bcolors, Person
from classes.magic import Spell
from classes.inventory import Items
from colorama import Fore, Back, Style
import random

#Black magic spells
fire     = Spell("Fire", 10, 100, "black")
thunder  = Spell("Thunder", 10, 100, "black")
blizzare = Spell("Blizzare", 10, 100, "black")
meteor   = Spell("Meteor", 20, 200, "black")
quake    = Spell("Quake", 20, 200, "black")

#White magic spells
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 10, 200, "white")

#Inventory
potion   = Items({"item" : "Potion", "type" : "potion", "quantity" : 3, "prop" : 20})
hipotion = Items({"item" : "Hi-potion", "type" : "potion", "quantity" : 3, "prop" : 100})
elixer   = Items({"item" : "Elixer", "type" : "elixer", "quantity" : 1, "prop" : 500})
grenade  = Items({"item" : "Grenade", "type" : "attack", "quantity" : 3, "prop" : 100})

#Creating players
player_magic = [fire, thunder, blizzare, meteor, quake]
player_items = [potion, hipotion, elixer, grenade]

player1 = Person("Kilo  ", 500, 65, 60, 30,  player_magic, player_items)
player2 = Person("Whisky", 500, 65, 60, 30,  player_magic, player_items)

enemy1  = Person("Alpha ", 500, 65, 60, 30, [fire, thunder, meteor, quake, cure], [hipotion, grenade])
enemy2  = Person("Tango ", 500, 65, 60, 30, [fire, blizzare, meteor, cure], [potion, grenade])

players = [player1, player2]
enemies = [enemy1, enemy2]

#Game code
run = True
i = 0
defeated_enemy = 0
defeated_player =0

print(Fore.BLUE + "Game begins.") 

while run:
    print("\n***************\n")

    print("Name                 HP                                MP          ")
    for player in players:
        player.get_stats()

    print("\n")
    print("Name                 HP")
    for enemy in enemies:
        enemy.get_enemy_stats()
    
    for player in players:
        print("\n" + " " + player.name)
        player.choose_action()
        choice = int(input("         Choose action: ")) - 1

        if choice == 0:
            dmg = player.generate_damage()

            player.choose_target(enemies)
            target_choice = int(input("         Choose target: ")) - 1

            if enemies[target_choice].get_hp() <= dmg:
                enemies[target_choice].take_damage(dmg)
                print("\nYou attacked " + enemies[target_choice].name.replace(" ", "") + " for " + str(dmg) + " points")
                print("\n" + enemies[target_choice].name.replace(" ", "") + " is dead.")
                del enemies[target_choice]
                defeated_enemy += 1

            else:
                enemies[target_choice].take_damage(dmg)
                print("\nYou attacked " + enemies[target_choice].name.replace(" ", "") + " for " + str(dmg) + " points")

        elif choice == 1:
            player.choose_magic()
            magic_choice = int(input("         Choose magic: ")) - 1

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()


            if spell.cost > player.get_mp():
                print("\nYou don\'t have enough mp.")
                continue

            if spell.types == "white":
                player.heal(magic_dmg)
                print("\n" + spell.name + " heals " + str(magic_dmg) + " HP")

            elif spell.types == "black":
                player.choose_target(enemies)
                target_choice = int(input("         Choose target: ")) - 1

                if enemies[target_choice].get_hp() <= magic_dmg:
                    enemies[target_choice].take_damage(magic_dmg)
                    print("\n" + spell.name + " deals " + str(magic_dmg) + " damage to " + enemies[target_choice].name.replace(" ", ""))
                    print("\n" + enemies[target_choice].name.replace(" ", "") + " is dead.")
                    del enemies[target_choice]
                    defeated_enemy += 1

                else:
                    enemies[target_choice].take_damage(magic_dmg)
                    print("\n" + spell.name + " deals " + str(magic_dmg) + " damage to " + enemies[target_choice].name.replace(" ", ""))

            player.reduce_mp(spell.cost)


        elif choice == 2:
            player.choose_item()
            item_choice = int(input("         Choose item: ")) - 1

            item = player.items[item_choice]

            if item.quantity == 0:
                print("\nNone left...")
                continue

            if item.type == "potion":
                player.heal(item.prop)
                print("\nPlayer heals for " + str(item.prop) + " HP")

            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print("\n" + item.name + " fully restores HP/MP")

            elif item.type == "attack":
                player.choose_target(enemies)
                target_choice = int(input("         Choose target: ")) - 1

                if enemies[target_choice].get_hp() <= item.prop:
                    enemies[target_choice].take_damage(item.prop)
                    print("\n" + item.name + " deals " + str(item.prop) + " damage to " + enemies[target_choice].name.replace(" ", ""))
                    print("\n" + enemies[target_choice].name.replace(" ", "") + " is dead.")
                    del enemies[target_choice]
                    defeated_enemy += 1

                else:
                    enemies[target_choice].take_damage(item.prop)
                    print("\n" + item.name + " deals " + str(item.prop) + " damage to " + enemies[target_choice].name.replace(" ", ""))

            item.quantity -= 1

        if defeated_enemy == 2:
            print("You won.")
            run = False


    for enemy in enemies:
        enemy_choice = random.randrange(3)

        if enemy_choice == 0:
            dmg = enemy.generate_damage()
            target = random.randrange(len(players))

            if players[target].get_hp() <= dmg:
                players[target].take_damage(dmg)
                print("\n" + players[target].name.replace(" ", "") + " is dead.")
                del players[target]
                defeated_player += 1

            else:
                players[target].take_damage(dmg)

        elif enemy_choice == 1:
            magic_choice = random.randrange(len(enemy.magic))

            spell = enemy.magic[magic_choice]
            magic_dmg = spell.generate_damage()


            if spell.cost > enemy.get_mp():
                continue

            if spell.types == "white" and enemy.get_hp() < 100:
                enemy.heal(magic_dmg)

            elif spell.types == "black":
                target = random.randrange(len(players))

                if players[target].get_hp() <= magic_dmg:
                    players[target].take_damage(magic_dmg)
                    print("\n" + players[target].name.replace(" ", "") + " is dead.")
                    del players[target]
                    defeated_player += 1

                else:
                    players[target].take_damage(magic_dmg)

            enemy.reduce_mp(spell.cost)


        elif enemy_choice == 2:
            item_choice = random.randrange(len(enemy.items))

            item = enemy.items[item_choice]

            if item.quantity == 0:
                continue

            if item.type == "potion" and enemy.get_hp() == 200:
                enemy.heal(item.prop)


            elif item.type == "attack":
                target = random.randrange(len(players))

                if players[target].get_hp() <= item.prop:
                    players[target].take_damage(item.prop)
                    print("\n" + players[target].name.replace(" ", "") + " is dead.")
                    del players[target]
                    defeated_player += 1

                else:
                    players[target].take_damage(item.prop)

        if defeated_player == 2:
            print("You lost.")
            run = False