#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    k = 0
    ret = []
    while k < list_length:
        res = 0
        try:
            res = my_list_1[k] / my_list_2[k]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            ret.append(res)
            k += 1
    return ret
