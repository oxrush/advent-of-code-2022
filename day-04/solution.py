def read_file():
    lines = []
    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    return lines



def parse(lines):
    pairs = []
    for line in lines:
        elves = line.split(",")
        elf1 = elves[0].split("-")
        elf2 = elves[1].split("-")
        pair = (
            (int(elf1[0]), int(elf1[1])),
            (int(elf2[0]), int(elf2[1]))
        )
        pairs.append(pair)
    return pairs


def fully_contains(range1, range2):
    (start1, end1) = range1
    (start2, end2) = range2
    return start2 >= start1 and end2 <= end1


def overlap(range1, range2):
    (start1, end1) = range1
    (start2, end2) = range2
    return start1 <= end2 and start2 <= end1


def main():
    pairs = parse(read_file())

    result1 = sum(1 for elf1, elf2 in pairs if fully_contains(elf1, elf2) or fully_contains(elf2, elf1))
    print(result1)

    result2 = sum(1 for elf1, elf2 in pairs if overlap(elf1, elf2))
    print(result2)


if __name__ == "__main__":
    main()