# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

numberOfAttributes = int(input())
supportThreshold = float(input())
numberOfRows = int(input())

people = []
for i in range(numberOfRows):
    peopleInfos = input().strip().split(',')
    infoDict = {}
    for peopleInfo in peopleInfos:
        key, value = peopleInfo.split("=")
        infoDict[key] = value

    people.append(infoDict)

attributes = people[0].keys()

for selectedAttribute in combinations(attributes, numberOfAttributes):
    data = defaultdict(int)
    for person in people:
        personData = []
        for attribute in selectedAttribute:
            personData.append(f'{attribute}={person[attribute]}')

        data[tuple(personData)] += 1

    for key in data:
        if data[key] / numberOfRows >= supportThreshold:
            print(','.join(key))







