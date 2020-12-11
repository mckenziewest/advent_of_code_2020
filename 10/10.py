#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 10
"""


from time import time
from functools import lru_cache


def load_and_clean(filename):
    with open(filename) as inputs:
        string_list = inputs.readlines()
    return string_list


def solve_first(filename='input.txt'):
    number_list = [int(a) for a in load_and_clean(filename)]
    number_list.append(0)
    number_list.sort()
    number_list.append(number_list[-1]+3)
    diffs = [number_list[i]-number_list[i-1] for i in range(1,len(number_list))]
    threes = diffs.count(3)
    ones = diffs.count(1)
    return threes*ones
print(solve_first())


@lru_cache(maxsize=None)
def num_next(voltage_list,value):
    voltage_list = list(voltage_list)
    if value >= max(voltage_list):
        return 1
    else:
        a, b, c = (0,0,0)
        if value+1 in voltage_list:
            a = num_next(tuple(voltage_list),value+1)
        if value+2 in voltage_list:
            b = num_next(tuple(voltage_list),value+2)
        if value+3 in voltage_list:
            c = num_next(tuple(voltage_list),value+3)
        return a+b+c

def solve_second(filename='input.txt'):
    voltage_list = (int(a) for a in load_and_clean(filename))
    return num_next(voltage_list,0)

start = time()
print(solve_second())
print(time() - start)

def let_me_cache(filename = 'input.txt'):
    voltage_list = [int(a) for a in load_and_clean(filename)]
    voltage_list.append(0)
    voltage_list.sort()
    voltage_list.reverse()
    cum_follows = {max(voltage_list):1}
    for i in voltage_list[1:]:
        cum_follows[i] = sum([cum_follows[j] for j in range(i+1,i+4) if j in voltage_list])
    return cum_follows[0]

start = time()
print(let_me_cache())
print(time() - start)
