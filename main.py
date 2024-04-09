import numpy

class MonteCarloSim:
    '''
    Object for returning call/put price at given t for European option.
    '''
    def __init__(self,spot_price,mu,sigma,epochs,time_to_maturity,intervals):
        self.S = spot_price
        self.mu = mu
        self.sigma = sigma
        self.epochs = epochs
        self.T = time_to_maturity
        self.intervals = intervals

    
