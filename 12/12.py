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
    list_list = [(row[0],int(row[1:])) for row in string_list]
    return list_list

def follow_direction(location,facing,direction):
    if direction[0] == "N":
        location[1] += direction[1]
    elif direction[0] == "S":
        location[1] -= direction[1]
    elif direction[0] == "E":
        location[0] += direction[1]
    elif direction[0] == "W":
        location[0] -= direction[1]
    elif direction[0] == "L":
        facing = (facing + direction[1]//90) %4 
    elif direction[0] == "R":
        facing = (facing - direction[1]//90) %4 
    elif direction[0] == "F":
        dirs = ["E","N","W","S"]
        location, facing = follow_direction(location,facing,(dirs[facing],direction[1]))
    return location, facing

def solve_one(filename="input.txt",location=[0,0],facing=0):
    direction_list = load_and_clean(filename)
    for direction in direction_list:
        location, facing = follow_direction(location,facing,direction)
    return abs(location[0])+abs(location[1])

print(solve_one())


def follow_direction_two(location,waypoint,direction):
    if direction[0] in "NSEW":
        waypoint = follow_direction(waypoint,0,direction)[0]
    elif direction[0] in "RL":
        amount_rotation = direction[1]//90 % 4
        slope = [waypoint[i]-location[i] for i in [0,1]]
        if amount_rotation == 2:
            slope = [c*-1 for c in slope]
        elif amount_rotation == 1:
            slope.reverse()
            if direction[0] == "R":
                slope[1] = -1*slope[1]
            else:
                slope[0] = -1*slope[0]
        elif amount_rotation == 3:
            slope.reverse()
            if direction[0] == "L":
                slope[1] = -1*slope[1]
            else:
                slope[0] = -1*slope[0]
        waypoint = [location[i] + slope[i] for i in [0,1]]
    elif direction[0] == "F":
        moves = direction[1]
        slope = [waypoint[i]-location[i] for i in [0,1]]
        location = [location[i]+slope[i]*moves for i in [0,1]]
        waypoint = [location[i]+slope[i] for i in [0,1]]
    return location, waypoint

def solve_two(filename="input.txt",location=[0,0],waypoint=[10,1]):
    direction_list = load_and_clean(filename)
    for direction in direction_list:
        slope = [waypoint[i]-location[i] for i in [0,1]]
        print(location,slope,direction)
        location, waypoint = follow_direction_two(location,waypoint,direction)
    return abs(location[0])+abs(location[1])

print(solve_two())

loc,way = follow_direction_two([-10,-4],[10,1],("L",180))
follow_direction_two(loc,way,("F",10))