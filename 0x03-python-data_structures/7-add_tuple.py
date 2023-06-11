#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lt_1 = []
    lt_2 = []
    for num in range(len(tuple_a)):
        lt_1.append(tuple_a[num])
    for num in range(len(tuple_b)):
        lt_2.append(tuple_b[num])
    while len(lt_1) < 2 or len(lt_2) < 2:
        lt_1.append(0)
        lt_2.append(0)
    return(lt_1[0]+lt_2[0], lt_1[1]+lt_2[1])
