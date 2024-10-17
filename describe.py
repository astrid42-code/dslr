from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
import numpy as np
import sys
from tools import percentile, _count, _mean, _std, _min, _max
import csv

def main():
    # Load data

    if len(sys.argv) != 2:
        print("You need to give a path as argument")
        exit()
    # try:
    #     data_path = "datasets/" + sys.argv[1]
    #     # data_path = sys.argv[1]
    #     # print(data_path)
    #     # dataset = read_csv(data_path)
    # except Exception:
    #     return print("ERROR : Unvalid path/file for data")
    # print(dataset)  # type = <class 'pandas.core.frame.DataFrame'>

    data = read_csv("datasets/dataset_train.csv").to_numpy().transpose()
    # print(data) # type = <class 'numpy.ndarray'>
    # print(data[0])
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
    for key, value in res.items():
        print(f"{key}: {value}")

    # a revoir:

    # with open('newdataset.csv', 'w', newline='') as csvfile:
    #     newdata = csv.writer(csvfile, delimiter=' ',
    #                             quotechar='|')
    #     for i, j in res.items():
    #         newdata.writerow([i, j])
    #         # newdata.writerow()
    #     print_data = read_csv('newdataset.csv').to_numpy().transpose()
    #     print(print_data)

if __name__ == "__main__":
    main()
