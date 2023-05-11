from random import randint

def randomDie():
#    Random number 1-6
   dieOne = randint(1,6)
   dieTwo = randint(1,6)
#    roll is a list of the random numbers
   roll = [dieOne,dieTwo]
#    sum is a built in function that sums a lists values
   total = sum(roll)
#    return roll and total as a tuple
   return (roll, total)
# calling randomDie and destructing with roll and total
roll,total = randomDie()

if roll[0] is roll[1]:
    print("=")
print(roll,total)