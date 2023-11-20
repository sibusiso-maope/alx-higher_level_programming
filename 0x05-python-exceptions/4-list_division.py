#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    m_list = []
    for k in range(list_length):
        try:
            divide = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            m_list.append(divide)
    return (m_list)
