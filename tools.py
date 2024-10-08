
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


def percentile_25(data):
    '''
    calculate percentile (25%)
    '''


def percentile_50(data):
    '''
    calculate percentile (50%)
    '''


def percentile_75(data):
    '''
    calculate percentile (75%)
    '''