#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 12
"""


def load_and_clean(filename):
    with open(filename) as inputs:
        string_list = inputs.readlines()
    string_list[1] = [int(val) for val in string_list[1].split(",") if val != 'x']
    string_list[0] = int(string_list[0])
    return string_list

def solve_one(filename='input.txt'):
    inputs = load_and_clean(filename)
    mods = [bus - inputs[0] % bus for bus in inputs[1]]
    wait = min(mods)
    bus_index = mods.index(wait)
    print(inputs)
    print(mods)
    return wait*inputs[1][bus_index]

#print(solve_one())


def load_and_clean_two(filename):
    with open(filename) as inputs:
        string_list = inputs.readlines()
    string_list[1] = string_list[1].replace('\n','')
    return string_list[1].split(",")

import math

def list_gcd(int_list):
    my_gcd = math.gcd(int_list[0],int_list[1])
    for i in int_list[2:]:
        my_gcd = math.gcd(my_gcd,i)
    return my_gcd

def lcm(int_list):
    prod = 1
    for i in int_list:
        prod *= i
    return abs(prod) // list_gcd(int_list)

def Euclidean_algorithm(a, b):  
    if a == 0 :   
        return b, 0, 1           
    gcd, x1, y1 = Euclidean_algorithm(b%a, a)    
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd, x, y   
    
def solve_two(filename="input.txt"):
    busses = load_and_clean_two(filename)
    live_buses = [int(bus) for bus in busses if bus != 'x']
    diffs = [(busses.index(str(bus)))%bus for bus in live_buses]
    L = lcm(live_buses)
    s_list = [Euclidean_algorithm(bus,L//bus)[2] for bus in live_buses]
    crt = sum([-diffs[i]*s_list[i]*L//live_buses[i] for i in range(len(live_buses))])
    assert all([(crt+diffs[i])%live_buses[i] == 0 for i in range(len(live_buses))])

    return crt % L
        
print(solve_two("test.txt"))

    