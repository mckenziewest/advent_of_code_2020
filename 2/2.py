#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 2
"""
def load_and_clean(filename):
    with open(filename) as inputs:
        as_string = inputs.read()
    pass_with_requirement = []
    for line in as_string.strip().split('\n'):
        line = line.strip()
        requirement, password = tuple(line.split(": ",1))
        minmax, letter = tuple(requirement.split())
        min_ok,max_ok = tuple(minmax.split("-"))
        min_ok = int(min_ok)
        max_ok = int(max_ok)
        pass_with_requirement.append(((min_ok,max_ok,letter),password))
    return pass_with_requirement
        
def num_legal_passwords(pass_list):
    count = 0
    for row in pass_list:
        num_letter = row[1].count(row[0][2])
        if row[0][0] <= num_letter and row[0][1] >= num_letter:
            count +=1
    return count

def solve_first(filename="input.txt"):
    pass_list = load_and_clean(filename)
    return num_legal_passwords(pass_list)

def num_legal_passwords_take_two(pass_list):
    count = 0
    for row in pass_list:
        pos1 = row[0][0]-1
        pos2 = row[0][1]-1
        letter = row[0][2]
        atpos1 = row[1][pos1] == letter and row[1][pos2] != letter
        atpos2 = row[1][pos1] != letter and row[1][pos2] == letter
        if atpos1 or atpos2:
            count +=1
    return count

def solve_second(filename="input.txt"):
    pass_list = load_and_clean(filename)
    return num_legal_passwords_take_two(pass_list)

print(solve_second())