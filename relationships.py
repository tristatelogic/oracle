#!/usr/bin/env python3
import random

# This is the structure that carries me
template = "The {color} {noun} is your {relation}"

# These are the colors of the world
colors = [
    "brown",
    "yellow",
    "gold",
    "silver",
    "red",
    "blood red",
    "white",
    "grey",
    "gray",
    "grey",
    "gray",
    "grey",
    "yellow",
    "white",
    "blue",
    "green",
    "blue-green",
    "red-orange",
]

# These are the things that can be
nouns = [
    "cow",
    "machine",
    "computer",
    "robot",
    "cat",
    "person",
    "animal",
    "monster",
    "ocean",
    "sky",
    "pilgrim",
    "animal",
    "holiday",

]

# These are the ways we connect with each other
relations = [
    "friend",
    "acquaintence",
    "relative",
    "father",
    "friend",
    "lover",
    "enemy",
]

poem = template.format(
    color=random.choice(colors),
    noun=random.choice(nouns),
    relation=random.choice(relations),
)

print(poem)

# When you find me, what will you say?
