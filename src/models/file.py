import csv
import os

PROJECT_PATH = None


class File:
    @staticmethod
    def read_csv(path):
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            return [row for row in csv_reader]

    @staticmethod
    def write_csv(path=PROJECT_PATH, message=''):
        ...
