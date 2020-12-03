#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: westmr
"""

def load_and_clean(filename):
    with open(filename) as inputs:
        as_string = inputs.read()
    int_list = [int(a) for a in as_string.split('\n') if len(a)>0]
    return int_list

def get_pair_sum(a_list,desired_sum):
    for a in a_list:
        if desired_sum-a in a_list:
            return a

def prod_with_diff(a,given_sum):
    return a*(given_sum-a)

def solve_first(filename="ints.txt",year=2020):
    int_list = load_and_clean(filename)
    val = get_pair_sum(int_list,year)
    return prod_with_diff(val,year)

print(solve_first())