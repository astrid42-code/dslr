from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
import numpy as np
import sys
from tools import percentile, _mean, _std, _min, _max


def main():
    # Load data

    if len(sys.argv) != 2:
        print("You need to give a path as argument")
        exit()
    try:
        data_path = "datasets/" + sys.argv[1]
        # print(data_path)
        dataset = read_csv(data_path)
    except Exception:
        return print("ERROR : Unvalid path/file for data")
    # print(dataset)  # type = <class 'pandas.core.frame.DataFrame'>

    data = read_csv("datasets/dataset_train.csv").to_numpy().transpose()
    # print(data) # type = <class 'numpy.ndarray'>
    # print(data[0])
    mean = []
    std = []
    min_ = []
    max_ = []
    perc_25 = []
    perc_50 = []
    perc_75 = []
    
    count = len(data[0])

    for i in range(len(data)):
        # print(i, data[i])
        # mean += [_mean(data[i])]
        # std += [_std(data[i])]
        # min_ += [_min(data[i])]
        max_ += [_max(data[i])]
        perc_25 += [percentile(data[i], 25)]
        # if perc_25[i] == -1:
        #     perc_25[i] = "We can't calculate without numbers"
        perc_50 += [percentile(data[i], 50)]
        # if perc_50[i] == -1:
        #     perc_50[i] = "We can't calculate without numbers"
        perc_75 += [percentile(data[i], 75)]
        # if perc_75[i] == -1:
        #     perc_75[i] = "We can't calculate without numbers"
    
    print("count", count)
    print("mean", mean)
    print("std", std)
    print("min", min_)
    print("max", max_)
    print("25", perc_25)
    print("50", perc_50)
    print("75", perc_75)


if __name__ == "__main__":
    main()
