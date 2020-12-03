#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 3
"""
def load_and_clean(filename):
    with open(filename) as inputs:
        as_string = inputs.read()
    return as_string.strip().split('\n')
        
def tob_pos(slope_run,line):
    return slope_run * line

def first_solve(filename="input.txt",slope_run=3,slope_rise=1):
    tree_chart = load_and_clean(filename)
    count = 0
    n = len(tree_chart[0])
    for i in range(0,len(tree_chart),slope_rise):
        row = tree_chart[i]
        if row[tob_pos(slope_run,i//slope_rise) % n] == "#":
            count += 1
    return count

print(first_solve())

def second_solve(filename="input.txt",slopes=[(1,1),(3,1),(5,1),(7,1),(1,2)]):
    to_return = 1
    for x,y in slopes:
        trees = first_solve(filename,x,y)
        to_return *= trees
        print(trees)
    return to_return

print(second_solve())
