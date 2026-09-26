from pandas import read_csv, DataFrame
# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import tools
from tools import percentile, _count, _mean, _std, _min, _max
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
    print(data)

    count = _count(data, col_index)
    # count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # mean = []
    # std = []
    # min_ = []
    # max_ = []
    # perc_25 = []
    # perc_50 = []
    # perc_75 = []
    n = 0
    for i in data:
        # print('i', i)
        # print('data[i]', data[i])
        if i in col_index:
            df.loc["Count", df.columns[n]] = count[n]
        
            # lancer la fct count et assigner la valeur trouvée dans la case "Count[n]" en mettant n = 0 au dessus et n+=1 à la fin de la boucle
            n+=1
    # print(data)
    print(df)


def my_describe(data):

    col_index = find_col_index(data)
    df = create_df(col_index)
    fill_df(data, df, col_index)

def tools(data):
    
    # print(data[2][4])
    for i in range(len(data)):
        # print(i, data[i])
        count += [tools._count(data[i])]
        mean += [tools._mean(data[i])]
        tmp = mean[i]
        # print(tmp)
        std += [tools._std(data[i], tmp)]
        min_ += [tools._min(data[i])]
        max_ += [tools._max(data[i])]
        perc_25 += [tools.percentile(data[i], 25)]
        perc_50 += [tools.percentile(data[i], 50)]
        perc_75 += [tools.percentile(data[i], 75)]
   
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
