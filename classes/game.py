import random, math

class bcolors:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'
    yellow = '\033[0m 1;33;40m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name    = name
        self.maxhp   = hp
        self.hp      = hp
        self.maxmp   = mp
        self.mp      = mp
        self.atkl    = atk - 10
        self.atkh    = atk + 10
        self.df      = df
        self.magic   = magic
        self.items   = items
        self.actions = ["Attack", "Magic", "Item"]
    
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def generate_spell_name(self, i):
        return self.magic[i]["name"]

    def spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("     Actions")
        for item in self.actions:
            print("         " + str(i) + ":", item)
            i+=1

    def choose_magic(self):
        i = 1
        print("     Magic")
        for spell in self.magic:
            print("         " + str(i) + ":", spell.name, ": cost = ", spell.cost)
            i+=1

    def choose_item(self):
        i = 1
        print("     Items")
        for items in self.items:
            print("         " + str(i) + ":", items.name, ": quantity : " + str(items.quantity))
            i+=1

    def choose_target(self, enemies):
        i = 1
        print("     Target")
        for enemy in enemies:
            print("         " + str(i) + ":", enemy.name)
            i+=1

    def get_enemy_stats(self):
        current_hp = math.ceil((self.get_hp() / self.maxhp) * 20)
        hpbar = ""

        hp_reduced = 20 - current_hp
        hpbar_ = ""

        while current_hp != 0:
            hpbar += "█"
            current_hp -= 1

        while hp_reduced != 0:
            hpbar_ += " "
            hp_reduced -= 1

        if self.get_hp() in range(10, 100):
            hp = " " + str(self.get_hp()) + "/" + f"{str(self.maxhp)}|"

        elif self.get_hp() < 10:
            hp = "  " + str(self.get_hp()) + "/" + f"{str(self.maxhp)}|"

        else:
            hp = str(self.get_hp()) + "/" + f"{str(self.maxhp)}|"

        print(self.name + "       " + hp + hpbar + hpbar_ + "|")



    def get_stats(self):
        current_hp = math.ceil((self.get_hp() / self.maxhp) * 20)
        hpbar = ""

        hp_reduced = 20 - current_hp
        hpbar_ = ""

        while current_hp != 0:
            hpbar += "█"
            current_hp -= 1

        while hp_reduced != 0:
            hpbar_ += " "
            hp_reduced -= 1

        
        current_mp = math.ceil((self.get_mp() / self.maxmp) * 10)
        mpbar = ""

        mp_reduced = 10 - current_mp
        mpbar_ = ""

        while current_mp != 0:
            mpbar += "█"
            current_mp -= 1

        while mp_reduced != 0:
            mpbar_ += " "
            mp_reduced -= 1


        if self.get_hp() in range(10, 100):
            hp = " " + str(self.get_hp()) + "/" + f"{str(self.maxhp)}|"

        elif self.get_hp() < 10:
            hp = "  " + str(self.get_hp()) + "/" + f"{str(self.maxhp)}|"

        else:
            hp = str(self.get_hp()) + "/" + f"{str(self.maxhp)}|"


        if self.get_mp() in range(10, 100):
            mp = " " + str(self.get_mp()) + "/" + f"{str(self.maxmp)}|"

        elif self.get_mp() < 10:
            mp = "  " + str(self.get_mp()) + "/" + f"{str(self.maxmp)}|"

        else:
            mp = str(self.get_mp()) + "/" + f"{str(self.maxmp)}|"


        print(self.name + "      " + hp + hpbar + hpbar_ + "|" +
              "      " + mp + mpbar + mpbar_ + "|")