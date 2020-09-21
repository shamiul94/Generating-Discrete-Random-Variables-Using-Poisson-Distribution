#!/home/heisenberg/anaconda3/bin/python

import matplotlib.pyplot as plt
import math
from random import seed
from random import random
from random import uniform

# This function is to plot a single curve


def plotSingleGraph(x, y):
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('CDF')
    plt.title('Poisson Distribution')
    plt.show()

# This function calculates the CDF or F(x) of the Poisson Distribution


def getCDF(x, Lambda):
    if x < 0:
        return 0
    else:
        return math.exp(-1.0 * Lambda) * sum([(pow(Lambda, i) / math.factorial(i)) for i in range(math.floor(x+1))])

# This function calculates the PDF or p(x) of the Poisson Distribution


def getPx(x, Lambda):
    if x < 0:
        return 0
    else:
        return math.exp(-1.0 * Lambda) * math.pow(Lambda, x) / math.factorial(x)


# This function calculates the Frequencies and Cummulative Frequencies of random numbers between 0 and 1.
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

        discreteValues.append(discreteVal)

    freqencies = [0 for i in range(21)]

    for val in discreteValues:
        freqencies[val] = freqencies[val] + 1

    for i in range(len(freqencies)):
        freqencies[i] = freqencies[i] / 1000

    noncumulative = [i for i in freqencies]

    for i in range(1, len(freqencies)):
        freqencies[i] = freqencies[i] + freqencies[i-1]

    return discreteValues, freqencies, noncumulative


# In this function I calculated p(x), F(x), frequencies/N, cumulative frequencies/N and plot them.

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

    discreteValues, cummulative_freq, noncumulative_freq = getExperimentalValues(
        cdfs)
    plt.plot(x, cummulative_freq, label="x vs cummulative frequencies")
    plt.plot(x, noncumulative_freq, label="x vs non-cummulative frequencies")

    for i in range(21):
        print(x[i], '&', Px[i], '&', noncumulative_freq[i], '&', cdfs[i],
              '&', cummulative_freq[i], '\\\\', '\n', '\\hline' '\n')

    ############# Plot them ###############
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Poisson')
    plt.legend()
    plt.show()

    ############
    fig, ax = plt.subplots(figsize=(10,10), dpi= 80)
    ax.vlines(x=x, ymin=0, ymax=cummulative_freq, color='firebrick', alpha=1, linewidth=2)
    ax.scatter(x=x, y=cummulative_freq, s=75, color='firebrick', alpha=1)

    plt.xlabel('X')
    plt.ylabel('Cumulative Frequency/N')
    plt.title('Poisson Distribution Cumulative Frequency')
    plt.legend()
    plt.show()
    return


if __name__ == '__main__':
    main()
