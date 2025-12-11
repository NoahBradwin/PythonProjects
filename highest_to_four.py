def compute_mathematically():
    return 1/3 * 4 + 1/6 * 5 + 1/2 * 6

def find_wait_time():
    num_iterations = 1000000
    import random
    num_rolls_total = 0
    highest_total = 0
    for i in range(num_iterations):
        rolls = []
        num_rolls = 0
        while True:
            roll_dice = random.randint(1,6)
            rolls.append(roll_dice)
            num_rolls += 1
            if roll_dice == 4:
                break
        num_rolls_total += num_rolls
        highest = max(rolls)
        highest_total += highest
    return num_rolls_total / num_iterations, highest_total / num_iterations
def main():
    average_wait, average_highest_roll = find_wait_time()
    math_highest = compute_mathematically()
    print(f"Mathematical expected highest roll before rolling a 4: {math_highest}")
    print(f"Average number of rolls before rolling a 4: {average_wait}")
    print(f"Average highest roll: {average_highest_roll}")
if __name__ == "__main__":
    main()

            