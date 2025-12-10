import random
def main():
    num_iterations = 1000000
    good_sets = 0
    for i in range (num_iterations):
        rolls = set()
        while len(rolls) < 3:
            roll_dice = random.randint(1,6)
            rolls.add(roll_dice)
        valid = False
        if rolls.issubset((2,4,6)):
            valid = True
        if valid == True:
            good_sets += 1
    print(good_sets/num_iterations)

if __name__ == "__main__":
    main()

