

def load_rucksacks():
    with open("input.txt", "r") as f:
        rucksacks = [line.strip() for line in f]
    return rucksacks


def compartmentalise(rucksack):
    midpoint = len(rucksack) // 2
    return (rucksack[:midpoint], rucksack[midpoint:])


def intersection(xs):
    return set.intersection(*(set(x) for x in xs))


def get_priority(item):
    if "a" <= item <= "z":
        return ord(item) - 96 # lowercase: 'a' is 97, want 'a' -> 1; 97 - 1 = 96
    return ord(item) - 38     # uppercase: 'A' is 65, want 'A' -> 27; 65 - 27 = 38


def group(rucksacks):
    return[rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]



def main():
    rucksacks = load_rucksacks()

    priority_sum_1 = sum(get_priority(duplicate) for rucksack in rucksacks for duplicate in intersection(compartmentalise(rucksack)))
    print(f"Task 1: {priority_sum_1}")

    priority_sum_2 = sum(get_priority(duplicate) for group in group(rucksacks) for duplicate in intersection(group))
    print(f"Task {2}: {priority_sum_2}")


if __name__ == "__main__":
    main()