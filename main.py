from Classes.game import Person, bcolors


"""
from Classes.magic import Spell

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "White")

"""

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("==================")
    player.choose_action()
    choice = input("Choose an action:")
    #index = int(choice) - 1
    if int(choice) == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("you attacked for", dmg, "points of damage.", "Enemy HP", enemy.get_hp())

    enemy_choice = 0

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.", "Player HP", player.get_hp())

'''
    elif int(choice) == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic"))
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\n Not enough MP \n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + "deals", str(magic_dmg), "points of damage" +bcolors.ENDC)



    print("_____________________________")
    print("Enemy hp:", bcolors.FAIL + str(enemy.get_hp()) + "/" +str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your hp:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your mp:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")


    if enemy.get_hp() == 0:
        print(bcolors.GREEN + bcolors.BOLD + "You have WON!!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You have been defeated :(" + bcolors.ENDC)
        running = False

'''