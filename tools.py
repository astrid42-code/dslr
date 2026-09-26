# from numpy import isnan
from math import isfinite


def _count(data, col_index):
    '''
    Calculate total amount
    '''

    # print(col_index)
    count_list = []
    for i in data:
        # print('data[i]', data[i])
        if i in col_index:
            count = 0.0
            # print("datai", data[i])
            for c in data[i]:
                # # print(c)
                if isfinite(c):
                    count+=1
                
            count_list.append(count)
        print(count_list)
        print(len(count_list))

   
    return (count_list)


def _mean(data, col_index, count):
    '''
    calculate mean
    '''
    mean_list = []
    for i in data:
        if i in col_index:
            mean = 0.0
            j = 0
            for c in data[i]:
                # print(c)
                if isfinite(c):
                    mean += c
            mean /= count[j]
            # print("mean", mean)
            mean_list.append(mean)
            j+=1
        # print("type i", type(i))
        # if type(i) is not float and type(i) is not int:
        #     return ("We can't calculate without numbers")
        # if isnan(i):
        #     continue
        # mean += i
    # print("type mean", type(mean))
    return(mean_list)


def _std(data, mean):
    '''
    calculate standard deviation
    '''
    
    res = 0.0

    for i in data:
        if type(i) is not float and type(i) is not int:
            # print("coucou")
            return ("We can't calculate without numbers")
        if isnan(i):    
            continue
            # i = 0
        res += (float(i) - mean) ** 2
    # print(res)
    return (res / len(data))


def _min(data):
    '''
    find min data
    '''
    
    # print("data0", data[0])
    _min = data[0]
    for i in data:
        if type(i) is not float and type(i) is not int:
            # print("coucou")
            return ("We can't calculate without numbers")
        # print("data_i", data[i])
        if isnan(i):
            continue
        if i < _min:
            _min = i
    # print("_min", _min)
    return (_min)


def _max(data):
    '''
    find max data
    '''
    _max = data[0]
    for i in data:
        # print("i", i)
        if type(i) is not float and type(i) is not int:
            # print("coucou")
            return ("We can't calculate without numbers")
        
        if isnan(i):
            continue
        if i > _max:
            _max = i
    # print("_max", _max)
    return (_max)

def percentile(data, perc):
    '''
    calculate percentile 
    perc = 25, 50, 75
    '''

    if type(data[0]) is not float and type(data[0]) is not int:
        # print()  # à modifier ensuite (à mettre dans le tableau de resulats)
        return ("We can't calculate without numbers")
    
    # percentile's position
    pos = (len(data) - 1) * (perc  / 100)

    # value at the position
    tmp1 = data[int(pos)]
    tmp2 = data[int(pos) + 1]
    val = (tmp1 + tmp2) / 2

    return (val)
