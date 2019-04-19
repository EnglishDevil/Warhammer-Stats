
boltRifle = {'wtype': 'RapidFire', 'range': 30, 'strength': 4, 'AP': -1, 'damage': 1}
bolter = {'wtype': 'RapidFire', 'range': 24, 'strength': 4, 'AP': 1, 'damage': 1}
Intercessor = {'move': 5, 'BS': 3, 'strength': 4, 'toughness': 4, 'wounds': 2, 'save': 3}
Plaguemarine = {'move': 5, 'BS': 3, 'strength': 4, 'toughness': 5, 'wounds': 1, 'save': 3, 'save++': 5}

# Fight Unit
# Variables
RapidFire = 0

how_many = input("Enter how many are shooting with the same type of of weapon")

# Number of Shots

rapidfirerange = input("Are they within rapid fire range? Enter yes or No")
if rapidfirerange == "yes":
    RapidFire += 2
else: RapidFire += 1
shots = RapidFire * int(how_many)
print("Firing" + " " + str(shots) + " ")

target = input("What is the target?")
if target == "Plaguemarine":
    print("Death to the Heretics!")

hit_roll = Intercessor['BS']
print("Hitting on a" + " " + str(hit_roll) + " " + "+")

#Hit Roller
#Variables
hits = 0
misses = 0
count = 0

import random

while count < shots:
    roll = random.randint(1, 6)
    if hit_roll >= roll:
        hits += 1
        count += 1
    else:
        misses += 1
        count += 1

print("Hit" + " " + str(hits) + " " + "times")
print("Missed" + " " + str(misses) + " " + "times")

# Wound
# Wound variables
woundroll = 1
woundcount = 0
succesful_wounds = 0


if int(boltRifle['strength']) > target['toughness']:
    woundroll += 3
elif int(boltRifle['strength']) == int(target['toughness']*2:
    woundroll += 2
elif int(boltRifle['strength']) == int(target['toughness']):
    woundroll += 4
elif int(boltRifle['strength']) < int(target['toughness']):
    woundroll += 5
else: woundroll += 6

while woundcount < hits:
    roll = random.randint(1, 6)
    if hit_roll >= roll:
        succesful_wounds += 1
        woundcount += 1
    else:
        woundcount += 1

print("Inflicted" + " " + str(succesful_wounds))





cover = input(input("Is the targert in cover? Enter yes or no"))

#Unit type
#How many
#What range
#Target
#In cover or not        `



def d6decimal (d6_result):
    #chance of success on a d6
    d6_chance_decimal = (7 - d6_result)/6
    return d6_chance_decimal
print("what is the chance of of a plaguemarine failing his disgusting resilient?")
PM_DR = Plaguemarine['save++'] # <- we use square brackets to pull the named values

chance_PM_pass_DR = d6decimal(PM_DR)
print(chance_PM_pass_DR)


print("what is the chance of of a plaguemarine failing his disgusting resilient?")
#first we have to get that value from the dictionary:
PM_DR = Plaguemarine['save++'] # <- we use square brackets to pull the named values

chance_PM_pass_DR = d6decimal(PM_DR)
print(chance_PM_pass_DR)

# what if we want him to fail?
chance_PM_fail_DR = 1- chance_PM_pass_DR
print("chance of Plaguemarine to fail DR is: " + str(chance_PM_fail_DR)) # <- we can add the strings together, but first I had to turn that number into a string (using str()p
