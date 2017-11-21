#Hákon Haraldsson & Viðar Marel
#Lokaverkefni í Forritun 2
#21.11.2017
import random
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
teningur = random.randint(1,6)
hamsturLocation = random.randint(1,75)
rottaLocation1 = random.randint(1,100)
rottaLocation2 = random.randint(1,100)
rottaLocation3 = random.randint(1,100)
musLocation    = random.randint(1,75)
print("-------Nagdýraleikur--------")
