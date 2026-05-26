from our_dice import Dice

gamer1Dice = Dice()
gamer2Dice = Dice()
gamer3Dice = Dice()

for i in range(5):
    gamer1Dice.playDice()
    gamer2Dice.playDice()
    gamer3Dice.playDice()

print(f'gamer1:{gamer1Dice.getNumbers()}')
print(f'gamer2:{gamer2Dice.getNumbers()}')
print(f'gamer3:{gamer3Dice.getNumbers()}')

print(f'sum of gamer1: { gamer1Dice.getSum()}')
print(f'sum of gamer2: { gamer2Dice.getSum()}')
print(f'sum of gamer3: { gamer3Dice.getSum()}')