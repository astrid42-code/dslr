from pandas import read_csv, DataFrame
# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
# import tools
from tools import _percentile, _count, _mean, _std, _min, _max 
import csv

def find_col_index(data):
    """
        Create the list of columns names with only numeric data 
    """
    col_index = []

    for i in data.columns:
        if isinstance(data[i][0], float):
            col_index.append(i)
        else:
            continue
        # try:
        #     if isinstance(data[i][0], float):
        #         num_col.append(i)
        # except:
        #     continue
    return(col_index)

def create_df(col_index):
    # calculer les résultats de chaque index pour pouvoir les envoyer directement dans le nveau dataframe 
    # faire boucle donnant les index puis les colonnes (ou l'inverse?) 
    
    if col_index == []:
        exit
    row_index = ["Count", "Mean", "Std", "Min", "25%","50%", "75%", "Max"]
    my_df = DataFrame(data= np.zeros((len(row_index), len(col_index))), index= row_index, columns= col_index)
    return(my_df)

def fill_df(data, df, col_index):
    # print(data)

    count = _count(data, col_index)
    mean = _mean(data, col_index, count)
    std = _std(data, col_index, mean, count)
    mini = _min(data, col_index)
    maxi = _max(data, col_index)
    perc_25 = _percentile(data, col_index, count, 25)
    perc_50 = _percentile(data, col_index, count, 50)
    perc_75 = _percentile(data, col_index, count, 75)
    n = 0
    for i in data:
        # print('i', i)
        # print('data[i]', data[i])
        if i in col_index:
            df.loc["Count", df.columns[n]] = count[n]
            df.loc["Mean", df.columns[n]] = mean[n]
            df.loc["Min", df.columns[n]] = mini[n]
            df.loc["Max", df.columns[n]] = maxi[n]
            df.loc["25%", df.columns[n]] = perc_25[n]
            df.loc["50%", df.columns[n]] = perc_50[n]
            df.loc["75%", df.columns[n]] = perc_75[n]
            df.loc["Std", df.columns[n]] = std[n]
            n+=1

    print(df)


def my_describe(data):

    col_index = find_col_index(data)
    df = create_df(col_index)
    fill_df(data, df, col_index)


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
