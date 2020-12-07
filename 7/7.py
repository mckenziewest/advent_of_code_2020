#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 7
"""


def load_and_clean(filename):
    with open(filename) as inputs:
        string_list = inputs.readlines()
    return string_list

def get_containment(bag):
    sep_contain = bag.split("contain",1)
    container = sep_contain[0].replace("bags","").strip()
    contents = sep_contain[1].replace(" bags","").replace(" bag","").replace(".","").strip()
    contents = contents.split(", ")
    color = [val.split(" ",1)[1] for val in contents]
    number = [val.split(" ",1)[0] for val in contents]
    zipped_contents = dict(zip(color,number))
    return container, zipped_contents

def can_hold(bag_list,little_spoon):
    holders = []
    for pair in bag_list:
        if little_spoon in pair[1].keys():
            holders.append(pair[0])
    count = 0
    last_count = -1
    while last_count < count:
        last_count = count
        count = 0
        for pair in bag_list:
            for holder in holders:
                if holder in pair[1].keys():
                    if pair[0] not in holders:
                        holders.append(pair[0])
                else:
                    count += 1

    return holders

def solve_one(filename = "input.txt", little_spoon="shiny gold"):
    requirement_list = load_and_clean(filename)
    bag_list = [get_containment(bag) for bag in requirement_list]
    return len(can_hold(bag_list,little_spoon))
print(solve_one())

def get_num_contained(bag_list,big_spoon):
    for bag, sub_bags in bag_list:
        if bag == big_spoon:
            val = 1
            for sub in sub_bags.keys():
                if sub != "other":
                    val += int(sub_bags[sub])*get_num_contained(bag_list,sub)
            return val

def solve_two(filename = "input.txt", big_spoon = "shiny gold"):
    requirement_list = load_and_clean(filename)
    bag_list = [get_containment(bag) for bag in requirement_list]
    return get_num_contained(bag_list,big_spoon)-1
    
print(solve_two())

