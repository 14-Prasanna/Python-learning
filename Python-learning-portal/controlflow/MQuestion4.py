total = int(input())
rabbits = int(input())
deer = int(input())
birds = int(input())
squirrels = int(input())
counted = rabbits + deer + birds + squirrels
if counted != total:
    print("Counted wrongly")
elif counted == total:
    print("Baby lion is well behaved")
else:
    print("Baby lion is mischievous")