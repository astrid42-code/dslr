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
        # print(count_list)
        # print(len(count_list))

   
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


def _perc_75(data, col_index, count):
    '''
    calculate percentile 25
    returns an ordered list of all percentile 25
    '''

    perc_75_list = []
    j = 0
    for i in data:
        val = 0
        if i in col_index:
            # print(j, count[j])
            # percentile's position
            pos = int((count[j] - 1) * 0.75)
                    
            # value at the position
            tmp1 = data[i][pos]
            tmp2 = data[i][pos + 1]
            val = (tmp1 + tmp2) / 2
                            
            j+=1
            perc_75_list.append(val)
    return(perc_75_list)

def _percentile(data, col_index, count, perc):
    '''
    calculate percentile     
    perc = 25, 50, 75
    returns an ordered list of all percentile 25
    '''

    perc_list = []
    j = 0
    for i in data:
        val = 0
        if i in col_index:
            # new_count = 0
            # for c in data[i]:
            #     if isfinite(c):
            #         data_ordered = list(data[i])
            #         new_count += 1
            data_ordered = sorted(c for c in data[i] if isfinite(c))

            l = len(data_ordered)

            if l == 0:
                perc_list.append(float('nan'))
                continue

            # Calculate theoretical position
            pos = (l - 1) * (perc / 100)

            lower = int(pos)
            upper = min(lower + 1, l - 1)

            # Linear interpolation
            weight = pos - lower

            val = (
                data_ordered[lower] * (1 - weight)
                + data_ordered[upper] * weight
            )


            # # percentile's position
            # pos = ((l - 1) * (perc / 100))
            # # pos = int((len(data_ordered) - 1) * (perc / 100))


    
            # # value at the position
            # tmp1 = data_ordered[pos]
            # tmp2 = data_ordered[pos + 1]
            # val = (tmp1 + tmp2) / 2
            # # print("val", val)
                            
            # j+=1
            perc_list.append(val)
    return(perc_list)
 

    # if type(data[0]) is not float and type(data[0]) is not int:
    #     # print()  # à modifier ensuite (à mettre dans le tableau de resulats)
    #     return ("We can't calculate without numbers")
    
    # # percentile's position
    # pos = (len(data) - 1) * (perc  / 100)

    # # value at the position
    # tmp1 = data[int(pos)]
    # tmp2 = data[int(pos) + 1]
    # val = (tmp1 + tmp2) / 2

    # return (val)
