from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
import numpy as np
import sys
from tools import percentile


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
    # for i in data:
    #     print(type(i), i)
    perc_25 = percentile(data[4], 25)
    if perc_25 == -1:
        perc_25 = "We can't calculate without numbers"
    perc_50 = percentile(data[5], 50)
    if perc_50 == -1:
        perc_50 = "We can't calculate without numbers"
    perc_75 = percentile(data[6], 75)
    if perc_75 == -1:
        perc_75 = "We can't calculate without numbers"

    print(perc_25, perc_50, perc_75)


if __name__ == "__main__":
    main()
