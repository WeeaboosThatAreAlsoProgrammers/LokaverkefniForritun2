# Hákon Haraldsson & Viðar Marel
# Lokaverkefni í Forritun 2
# 21.11.2017
import random
"""
class color:        #teningur ætti að litast eftir hvaða karakter kastar teningunum
    mus = "\033[1;35;40m"
    hamstur = "\033[1;33;40m"
    rotta1 = "\033[1;32;40m"
    rotta2 = "\033[1;34;40m"
    rotta3 = "\033[1;36;40m"
"""
class Nagdyr:   #Verður notað fyrir alla karkatera
    def __init__(self, tegund, stadsetning, afl):
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl
aflKat = 1
while aflKat % 2 == 0:
    random.randint(1,6)
mus = Nagdyr("Mús", 1, random.randrange(2, 6))
hamstur = Nagdyr("Hamstur", random.randint(1, 100), random.randrange(1, 6))
rotta1 = Nagdyr("rotta1", random.randint(1, 100), random.randrange(1, 6))
rotta2 = Nagdyr("rotta2", random.randint(1, 100), random.randrange(1, 6))
rotta3 = Nagdyr("rotta3", random.randint(1, 100), random.randrange(1, 6))
def teningaUmbreytir(teningur):
    if teningur == 1:
        teningurVis = "⚀"
    if teningur == 2:
        teningurVis = "⚁"
    if teningur == 3:
        teningurVis = "⚂"
    if teningur == 4:
        teningurVis = "⚃"
    if teningur == 5:
        teningurVis = "⚄"
    if teningur == 6:
        teningurVis = "⚅"
    return teningurVis
teljari = 0
print("-------Nagdýraleikur--------")
while mus.stad < 100:
    teningur = random.randint(1, 6)
    teljari = teljari + 1
    print("ROUND",teljari)
    input("kastar tening")
    currentTen = teningur
    print("Þú kastaðir",teningaUmbreytir(currentTen))
    for x in range(1,currentTen):
        mus.stad = mus.stad + 1
    if mus.stad > 100:
        mus.stad = 100
    print("músin fór áfram á reit", mus.stad)
print("Þú vannst")