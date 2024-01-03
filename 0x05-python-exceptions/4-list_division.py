#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    m = 0
    len_1 = len(my_list_1)
    len_2 = len(my_list_2)
    new_list = [0] * list_length
    try:
        for i in new_list:
            i = my_list_1[m] / my_list_2[m]
            if ZeroDivisionError:
                raise ZeroDivisionError("divison by 0")
            elif IndexError:
                raise IndexError("out of range")
            else:
                raise TypeError
    except IndexError:
        print("out of range")
    except ZeroDivisionError:
        print("divison by 0")
    except TypeError:
        print("wrong type")
    else:
        m = m + 1
    finally:
        return new_list


my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
