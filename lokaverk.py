# Hákon Haraldsson & Viðar Marel
# Lokaverkefni í Forritun 2
# 21.11.2017
import random
"""
class color:
    mus = "\033[1;35;40m"
    hamstur = "\033[1;33;40m"
    rotta1 = "\033[1;32;40m"
    rotta2 = "\033[1;34;40m"
    rotta3 = "\033[1;36;40m"
"""
def battleDetectorV2(locMus ,locHam, locRot1, locRot2, locRot3):
    if locMus == locHam:
        print("Hamstur Trigger")
    if locMus == locRot1:
        print("Rotta1 Trigger")
    if locMus == locRot2:
        print("Rotta2 Trigger")
    if locMus == locRot3:
        print("Rotta3 Trigger")

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
    locHam  = 666
    locRot1 = 666
    locRot2 = 666
    locRot3 = 666
    print("ROUND",teljari)
    input("kastar tening")
    currentTen = teningur
    print("Þú kastaðir",teningaUmbreytir(currentTen))
    for x in range(1,currentTen):
        mus.stad = mus.stad + 1
        locMus = mus.stad
        locHam = hamstur.stad
        locRot1 = rotta1.stad
        locRot2 = rotta2.stad
        locRot3 = rotta3.stad
    currentTen = random.randint(1,6)
    print("Hamstur kastar")
    upOrDown = random.randint(1, 2)
    print("Hún fékk", teningaUmbreytir(currentTen))
    if upOrDown == 1:
        print("Hún fer upp!")
    else:
        print("Hún fer niður!")
    for x in range(1, currentTen):
        if upOrDown == 1:
            rotta1.stad = rotta1.stad + 1
        elif upOrDown == 2:
            rotta1.stad = rotta1.stad - 1
        locMus = mus.stad
        locRot1 = rotta1.stad
        battleDetectorV2(locMus, locHam, locRot1, locRot2, locRot3)
    print("Rotta eitt kastar")
    upOrDown = random.randint(1, 2)
    print("Hún fékk",teningaUmbreytir(currentTen))
    if upOrDown == 1:
        print("Hún fer upp!")
    else:
        print("Hún fer niður!")
    for x in range(1,currentTen):
        if upOrDown == 1:
            rotta1.stad = rotta1.stad + 1
        elif upOrDown == 2:
            rotta1.stad = rotta1.stad - 1
        locMus = mus.stad
        locRot1 = rotta1.stad
        battleDetectorV2(locMus, locHam, locRot1, locRot2, locRot3)
    print("Rotta Tvö kastar")
    upOrDown = random.randint(1, 2)
    print("Hún fékk",teningaUmbreytir(currentTen))
    if upOrDown == 1:
        print("Hún fer upp!")
    else:
        print("Hún fer niður!")
    for x in range(1,currentTen):
        if upOrDown == 1:
            rotta2.stad = rotta2.stad + 1
        elif upOrDown == 2:
            rotta2.stad = rotta2.stad - 1
        locMus = mus.stad
        locRot2 = rotta2.stad
        battleDetectorV2(locMus, locHam, locRot1, locRot2, locRot3)
    print("Rotta þrjú kastar")
    upOrDown = random.randint(1, 2)
    print("Hún fékk",teningaUmbreytir(currentTen))
    if upOrDown == 1:
        print("Hún fer upp!")
    else:
        print("Hún fer niður!")
    for x in range(1,currentTen):
        if upOrDown == 1:
            rotta3.stad = rotta3.stad + 1
        elif upOrDown == 2:
            rotta3.stad = rotta3.stad - 1
        locMus = mus.stad
        locRot3 = rotta3.stad
        battleDetectorV2(locMus, locHam, locRot1, locRot2, locRot3)
    if mus.stad > 100:
        mus.stad = 100
    print("Músin fór áfram á reit", mus.stad)
    print("Hamstur fór áfram á reit", hamstur.stad)
    print("Rotta eitt fór áfram á reit", rotta1.stad)
    print("Rotta tvö fór áfram á reit", rotta2.stad)
    print("Rotta Þrjú fór áfram á reit", rotta3.stad)
print("Þú vannst")