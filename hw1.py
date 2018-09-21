#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import re

def histogram_times(filename):
    times = [0] * 24
    with open(filename, 'r') as file:
        data = list(csv.reader(file))
        for crash in data[1:]:
            if not crash[1] == "":
                # time could be in form HH.MM, HH:MM, HH'MM, H:MM, or HHMM
                time_str = re.search("[0-9]{1,2}(?=[:'.]*[0-9]{2})", crash[1]).group(0)
                times[int(time_str)] += 1
    return times

def weigh_pokemons(filename, weight):
    same_weight = []
    with open(filename, 'r') as file:
        json_file = json.load(file)
        for pokemon in json_file['pokemon']:
            # cut off " kg" suffix
            pokemon_weight = float(pokemon['weight'][:-3])
            if pokemon_weight == weight:
                same_weight.append(pokemon['name'])
    return same_weight

def single_type_candy_count(filename):
    candy_count = 0
    with open(filename, 'r') as file:
        json_file = json.load(file)
        for pokemon in json_file['pokemon']:
            if 'candy_count' in pokemon and len(pokemon['type']) == 1:
                candy_count += pokemon['candy_count']
    return candy_count

def reflections_and_projections(points):
    #1 reflect point about y = 1
    arr1 = points - 1
    arr1 = np.array([[1, 0], [0, -1]]) @ arr1
    arr1 = arr1 + 1
    #2 rotate points pi/2 about origin
    arr2 = np.array([[0, -1], [1, 0]]) @ arr1
    #3 projects points onto line y=3x
    m = 3
    arr3 = np.array([[1, m], [m, m ** 2]]) @ arr2
    arr3 = arr3 * (1 / (m ** 2 + 1))
    return arr3

def normalize(image):
     max = np.max(image)
     min = np.min(image)
     return (image - min) * (255 / (max - min))

def sigmoid_normalize(image, a):
    return 255 / (1 + np.exp(-(image - 128) / a))

# print(histogram_times("airplane_crashes.csv"))
# print(weigh_pokemons("pokedex.json", 10))
# print(single_type_candy_count("pokedex.json"))
# print(reflections_and_projections(np.array([[0], [1]])))
# print(normalize(np.random.random((32, 32))))
# print(sigmoid_normalize(np.random.random((32, 32)), 128))