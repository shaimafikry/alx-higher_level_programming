#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    m = 0
    new_list = [0] * list_length
    for i in range(list_length):
        try:
            new_list[i] = my_list_1[m] / my_list_2[m]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("divison by 0")
        except TypeError:
            print("wrong type")
        finally:
            m = m + 1
    return new_list
