from numpy import isnan


def _count(data):
    '''
    Calculate total amount
    '''

    if type(data[0]) is not float and type(data[0]) is not int:
        # print("cocuou")  # à modifier ensuite (à mettre dans le tableau de resulats)
        return (len(data))
    _tmp = data.astype(float)
    _count = _tmp[~isnan(_tmp)]  # to remove nan from a list : https://stackoverflow.com/questions/11620914/how-do-i-remove-nan-values-from-a-numpy-array
    # print(_tmp)
    # print("c= ", len(_count))
    return (len(_count))


def _mean(data):
    '''
    calculate mean
    '''

    _mean = 0.0
    for i in data:
        if type(i) is not float and type(i) is not int:
            # print("coucou")
            return ("We can't calculate without numbers")
        if isnan(i) is True:
                continue
                # pass
        _mean += i
    _mean /= len(data)
    return(_mean)


def _std(data):
    '''
    calculate standard deviation
    '''
    
    res = 0.0
    mean = _mean(data)
    for i in data:
        if type(i) is not float and type(i) is not int:
            # print("coucou")
            return ("We can't calculate without numbers")
        if i == 'nan':
                continue
        res += (i - mean) ** 2
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
        if i == 'nan':
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
        
        if i == 'nan':
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
