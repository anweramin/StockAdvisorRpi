import numpy as np 
import mongo_data as mdata

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



#Relative Strength Index (RSI)
# price =  closing rates
def rsiFunc(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi




#   compute the MACD (Moving Average Convergence/Divergence) using a fast and slow exponential moving avg'
#    return value is emaslow, emafast, macd which are len(x) arrays
def computeMACD(x, slow=26, fast=12):
    emaslow = ExpMovingAverage(x, slow)
    emafast = ExpMovingAverage(x, fast)
    return emaslow, emafast, emafast - emaslow # tuple

# print(movingaverage(mdata.getClosingRates('Atlas Honda Ltd'),5))
# print(ExpMovingAverage(mdata.getClosingRates('Atlas Honda Ltd'),5))
# print(ExpMovingAverage([1,2,34,45,53,65,72],3))