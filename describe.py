from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt
import os
import numpy as np


def main():
    # Load data
    try:
        data_path = os.path.join(os.getcwd(), "datasets/dataset_train.csv")
        dataset = read_csv(data_path)
    except Exception:
        return print("ERROR : Unvalid path/file for data")
    # print(dataset)

    data = read_csv("datasets/dataset_train.csv").to_numpy().transpose()
    print(data)

    

if __name__ == "__main__":
    main()
