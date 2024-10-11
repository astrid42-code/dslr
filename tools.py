
def _count(data):
    '''
    calculate total amount
    '''
    return (len(data))


def _mean(data):
    '''
    calculate mean
    '''
    _mean = 0.0
    for i in data:
        _mean += data[i]
    _mean /= len(data)
    return(_mean)


def _std(data):
    '''
    calculate standard deviation
    '''
    res = 0.0
    mean = _mean(data)
    for i in data:
        res += (data[i] - mean) ** 2
    return (res / len(data))


def _min(data):
    '''
    find min data
    '''
    _min = data[0]
    for i in data:
        if data[i] < _min:
            _min = data[i]
    return (_min)


def _max(data):
    '''
    find max data
    '''
    _max = data[0]
    for i in data:
        if data[i] > _max:
            _max = data[i]
    return (_max)

def percentile(data, perc):
    '''
    calculate percentile 
    perc = 25, 50, 75
    '''

    print(type(data[0]))
    if type(data[0]) is not float and type(data[0]) is not int:
        # print("We can't calculate without numbers")  # à modifier ensuite (à mettre dans le tableau de resulats)
        return (-1)
    # percentile's position
    pos = (len(data) + 1) * (perc  / 100)

    # value at the position
    tmp1 = data[int(pos)]
    tmp2 = data[int(pos) + 1]
    val = (tmp1 + tmp2) / 2

    return (val)
