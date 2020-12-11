#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 8
"""


def load_and_clean(filename):
    with open(filename) as inputs:
        string_list = inputs.readlines()
    return string_list


def solve_first(filename='input.txt',prev=25):
    number_list = [int(a) for a in load_and_clean(filename)]
    for index in range(prev,len(number_list)):
        last25 = number_list[index-prev:index]
        sums = [last25[i]+last25[j] for i in range(prev) for j in range(i+1,prev)]
        if number_list[index] not in sums:
            return number_list[index]
print(solve_first())

def solve_second(filename='input.txt',prev=25):
    invalid = solve_first(filename,prev)
    number_list = [int(a) for a in load_and_clean(filename)]
    for j in range(2,len(number_list)):
        for i in range(len(number_list)-j):
            test_list = number_list[i:i+j]
            if sum(test_list) == invalid:
                return max(test_list) + min(test_list)
print(solve_second())