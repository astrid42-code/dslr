from pandas import read_csv, DataFrame
# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from tools import percentile, _count, _mean, _std, _min, _max
import csv

def numeric_data(data):
    """
        Create a list of columns with only numerics data 
    """
    num_col = []

    for i in data.columns:
        if isinstance(data[i][0], float):
            num_col.append(i)
        else:
            continue
        # try:
        #     if isinstance(data[i][0], float):
        #         num_col.append(i)
        # except:
        #     continue
    return(num_col)

def my_describe(data):

    num = numeric_data(data)
    print(num)


def todo():
    count = []
    mean = []
    std = []
    min_ = []
    max_ = []
    perc_25 = []
    perc_50 = []
    perc_75 = []
    
    # print(data[2][4])
    for i in range(len(data)):
        # print(i, data[i])
        count += [_count(data[i])]
        mean += [_mean(data[i])]
        tmp = mean[i]
        # print(tmp)
        std += [_std(data[i], tmp)]
        min_ += [_min(data[i])]
        max_ += [_max(data[i])]
        perc_25 += [percentile(data[i], 25)]
        perc_50 += [percentile(data[i], 50)]
        perc_75 += [percentile(data[i], 75)]
   
    # print("count", count)
    # print("mean", mean)
    # print("std", std)
    # print("min", min_)
    # print("max", max_)
    # print("25", perc_25)
    # print("50", perc_50)
    # print("75", perc_75)

    res = {
            "count": count, 
            "mean": mean,
            "std": std, 
            "min": min_, 
            "max": max_, 
            "perc 25": perc_25, 
            "perc 50": perc_50, 
            "perc 75": perc_75
    }
    # print("coucou")
    # print('{}'.format(res), sep='\n')

    # for key, value in res.items():
    #     print(f"{key}: {value}")


def main():
    # Load data
    if len(sys.argv) != 2:
        print("You need to give a path as an argument, e.g. dataset_test.csv")
        exit()
    try:
        data_path = "./datasets/" + sys.argv[1]
        data = read_csv(data_path, index_col = 0)
    except Exception:
        return print("ERROR : Unvalid path/file for data")


    # data = read_csv("datasets/dataset_train.csv").to_numpy().transpose() # to obtain # type = <class 'numpy.ndarray'>
    # data = read_csv(sys.argv[1], index_col = 0)
    # print(type(data)) 
    # print(data)
    # print(data[0])

    my_describe(data)

if __name__ == "__main__":
    main()
