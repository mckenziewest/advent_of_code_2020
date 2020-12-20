#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:09:49 2020

@author: Mckenzie West

Advent of Code 2020: Day 11
"""

def load_and_clean(filename):
    with open(filename) as inputs:
        string_list = inputs.readlines()
    list_list = [list(row.replace("\n","").strip()) for row in string_list]
    return list_list

def get_adjacent(seat_row,seat_col,row_len,col_len):
    adjs = [(seat_row+i,seat_col+j) for i in [-1,0,1] for j in [-1,0,1]]
    adjs.remove((seat_row,seat_col))
    adjs = [(a,b) for a,b in adjs if a>=0 and b>=0 and a<row_len and b<col_len]
    return adjs

def fill_seats(seats_in):
    seats = [row.copy() for row in seats_in]
    num_rows = len(seats)
    num_cols = len(seats[0])
    for row in range(num_rows):
        for col in range(num_cols):
            if seats[row][col] == "L":
                adjs = get_adjacent(row,col,num_rows,num_cols)
                occupied = [(a,b) for a,b in adjs if seats_in[a][b] == "#"]
                if len(occupied) == 0:
                    seats[row][col] = "#"
    return seats

def empty_seats(seats_in):
    seats = [row.copy() for row in seats_in]
    num_rows = len(seats)
    num_cols = len(seats[0])
    for row in range(num_rows):
        for col in range(num_cols):
            if seats[row][col] == "#":
                adjs = get_adjacent(row,col,num_rows,num_cols)
                occupied = [(a,b) for a,b in adjs if seats_in[a][b] == "#"]
                if len(occupied) >= 4:
                    seats[row][col] = "L"
    return seats
    
def pretty_print(list_of_list):
    string_list = ["".join(row) for row in list_of_list]
    for row in string_list:
        print(row)
    
def solve_first(filename='input.txt'):
    ferry_seat = load_and_clean(filename)
    new_ferry_seat = fill_seats(ferry_seat)
    while any([ferry_seat[i][j] != new_ferry_seat[i][j] for i in range(len(ferry_seat)) for j in range(len(ferry_seat[0]))]):
        ferry_seat = [row.copy() for row in new_ferry_seat]
        new_ferry_seat = fill_seats(empty_seats(ferry_seat))
    return sum([row.count('#') for row in ferry_seat])
#print(solve_first())

def find_seat(row,col,rise,run,num_rows,num_cols,seats):
    for i in range(1,max(num_rows,num_cols)):
        a = i*rise
        b = i*run
        if row+a >= 0 and row+a<num_rows and col+b >= 0 and col+b < num_cols:
            if seats[row+a][col+b] == "#":
                return True
            elif seats[row+a][col+b] == "L":
                return False
    return False
    #return legal_pairs

test_ferry = load_and_clean('test.txt')

find_seat(0,0,1,1,10,10,test_ferry)


def fill_seats_second(seats_in):
    seats = [row.copy() for row in seats_in]
    num_rows = len(seats)
    num_cols = len(seats[0])
    for row in range(num_rows):
        for col in range(num_cols):
            if seats[row][col] == "L":
                directions = [(a,b) for a in [-1,0,1] for b in [-1,0,1] if a != 0 or b!=0]
                occupied = [find_seat(row,col,rise,run,num_rows,num_cols,seats_in) for rise,run in directions]
                if occupied.count(True) == 0:
                    seats[row][col] = "#"
    return seats
      
def empty_seats_second(seats_in):
    seats = [row.copy() for row in seats_in]
    num_rows = len(seats)
    num_cols = len(seats[0])
    directions = [(a,b) for a in [-1,0,1] for b in [-1,0,1] if a!= 0 or b!=0]
    for row in range(num_rows):
        for col in range(num_cols):
            if seats[row][col] == "#":
                if [find_seat(row,col,rise,run,num_rows,num_cols,seats_in) for rise,run in directions].count(True) >= 5 :
                    seats[row][col] = "L"

    return seats

def solve_second(filename="input.txt"):
    ferry_seat = load_and_clean(filename)
    new_ferry_seat = fill_seats_second(ferry_seat)
    while any([ferry_seat[i][j] != new_ferry_seat[i][j] for i in range(len(ferry_seat)) for j in range(len(ferry_seat[0]))]):
        ferry_seat = [row.copy() for row in new_ferry_seat]
        new_ferry_seat = fill_seats_second(empty_seats_second(ferry_seat))
    return sum([row.count('#') for row in ferry_seat])
                          
print(solve_second())
    