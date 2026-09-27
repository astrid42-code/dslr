from numpy import inf
from math import isfinite


def _count(data, col_index):
    '''
    calculate number of numeric data for each numeric column 
    returns an ordered list of all counts
    '''

    # print(col_index)
    count_list = []
    for i in data:
        # print('data[i]', data[i])
        if i in col_index:
            _count = 0.0
            # print("datai", data[i])
            for c in data[i]:
                # # print(c)
                if isfinite(c):
                    _count+=1
                
            count_list.append(_count)
        print(count_list)
        print(len(count_list))

   
    return (count_list)


def _mean(data, col_index, count):
    '''
    calculate mean for each numeric column 
    formula : total amount / count (count = the number of numeric data in the column)
    returns an ordered list of all means
    '''
    mean_list = []
    for i in data:
        if i in col_index:
            _mean = 0.0
            j = 0
            for c in data[i]:
                # print(c)
                if isfinite(c):
                    _mean += c
            _mean /= count[j]
            # print("mean", mean)
            mean_list.append(_mean)
            j+=1
    return(mean_list)

def _min(data, col_index):
    '''
    find min data for each numeric column 
    returns an ordered list of all mins
    '''

    min_list = []
    for i in data:
        if i in col_index:
            _min = inf
            for c in data[i]:
                if isfinite(c):
                    if c < _min:
                        _min = c
                    
            min_list.append(_min)
    return(min_list)


def _max(data, col_index):
    '''
    find max data for each numeric column 
    returns an ordered list of all maxs
    '''

    max_list = []
    for i in data:
        if i in col_index:
            _max = -inf
            for c in data[i]:
                if isfinite(c):
                    if c > _max:
                        _max = c
                        
            max_list.append(_max)
    return(max_list)


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

def _perc_25(data, col_index):
    '''
    calculate percentile 25
    returns an ordered list of all percentile 25
    '''

    perc_25_list = []
    for i in data:
        val = 0
        if i in col_index:

            # percentile's position
            pos = (len(data) - 1) * 0.25
            print("pos", pos, type(pos))
                    
            # value at the position
            # tmp1 = data[int(pos)]
            # tmp2 = data[int(pos) + 1]
            # val = (tmp1 + tmp2) / 2
                            
        perc_25_list.append(val)
    return(perc_25_list)

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
