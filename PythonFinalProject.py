"""
PROBLEM 1
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
"""

ex_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

flatten_list = []


def flatter(l):
    for i in l:
        if type(i) == list:
            flatter(i)
        else:
            flatten_list.append(i)


flatter(ex_list)
print('Flattened List: ', flatten_list)

"""
PROBLEM 2
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

my_list = [[1, 2], [3, 4], [5, 6, 7]]


def reverse(ml):
    reversed_list = []
    for i in ml:
        if isinstance(i, list):
            reversed_list.append(reverse(i))
        else:
            reversed_list.append(i)
    reversed_list.reverse()
    return reversed_list


print("Reversed List: ", reverse(my_list))
