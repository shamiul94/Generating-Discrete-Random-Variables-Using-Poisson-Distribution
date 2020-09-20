#!/home/heisenberg/anaconda3/bin/python

import matplotlib.pyplot as plt
import math
from random import seed
from random import random
from random import uniform


def plotSingleGraph(x, y):
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('CDF')
    plt.title('Poisson Distribution')
    plt.show()


def getCDF(x, Lambda):
    if x < 0:
        return 0
    else:
        return math.exp(-1.0 * Lambda) * sum([(pow(Lambda, i) / math.factorial(i)) for i in range(math.floor(x+1))])


def getExperimentalValues(cdfs):
    discreteValues = []

    seed(1)

    for _ in range(1000):
        # generate random numbers between 0-1
        value = random()

        discreteVal = 0

        # Finding the smallest number which is larger than 'value'. It is actually upper bound.
        # It can be solved using both Bruteforce and Binary Search. I used the latter.

        lo = 0
        hi = len(cdfs)-1
        while lo <= hi:
            mid = int(lo + (hi-lo)/2)

            if value > cdfs[mid]:
                lo = mid+1
            else:  # value <= cdfs[mid]
                hi = mid-1
                discreteVal = mid

        # print('[', discreteVal, ']', cdfs[discreteVal], '\n')
        discreteValues.append(discreteVal)
    # print(discreteValues)

    freqencies = [0 for i in range(21)]

    for val in discreteValues:
        freqencies[val] = freqencies[val] + 1
    
    for i in range(len(freqencies)):
        freqencies[i] = freqencies[i] / 1000

    noncumulative = [i for i in freqencies]
    

    for i in range(1, len(freqencies)):
        freqencies[i] = freqencies[i] + freqencies[i-1]

    # print(freqencies)
    # print(noncumulative)

    return discreteValues, freqencies, noncumulative


def getPx(x, Lambda):
    if x < 0:
        return 0
    else:
        return math.exp(-1.0 * Lambda) * math.pow(Lambda, x) / math.factorial(x)


def main():
    ####### Theoratical values #######
    x = [i for i in range(0, 21)]
    Lambda = 1

    ######### p(x) ###########

    Px = [getPx(i, Lambda) for i in x]
    plt.plot(x, Px, label="x vs P(x)")

    ########## F(x) ###########
    cdfs = [getCDF(i, Lambda) for i in x]
    plt.plot(x, cdfs, label="x vs F(x)")

    ######## Experimental values #########
    # print(cdfs)

    discreteValues, cummulative_freq, noncumulative_freq = getExperimentalValues(cdfs)
    plt.plot(x, cummulative_freq, label="x vs cummulative frequencies")
    plt.plot(x, noncumulative_freq, label="x vs non-cummulative frequencies")

    ############# Plot them ###############
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Poisson')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
