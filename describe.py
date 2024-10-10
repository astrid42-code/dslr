from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
import numpy as np
import sys


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



if __name__ == "__main__":
    main()
