#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Auther: ZhengZhong,Jiang

def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] < data[j+1]:
            j += 1
        if tmp < data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp

def heapsort(data):
    n = len(data)
    # 建堆
    for i in range(n//2 - 1, -1, -1):
        sift(data, i, n - 1)
    # 
    for i in range(n - 1, -1, -1):
        data[0], data[i] = data[i], data[0]
        sift(data, 0, i - 1)
    print(data)

data = [7, 0, 1, 6, 2, 5, 8, 3, 4, 9]
heapsort(data)
