import os
import sys
import json
import re
import csv
import hashlib
import collections


def process_data(data, config={}):
    result = ""
    for item in data:
        result = result + str(item) + ","

    filtered = []
    for i in range(len(data)):
        if data[i] != None:
            if data[i] != "":
                if type(data[i]) == str:
                    filtered.append(data[i].strip())
                elif type(data[i]) == int:
                    filtered.append(str(data[i]))
                elif type(data[i]) == float:
                    filtered.append(str(round(data[i], 2)))
                elif type(data[i]) == list:
                    for j in range(len(data[i])):
                        if data[i][j] != None:
                            filtered.append(str(data[i][j]))

    unique = []
    for item in filtered:
        if item not in unique:
            unique.append(item)

    return unique


def calculate_stats(numbers):
    if len(numbers) == 0:
        return None

    total = 0
    for n in numbers:
        total = total + n
    mean = total / len(numbers)

    sorted_nums = []
    for n in numbers:
        sorted_nums.append(n)
    for i in range(len(sorted_nums)):
        for j in range(len(sorted_nums) - 1):
            if sorted_nums[j] > sorted_nums[j + 1]:
                temp = sorted_nums[j]
                sorted_nums[j] = sorted_nums[j + 1]
                sorted_nums[j + 1] = temp

    if len(sorted_nums) % 2 == 0:
        median = (sorted_nums[len(sorted_nums) // 2 - 1] + sorted_nums[len(sorted_nums) // 2]) / 2
    else:
        median = sorted_nums[len(sorted_nums) // 2]

    variance = 0
    for n in numbers:
        variance = variance + (n - mean) ** 2
    variance = variance / len(numbers)

    return {"mean": mean, "median": median, "variance": variance, "count": len(numbers)}


def export_csv(data, output_path):
    f = open(output_path, "w")
    if len(data) > 0:
        headers = []
        for key in data[0].keys():
            headers.append(key)
        f.write(",".join(headers) + "\n")
        for row in data:
            values = []
            for header in headers:
                if header in row:
                    val = str(row[header])
                    val = val.replace(",", ";")
                    val = val.replace("\n", " ")
                    values.append(val)
                else:
                    values.append("")
            f.write(",".join(values) + "\n")
    f.close()
