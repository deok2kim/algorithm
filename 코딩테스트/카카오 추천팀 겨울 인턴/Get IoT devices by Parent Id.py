#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'avgRotorSpeed' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId
#
import requests


def avgRotorSpeed(statusQuery, parentId):
    # Write your code here
    URL = 'https://jsonmock.hackerrank.com/api/iot_devices/search?'

    def get_infos(_statusQuery, _pageNumber):
        uri = f'{URL}status={_statusQuery}&page={_pageNumber}'
        return requests.get(uri).json()

    totalPages = get_infos(statusQuery, 1)['total_pages']

    totRotorSpeed = 0
    cntRotorSpeed = 0
    # 전체 페이지 수만큼 
    for page in range(1, totalPages + 1):
        infos = get_infos(statusQuery, page)
        for info in infos:
            # 데이터 - 페어런트(있을수도있고 없을수도 있고 get())
            if info == 'data':
                for d in infos['data']:
                    # 페어런트가 있고, 아이디가 parentId 이면
                    if d.get('parent') and d['parent']['id'] == parentId:
                        totRotorSpeed += d['operatingParams']['rotorSpeed']
                        cntRotorSpeed += 1

    answer = totRotorSpeed // cntRotorSpeed if cntRotorSpeed != 0 else 0
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    statusQuery = input()

    parentId = int(input().strip())

    result = avgRotorSpeed(statusQuery, parentId)

    fptr.write(str(result) + '\n')

    fptr.close()
