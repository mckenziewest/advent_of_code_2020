#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 8
"""
import string

def load_and_clean(filename):
    with open(filename) as inputs:
        string_list = inputs.readlines()
    return string_list

def process_command(cmd,pos,acc):
    cmd=cmd.split()
    if cmd[0] == "nop":
        return pos+1, acc
    elif cmd[0] == "jmp":
        return pos+int(cmd[1]), acc
    else:
        return pos+1, acc+int(cmd[1])
    
print(process_command('jmp -99',0,0))

def solve_one(filename='input.txt'):
    cmd_list = load_and_clean(filename)
    pos = 0
    acc = 0
    locations = []
    while pos not in locations:
        locations.append(pos)
        pos, acc = process_command(cmd_list[pos],pos,acc)
    return acc

print(solve_one('test.txt'))
print(solve_one())

def is_loop(cmd_list):
    pos = 0
    acc = 0
    locations = []
    while pos not in locations and pos < len(cmd_list):
        locations.append(pos)
        pos, acc = process_command(cmd_list[pos],pos,acc)
    return pos == len(cmd_list), acc

def solve_second(filename='input.txt'):
    cmd_list = load_and_clean(filename)
    for i in range(len(cmd_list)):
        if cmd_list[i].startswith('acc'):
            next
        new_list = cmd_list.copy()
        if cmd_list[i].startswith('nop'):
            new_list[i] = new_list[i].replace('nop','jmp')
        elif cmd_list[i].startswith('jmp'):
            new_list[i] = new_list[i].replace('jmp','nop')
        made_it, acc = is_loop(new_list)
        if made_it:
            print(i)
            return acc
    return None

print(solve_second())
            
    
