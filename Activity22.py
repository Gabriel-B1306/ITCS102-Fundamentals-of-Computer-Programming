# Multiple Dimensional List/Dictionary

# NARUTO CHARACTER & SKILLS
naruto_power = {
    "Name: ": "Naruto Uzumaki",
    "skill_1": "Rasengan",
    "skill_2": "Shadow Clone Jutsu",
    "skill_3": "Sage Mode",
    "skill_4": "Baryon Mode"
}

sasuke_power = {
    "Name: ": "Sasuke Uchiha",
    "skill_1": "Chidori",
    "skill_2": "Sharingan",
    "skill_3": "Amaterasu",
    "skill_4": "Susanoo"
}

# ONE_PIECE CHARACTER & SKILLS
luffy_power = {
    "Name: ": "Monkey D. Luffy",
    "skill_1": "Gum-Gum Pistol",
    "skill_2": "Gear Second",
    "skill_3": "Gear Fourth",
    "skill_4": "Gear Fifth"
}

zoro_power = {
    "Name: ": "Roronoa Zoro",
    "skill_1": "Three Sword Style",
    "skill_2": "Oni Giri",
    "skill_3": "Ashura",
    "skill_4": "King of Hell"
}

# BLEACH CHARACTER & SKILLS
ichigo_power = {
    "Name: ": "Ichigo Kurosaki",
    "skill_1": "Getsuga Tensho",
    "skill_2": "Bankai",
    "skill_3": "Hollow Mask",
    "skill_4": "Final Getsuga Tensho"
}

rukia_power = {
    "Name: ": "Rukia Kuchiki",
    "skill_1": "Sode no Shirayuki",
    "skill_2": "Some no Mai Tsukishiro",
    "skill_3": "Kido",
    "skill_4": "Hakka no Togame"
}

# RECALLING VARIABLE NAMES
Naruto = naruto_power
Sasuke = sasuke_power
Luffy = luffy_power
Zoro = zoro_power
Ichigo = ichigo_power
Rukia = rukia_power

# PUTTING CHARACTERS IN A LIST
NarutoSeries = [Naruto, Sasuke]
OnePiece = [Luffy, Zoro]
Bleach = [Ichigo, Rukia]

# ANIMES
Anime = {
    "NRT": NarutoSeries,
    "OP": OnePiece,
    "BL": Bleach
}

# OVERALL PRINT
print(Anime)

print("------------------------------------------------------------------------------------")
# Dictionary Print
print(Anime["NRT"])

print("------------------------------------------------------------------------------------")
# 2D Dimensional Print
print(Anime["OP"][0])

print("------------------------------------------------------------------------------------")
# Multiple Dimensional Print
print(Anime["BL"][0]["Name: "])
print(Anime["BL"][0]["skill_2"])
