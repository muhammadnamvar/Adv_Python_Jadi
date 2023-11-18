import random


class Human:

    def __init__(self, name=None, age=None, height=None):
        self.name = name
        self.age = age
        self.height = height

    def get_info(self):
        print("name: ", self.name)
        print("age: ", self.age)
        print("height: ", self.height)


class Player(Human):

    def __init__(self, name=None, age=None, height=None, post=None, skill=None):
        Human.__init__(self, name, age, height)
        self.post = post
        self.skill = skill

    def get_info(self):
        Human.get_info(self)
        print("post: ", self.post)
        print("skill: ", self.skill)
        print("Team: ", self.team)

    def set_team(self, team):
        self.team = team


names = ("ali-hassan-hossein-sajad-jafar-sadegh-mosa-reza-taghi-naghi-asgar-mahdi-"
         "kurosh-khashi-dariush-ebi-esi-hayedeh-homeyra-chavoosh-shadi-sara").split('-')
post = ["Gk", "CB", "LB", "RB", "CM", "LM", "RM", "AM", "LWF", "RWF", "SS", "CF"]
players = list()
for i in range(22):
    print(f"$$$$$$$$$$$$ {i + 1} $$$$$$$$$$$$$$$$$")
    name = random.choice(names)
    names.remove(name)
    players.append(Player(name, random.choice(range(16, 38)), random.choice(range(165, 199)),
                          random.choice(post), random.choice(range(70, 99))))
    players[i].set_team(random.choice(["A", "B"]))
    players[i].get_info()
