#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 4
"""
def load_and_clean(filename):
    with open(filename) as inputs:
        as_string = inputs.read()
    return as_string.strip().split('\n\n')

def create_pass(entry):
    linesplit = entry.split('\n')
    all_split = []
    for val in linesplit:
        all_split += val.split()
    pairs = [ val.split(":") for val in all_split]
    return dict(pairs)

def check_pass_legal(passport):
    legal_needs = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    return all([a in passport.keys() for a in legal_needs])




def solve_one(filename='input.txt'):
    entry_string = load_and_clean(filename)
    list_of_dicts = [create_pass(e) for e in entry_string]
    num_ok = len([a for a in list_of_dicts if check_pass_legal(a)])
    return num_ok

def verify_byr(passport):
    byr = int(passport['byr'])
    return 1920 <= byr and 2002 >= byr

def verify_iyr(passport):
    iyr = int(passport['iyr'])
    return 2010 <= iyr and 2020 >= iyr

def verify_eyr(passport):
    eyr = int(passport['eyr'])
    return 2020 <= eyr and 2030 >= eyr

def verify_hgt(passport):
    try: hgt = int(passport['hgt'][:-2])
    except: 
        print(passport['hgt'])
        return False
    hgt_scale = passport['hgt'][-2:]
    if hgt_scale == 'cm':
        return hgt >= 150 and hgt <= 193
    elif hgt_scale == 'in':
        return hgt >= 59 and hgt <= 76
    else:
        return False

def verify_hcl(passport):
    hcl = passport['hcl']
    if hcl[0] != '#' or len(hcl) != 7:
        return False
    for i in range(1,7):
        if hcl[i] not in '0123456789abcdef':
            return False
    return True

def verify_ecl(passport):
    ecl = passport['ecl']
    return ecl in ['amb','blu','brn','gry','grn','hzl','oth']

def verify_pid(passport):
    pid = passport['pid']
    if len(pid) != 9:
        return False
    try:
        int(pid)
        return True
    except:
        return False


def solve_two(filename='input.txt'):
    entry_string = load_and_clean(filename)
    list_of_dicts = [create_pass(e) for e in entry_string]
    have_entries = [a for a in list_of_dicts if check_pass_legal(a)]
    funcs = [verify_byr,verify_iyr,verify_eyr,verify_hgt,verify_hcl,verify_ecl,verify_pid]
    valid = []
    for passport in have_entries:
        if all([func(passport) for func in funcs]):
            valid.append(passport)
    return len(valid)

print(solve_two())

verify_pid({'pid':'000000001'})
