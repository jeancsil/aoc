def part1():
    with open('./data/adv1.txt', 'r') as f:
        most_calories = -1
        elf_with_most_calories = -1
        current_calories = 0

        elf_number = 1
        for row, line in enumerate(f.readlines()):
            line = line.strip()
            #print("Elf number " + str(elf_number))
            #print(line)
            if line:
                current_calories = current_calories + int(line)
            else:
                #print("Elf {} carrying {} calories".format(elf_number, current_calories))
                if current_calories >= most_calories:
                    most_calories = current_calories
                    elf_with_most_calories = elf_number

                current_calories = 0
                elf_number = elf_number + 1

        print("The elf carrying the most number of calories is Elf #{} which is carrying a total of {} calories".format(
            elf_with_most_calories, most_calories))


def part2():
    with open('./data/adv1.txt', 'r') as f:
        current_calories = 0
        count_calories = {}
        elf_number = 1
        for row, line in enumerate(f.readlines()):
            line = line.strip()
            if line:
                current_calories = current_calories + int(line)
            else:
                #print("Elf #{} is carrying {} calories".format(elf_number, current_calories))
                count_calories[elf_number] = current_calories
                current_calories = 0
                elf_number = elf_number + 1

        #print(count_calories)
        sorted_calories = sorted(count_calories.values(), reverse=True)
        top_3 = sorted_calories[0] + sorted_calories[1] + sorted_calories[2]
        print("The top 3 elves carrying the most calories are carrying: {} calories".format(top_3))


if __name__ == '__main__':
    part1()
    part2()
