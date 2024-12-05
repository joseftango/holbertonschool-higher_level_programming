#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_of_results = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            list_of_results.append(res)
        except (TypeError, TypeError):
            print('wrong type')
            list_of_results.append(0)
        except ZeroDivisionError:
            print('division by 0')
            list_of_results.append(0)
        except IndexError:
            print('out of range')
            list_of_results.append(0)
        finally:
            pass
    return list_of_results
