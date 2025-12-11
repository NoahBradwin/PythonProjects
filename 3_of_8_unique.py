def unique_probability():
    import random
    num_repetitions = 100000
    unique_count = 0
    for _ in range(num_repetitions):
        for i in range(3):
            nums = [random.randint(1, 8) for _ in range(3)]
            if len(set(nums)) == 3:
                unique_count += 1
    probability = unique_count / (num_repetitions * 3)
    return probability
def main():
    prob = unique_probability()
    print(f"Estimated Probability of all three numbers being unique: {prob}")
    print(f"Mathematical Probability: { (7/8) * (6/8) }")
if __name__ == "__main__":
    main()
