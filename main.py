from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.inventory import Item

print("\n\n")
print("NAME                    HP                                  MP")
print("                        ____________________                _____________ ")
print(bcolors.BOLD + "Valos:          460/460|" + bcolors.OKGREEN + "████████████        " + bcolors.ENDC + bcolors.BOLD + "|     " +
      "65/65    |" + bcolors.OKBLUE + "█████████████" + bcolors.ENDC + "|")
print("                        ____________________                ____________________ ")
print("Valos:          450/450|                    |     65/65    |                    |")
print("                        ____________________                ____________________ ")
print("Valos:          450/450|                    |     65/65    |                    |")
print("\n\n")

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixir", "elixir", "Fully restores HP/MP of one party member ", 9999)
hielixer = Item("Mega Elixir", "elixir", "Fully restores HP/MP ", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 15},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 15}]

# Initiate people
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("==================")
    player.choose_action()
    choice = input("Choose an action:")
    # index = int(choice) - 1

    if int(choice) == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("you attacked for", dmg, "points of damage.")

    elif int(choice) == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic"))

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\n Not enough MP \n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "heals for", str(magic_dmg), "HP" + bcolors.ENDC)

        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    elif int(choice) == 2:
        player.choose_item()
        item_choice = int(input("Choose item: "))

        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
            continue

        player.items[item_choice]["quantity"] -= 1

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)
        elif item.type == "elixir":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + "deals", str(item.prop), "Points of damage" + bcolors.ENDC)
    enemy_choice = 0

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    print("_____________________________")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You have WON!!" + bcolors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You have been defeated :(" + bcolors.ENDC)
        running = False