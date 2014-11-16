# coding: utf-8
"""
Created on 28.01.2013 16:55:35
@author: Oleksandr Poliatykin
"""
from datetime import datetime

import csv
import sys

import matplotlib.pyplot as plt

datafile = "ServerTempHigh.csv"
dpd2 = []


def parse_csv(datafile):
    with open(datafile) as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        isHeader = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)
        r = csv.reader(csvfile, dialect)
        if isHeader:
            header = r.__next__()
            for (i, dat) in enumerate(header):
                header[i] = dat.strip()
            print(header)
        try:
            for row in r:
                rowdata = []
                for column in row:
                    rowdata.append(column.strip())
                dpd2.append(rowdata)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(datafile, r.line_num, e))
            
    dpd2.reverse()
    times = []
    temperatures = []
    for r in dpd2:
        # 2013-01-28 06:59:29
        date_object = datetime.strptime(r[0] + " " + r[1],
                                         "%Y-%m-%d %H:%M:%S")
        times.append(date_object)  # .timestamp())
        temperatures.append(float(r[2]))
    print("total samples: " + str(len(dpd2)))
    return times, temperatures


def plot_data(times, temperatures):
    plt.plot(times, temperatures)
    plt.ylabel("UPS Temperature")
    plt.show()

if __name__ == "__main__":
    times, temperatures = parse_csv(datafile)
    plot_data(times, temperatures)
