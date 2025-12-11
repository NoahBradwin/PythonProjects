def compute_math():
    sum_prob = 0
    for i in range(1,49):
        prod = 1
        for j in range(1,i):
            term = (49 - j) / (53 - j)
            prod *= term
        prob = prod * (4 / (53 - i))
        sum_prob += prob * i
    return sum_prob
def compute_monte():
    import random
    num_iterations = 1000000
    population = list(range(1,53))
    k = 52
    # aces are one two three and four
    aces = [1, 2, 3, 4]
    total_ace_position = 0
    for _ in range(num_iterations):
        random_list = random.sample(population, k)
        ace_position = 0
        for i in range(1, 53):
            if random_list[i - 1] in aces:
                ace_position = i
                total_ace_position += ace_position
                break
    return total_ace_position / num_iterations
def main():
    math_result = compute_math()
    monte_result = compute_monte()
    print(f"Mathematical Expectation: {math_result}")
    print(f"Monte Carlo Simulation: {monte_result}")
if __name__ == "__main__":
    main()