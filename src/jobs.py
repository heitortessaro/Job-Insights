import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        jobs_data = []
        for row in csv.DictReader(file, delimiter=",", quotechar='"'):
            jobs_data.append(row)
    return jobs_data
