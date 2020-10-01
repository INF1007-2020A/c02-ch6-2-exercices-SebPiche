#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_even_keys(dictionary):
	# return {k for k, v in dictionary.items() if k%2 == 0}
	return {k for k in dictionary.keys() if k%2 == 0}

	# keys = {}
	# for k, v in dictionary.items():
	# 	if k%2 == 0:
	# 		keys.add(k)
	# return keys

def join_dictionaries(dictionaries):
	# result = {}
	# for elem in dictionaries:
	# 	result.update(elem)
	# return result

	# result={}
	# for d in dictionaries:
	# 	for key, value in d:
	# 		result += (key, value)
	# return result
	return {keys: value
			for d in dictionaries
				for keys, value in d.items()
			}

def dictionary_from_lists(keys, values):
	# result = {}
	# for i in range(min(len(keys), len(values))):
	# 	result[keys[i]] = values[i]
	# return result
	# return {keys[i]: values[i] for i in range(min(len(keys), len(values)))}
	return dict(zip(keys, values))
def get_greatest_values(dictionary, num_values):
	#Extraire les valeurs
	# vals = [v for k, v in dictionary.items()]
	# vals = list(dictionary.values())
	#Ordonner les valeurs
	# vals.sort()
	# vals = sorted(vals, reverse=True)
	#Choisir les num_values plus grands
	return sorted(dictionary.values(), reverse=True)[0:num_values]

def get_sum_values_from_key(dictionaries, key):
	#Extraire les valeurs associes a une cle
	#Faire la somme des valeurs
	# sum = 0
	# for d in dictionaries:
	# 	if key in d:
	# 		sum += d[key]
	# return sum
	# values =[]
	# for d in dictionaries:
	# 	if key in d:
	# 		values.append(d[key])
	# return sum(values)
	return sum(d[key] for d in dictionaries if key in d)


if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print( "--" * 20)

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print( "--" * 20)
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print( "--" * 20)
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print( "--" * 20)

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print( "--" * 20)
