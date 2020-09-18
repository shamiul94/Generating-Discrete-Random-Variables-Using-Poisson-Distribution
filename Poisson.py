#!/home/heisenberg/anaconda3/bin/python

# importing the required module
import matplotlib.pyplot as plt
import math
from random import seed
from random import random
from random import uniform


def plotSingleGraph(x, y):
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('X')
    # naming the y axis
    plt.ylabel('CDF')

    plt.title('Poisson Distribution')

    # function to show the plot
    plt.show()


def getCDF(x, Lambda):
    if x < 0:
        return 0
    else:
        return math.exp(-1.0 * Lambda) * sum([(pow(Lambda, i) / math.factorial(i)) for i in range(math.floor(x))])


def getExperimentalValues(cdfs):
    discreteValues = []
    # seed random number generator
    seed(1)
    # generate random numbers between 0-1
    for _ in range(1000):
        value = random()
        print(value, '----->')
        discreteVal = 0
        lo = 0
        hi = len(cdfs)-1
        # mid = lo + (hi-lo)/2
        while lo <= hi:
            # print(lo, '#', hi)
            mid = int(lo + (hi-lo)/2)
            # print('mid==', mid)

            if value > cdfs[mid]:
                lo = mid+1
            else:  # value <= cdfs[mid]
                hi = mid-1
                discreteVal = mid
            # break

        print('[', discreteVal, ']', cdfs[discreteVal], '\n')
        discreteValues.append(discreteVal)
    print(discreteValues)


    freqencies = [0 for i in range(21)]

    for val in discreteValues: 
        freqencies[val] = freqencies[val] + 1
    # print(sum(freqencies))

    for i in range(1, len(freqencies)): 
        freqencies[i] = freqencies[i] + freqencies[i-1]

    for i in range(len(freqencies)): 
        freqencies[i] = freqencies[i]/ 1000; 

    return discreteValues, freqencies


def main():
    ####### Theoratical values #######
    x = [i for i in range(0, 21)]
    Lambda = 1
    cdfs = [getCDF(i, Lambda) for i in x]
    # plotSingleGraph(x, cdfs)
    plt.plot(x, cdfs, label = "x vs F(x)") 

    ######## Experimental values #########
    print(cdfs)
    print('---------------')
    discreteValues, cummulative_freq = getExperimentalValues(cdfs)
    # print(cummulative_freq)
    # plotSingleGraph(x, cummulative_freq)

    plt.plot(x, cummulative_freq, label = "x vs cummulative frequencies")

    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 
    plt.title('Poisson') 

    plt.legend() 
  
    # function to show the plot 
    plt.show() 


if __name__ == '__main__':
    main()
