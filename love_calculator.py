
def love_calculator(name_1: str, name_2: str):

    true_love_list = ["t", "r", "u", "e", "l", "o", "v", "e"]
    name_1_sum = 0
    name_2_sum = 0

    for i in true_love_list:

        name_1_count = name_1.count(i)
        name_2_count = name_2.count(i)
        print(f"the letter {i.upper()} appears {name_1_count + name_2_count} times")
        name_1_sum += name_1_count
        name_2_sum += name_2_count

    result = name_1_sum + name_2_sum
    print(f"your score is {result}")


love_calculator(name_1="sean crazz", name_2="tal kuriel")
