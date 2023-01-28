def gen_powerset(items):
    
    powerset = [[]]
    for item in items:
        subset = []
        for i in powerset:
            subset.append(i + [item])
        powerset.extend(subset)
    return powerset


def calculate_weight(knapsack):
    return sum([w for w, _ in knapsack])


def calculate_price(knapsack):
    return sum([p for _, p in knapsack])


def get_mvk(solutions):
    # most valuable knapsack
    sol = []
    max_price = float("-Inf")
    for knapsack in solutions:
        total_price = calculate_price(knapsack)
        if total_price > max_price:
            sol = knapsack
    return sol


def exercise1():
    weights = [12, 23, 11, 15, 7]
    prices = [103, 60, 70, 5, 15]
    max_sack = 100
    items = list(zip(weights, prices))
    powerset = gen_powerset(items)

    candidate_solutions = []
    for knapsack in powerset:
        if calculate_weight(knapsack) <= max_sack:
            candidate_solutions.append(knapsack)

    solution = get_mvk(candidate_solutions)
    print(f"La solución a este problema de la mochila es {solution}")
    print(f"El peso total de lamochila es de {calculate_weight(solution)}")


def usar_la_fuerza(knapsack, item, counter=0):
    if len(knapsack) == 0:
        return False, counter
    if knapsack[0] == item:
        return True, counter
    else:
        return usar_la_fuerza(knapsack[1:], item, counter + 1)





def main():
    exercise1()
    

if __name__ == "__main__":
    main()
