''' Code for adam '''
# I'm going to add in an intercessor

# Here is the bolt rifle. The intercessor profile references this.
boltRifle = {"type": "rapidFire", "strength": 4, "ap": -1, "damage": 2}
krakGrenade = {"type": "grenade", "strength": 6, "ap": -2,
               "damage": 'd3'}  # to use this we would need adapt some of the later stuff to be able to deal with d3

# I've made an intercessor. The weapon, boltRifle, is in a "list". This is because they can have more than one
# I'm not going to use the grendades, it's just an example
Intercessor = {"move": 6, "BS": 3, "WS": 3, "stength": 4, "toughness": 5, "wounds": 2, "attacks": 2, "save": 3,
               "weapon": [boltRifle, krakGrenade]}


# obviously I need to explain this better.
# functions are ways of packaging up stuff you will do a lot to make the whole thing neater.
# we will need to convert a lot of the 3+ and 4+ into percentages to end up working out wounds
# mathematically, for a 4+ this is done by (7- "4+") / 6  => which is 7-3 = 3 then 3/6 = 0.5. half chance,

def d6chance(d6plus_value):  # this line sets the name of the function and what parameters it will take later. the name you give the parameter is then used inside the function calculation

    d6percent_chance = (7 - d6plus_value) / 6  # <- here we do the above calculation on the d6plus_value i.e. 2+, 3+ or 4+ or 5+

    return d6percent_chance  # then we return the result, in this case a decimal chance, i.e. 0.5.


# Important note!! In python "indentation" is VERY important. the way Python knows what is inside the function and what is not, is by indentation. The same is try for most other sequences, so if, loops, try/except, etc.

# before we can do calculations we need to also make something to handle the strength toughness comparion:
def toWoundD6plus(strength, toughness):
    toWoundD6plus_value = 0
    if strength <= 2 * toughness:
        toWoundD6plus_value = 6
    elif strength < toughness:
        toWoundD6plus_value = 5
    elif strength == toughness:
        toWoundD6plus_value = 4
    elif strength > toughness:
        toWoundD6plus_value = 3
    elif strength >= 2 * toughness:
        toWoundD6plus_value = 2
    # now we return this value
    return toWoundD6plus_value


# now lets get serious. lets make a function to work out how much damage a weapon will do to a target.
def weaponWounds(firer, weapon, target):
    # Calculate number if wounds caused by weapon fired by firer on target

    # first need to calculate the decimal hit success chance:
    hit_d6plus = firer["BS"]  # here I've grabbed the value of the firer's BS
    hit_chance = d6chance(hit_d6plus)  # I've then converted this into a hit chance, using our function from before.

    # next calculate the decimal wound success chance
    wound_d6plus = toWoundD6plus(weapon["strength"], target["toughness"])  # you see how I'm feeding in the values. But it's all generic. So when you put the real values in i.e. set target to space marine and weapon to bolter, then it will flow through
    wound_chance = d6chance(wound_d6plus)

    # now calculate chance of FAILED save
    if target["save"] + weapon["ap"] < 7:  # the AP effectively adds to the save, to make it worse
        saveAfterAP = 7  # if it goes above 7 it will screw our percentages, so we make the max value it can take 7
    else:
        saveAfterAP = target["save"] + weapon["ap"]

    save_chance = 1 - d6chance(saveAfterAP)  # need to take it off one to get the chance of a failed save.

    attacks = 1  # need to program some way of working this out

    wounds = attacks * hit_chance * wound_chance * save_chance

    return wounds


# lets see how many wounds would an intercessor do to another?
intVsInt_wounds = weaponWounds(Intercessor, Intercessor["weapon"][0], Intercessor) #<- for the weapon section I've chosen the first weapon the intercessor is holding

print("wounds by an intercessor bolt rifle on an intercessor")
print(intVsInt_wounds)


# how many shots to kill another intercessor?
shots = 0

# we are going to use a while loop. This says whilst this condition is true, do this stuff:
while Intercessor["wounds"] > 0: # while intercessor wounds is greater than zero....
    # First we increment the number of shots
    shots = shots + 1  # or you can write shots += 1
    print("Shot number: " + str(shots))

    #then we calculate the wounds caused by the shot
    woundsByShot = intVsInt_wounds

    # then we subtract that from the intercessors wounds
    Intercessor["wounds"] = Intercessor["wounds"] - woundsByShot

    # then lets output the wounds remaining to watch it happen
    print("wounds remaining: " +str(Intercessor["wounds"]))
    print()
    #then we loop round again!


print("How many shots by an intercessor to kill an intercessor?")
print(shots)

#obviously the above seems a bit silly, but it would make more sense for some dynamic thing.
# for example if yous hot something that causes wounds back, and you had a degrading profile, then as this works
# it out stage by stage you could degrade the profile their BS would get worse and so require more shots etc.