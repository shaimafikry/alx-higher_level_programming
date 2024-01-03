#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    m = 0
    new_list = [0] * list_length
    try:
        for i, r in zip(my_list_1, my_list_2):
            if r == 0:
                print("division by 0")
            elif isinstance(i, (int, float)) and isinstance(r, (int, float)):
                new_list[m] = i / r
            else:
                print("wrong type")
            m = m + 1
        if len(my_list_1) != len(my_list_2):
            raise IndexError
    except IndexError:
        print("out of range")
    finally:
        return new_list


# my_l_1 = [10, 8, 4]
# my_l_2 = [2, 4, 4]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)

# print("--")

# my_l_1 = [10, 8, 4, 4]
# my_l_2 = [2, 0, "H", 2, 7]
# result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
# print(result)
