#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 4
"""

import numpy as np

def load_and_clean(filename):
    with open(filename) as inputs:
        string_list = inputs.readlines()
    return string_list

def turn_binary(seat):
    row = seat[:7]
    col = seat[7:]
    row = row.replace("B","1")
    row = row.replace("F","0")
    col = col.replace("R","1")
    col = col.replace("L","0")
    return int(row,2),int(col,2)


def get_seat_id(string_seat):
    row, col = turn_binary(string_seat)
    return row*8+col

def solve_one(filename = "input.txt"):
    seat_list = load_and_clean(filename)
    all_seats = []
    for seat in seat_list:
        all_seats.append(get_seat_id(seat))
    return np.array(all_seats).max()

print(solve_one())

def solve_two(filename = "input.txt"):
    nums = [a for a in range(128*8)]
    seat_list = load_and_clean(filename)
    for seat in seat_list:
        nums.pop(nums.index(get_seat_id(seat)))
    for seat in nums:
        if seat-1 not in nums and seat+1 not in nums:
            return seat

print(solve_two())
    

