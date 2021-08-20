import sys

V1 = float(str(sys.argv[1]))
V2 = float(str(sys.argv[2]))
V3 = float(str(sys.argv[3]))
V4 = float(str(sys.argv[4]))
V5 = str(sys.argv[5])
V6 = float(str(sys.argv[6]))
V7 = float(str(sys.argv[7]))

import numpy as np
import math
import time

class OptionPricing:

    def __init__(self,S0, E,T, rf, sigma, dividend, iterations):
        self.S0= S0
        self.E = E
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.dividend = dividend
        self.iterations = iterations

    def call_option_simulation(self):

        option_data = np.zeros([self.iterations, 2])

        rand = np.random.normal(0, 1, [1, self.iterations])

        stock_price = self.S0*np.exp(self.T*((self.rf - self.dividend) - 0.5*self.sigma**2) + self.sigma*np.sqrt(self.T)*rand)

        option_data[:,1] = stock_price - self.E

        average = np.sum(np.amax(option_data, axis=1))/float(self.iterations)

        return np.exp(-1.0*(self.rf - self.dividend)*self.T)*average

    def pull_option_simulation(self):

        option_data = np.zeros([self.iterations, 2])

        rand = np.random.normal(0, 1, [1, self.iterations])

        stock_price = self.S0*np.exp(self.T*((self.rf - self.dividend) - 0.5*self.sigma**2) + self.sigma*np.sqrt(self.T)*rand)

        option_data[:,1] = self.E - stock_price 

        average = np.sum(np.amax(option_data, axis=1))/float(self.iterations)

        return np.exp(-1.0*(self.rf - self.dividend)*self.T)*average

if __name__ == "__main__":

    S0 = V1
    E = V2
    T = V3
    rf = (V6/100)
    sigma = (V4/100)
    dividend = (V7/100)
    iterations = 10000000

    model = OptionPricing(S0,E,T,rf,sigma,dividend,iterations)
    if V5 == "Call":
        print (model.call_option_simulation())
    else: 
        print (model.pull_option_simulation())


    



                              

