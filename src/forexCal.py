import numpy as np 


#Simple moving average
# values =  closing rates
# window =  time window; 10-day or 20-day etc
def movingaverage(values,window):
    weigths = np.repeat(1.0, window)/window       # to save up on processing power.
    smas = np.convolve(values, weigths, 'valid')  # only run on valid points
    return smas # as a numpy array

# print(movingaverage([1,2,34,45,53,65,72],3))



#exponensial moving average
# values =  closing rates
# window =  time window; 10-day or 20-day etc
def ExpMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a =  np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a

print(ExpMovingAverage([1,2,34,45,53,65,72],3))
