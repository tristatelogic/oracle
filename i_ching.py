#!/usr/bin/env python3
import random

coin = ['H', 'T']
dish = []
paper = []
memory = []

def toss():
    dish.append(random.choice(coin))

def toss_three():
    toss()
    toss()
    toss()

def read_dish():
    total = 0
    for coin in dish:
        total += 3 if coin == 'H' else 2
    memory.append(total)

def write_line():
    total = memory[-1]
    if total == 6:
        line = "-X-"
    elif total == 7:
        line = "- -"
    elif total == 8:
        line = "---"
    elif total == 9:
        line = "-ϴ-"
    else:
        print("A miracle has occurred.")
        import sys; sys.exit()

    paper.insert(0, line)

def clear_dish():
    while dish:
        for x in dish:
            dish.remove(x)

def cast():
    for _ in range(6):
        toss_three()
        read_dish()
        write_line()
        clear_dish()

def print_hexagram():
    for line in paper:
        print(line)

cast()
print_hexagram()
