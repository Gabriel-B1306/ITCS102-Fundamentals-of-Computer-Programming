# Multiple Dimensional List/Dictionary

# THE SAGA OF TANYA THE EVIL
tanya = ["Tanya Degurechaff", "Elinium Type 95", "Flight Magic", "Explosive Formula", "Optical Decoy"]
visha = ["Viktoriya Serebryakov", "Flight Magic", "Illusion Formula", "Marksmanship", "Defensive Barrier"]

# ONE_PIECE CHARACTER & SKILLS
luffy = ["Monkey D. Luffy", "Gum-Gum Pistol", "Gear Second", "Gear Fourth, Gear Fifth"]
zoro = ["Roronoa Zoro", "Three Sword Style", "Oni Giri", "Ashura", "King of Hell"]

# NO GAME NO LIFE
sora = ["Sora", "Cold Reading", "Bluffing", "Negotiation", "Game Theory"]
shiro = ["Shiro", "Superhuman Intellect", "Chess Mastery", "Perfect Memory", "Probability Calculation"]

# BLACK CLOVER CHARACTER & SKILLS
Asta = ["Magic Knight of the Black Bulls", "Demon Slayer Sword", "Black Meteorite", "Black Divider", "Demon-Dweller Sword"]
Yuno = ["Vice-captain of the Golden Dawn,", "Wind Magic", "Spirit of Zephyr", "Spirit of Sylph","Spirit of the Wind God"]


# RECALLING VARIABLE NAMES
Saga_Tanya = {"tanya": tanya, "visha": visha}
OnePiece = {"Luffy": luffy, "Zoro": zoro}
NoGameNoLife = {"Sora": sora, "Shiro": shiro}
BlackClover = {"Asta": Asta, "Yuno": Yuno}

# PUTTING CHARACTERS IN A LIST
NarutoSeries = [Naruto, Sasuke]
OnePiece = [Luffy, Zoro]
Bleach = [Ichigo, Rukia]
BlackClover = [Asta, Yuno]

# ANIMES
Anime = {
    "NRT": NarutoSeries,
    "OP": OnePiece,
    "BL": Bleach,
    "BC": BlackClover
}



#Transvesal 
for x, y in Anime.items():
    print(x, y)
