#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 6
"""

import string

def load_and_clean(filename):
    with open(filename) as inputs:
        string_list = inputs.read()
    return string_list[:-1].split("\n\n")

def get_counts(group):
    group_yes = ""
    for letter in string.ascii_lowercase:
        if letter in group:
            group_yes += letter
    return len(group_yes)

def solve_one(filename="input.txt"):
    all_groups = load_and_clean(filename)
    counts = [get_counts(group) for group in all_groups]
    return sum(counts)

print(solve_one())

def get_counts_consensus(group):
    group_list = group.split("\n")
    group_yes = ""
    for letter in string.ascii_lowercase:
        if all([letter in person for person in group_list]):
            group_yes += letter
    return len(group_yes)
    
def solve_two(filename="input.txt"):
    all_groups = load_and_clean(filename)
    counts = [get_counts_consensus(group) for group in all_groups]
    return sum(counts)   

print(solve_two())

load_and_clean("input.txt")[-1][-1]
    

