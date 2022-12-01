elf_calorie_totals = []
current_elf_calorie_total = 0

with open("input.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            elf_calorie_totals.append(current_elf_calorie_total)
            current_elf_calorie_total = 0
        else:
            current_elf_calorie_total += int(line.strip())

print(max(elf_calorie_totals))
print(sum(sorted(elf_calorie_totals)[-3:]))

