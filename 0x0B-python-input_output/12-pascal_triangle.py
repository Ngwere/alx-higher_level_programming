#!/usr/bin/python3
"""module for the pascal_triangle with the pascal_triangle() function"""


def pascal_triangle(n):
    my_list = []
    if n <= 0:
        return my_list
    for i in range(1, n):
        my_list.append(1)
        for j range(i):
           my_list.append(i)
    for i in range(num):  
          list1.append([])  
            list1[i].append(1)  
              for j in range(1, i):  
                      list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])  
                        if(num != 0):  
                                list1[i].append(1)
