# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from itertools import combinations
from collections import defaultdict
import pandas as pd

input = sys.stdin.readline

numberOfAttributes = int(input())
supportThreshold = float(input())
numberOfRows = int(input())

data = defaultdict(list)
for i in range(numberOfRows):
    peopleInfos = input().strip().split(',')

    for peopleInfo in peopleInfos:
        key, value = peopleInfo.split("=")
        data[key].append(value)

attributes = data.keys()
df = pd.DataFrame(data)

for selectedAttribute in combinations(attributes, numberOfAttributes):
    df = pd.DataFrame(data, columns=list(selectedAttribute))
    display








