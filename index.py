import numpy as np
import yfinance as yf


class monteCarloSim:
    '''
    Object for returning call/put price at given t for European option.
    '''

    def __init__(self, spot_price, mu, sigma, epochs, time_to_maturity, intervals, strike_price):
        self.S = spot_price
        self.mu = mu
        self.strike_price = strike_price
        self.sigma = sigma
        self.epochs = epochs
        self.T = time_to_maturity
        self.intervals = intervals

    def price_paths(self):
        dt = self.T / self.intervals  # defines the change in time in the given time left
        price_paths = np.zeros((self.epochs + 1, self.intervals))  # initialise empty matrix
        for i in range(self.epochs + 1):
            z_values = np.random.randn(self.intervals)  # get random Z values using standard normal
            for z_index in range(self.intervals):
                price_paths[i][z_index] = self.S * np.exp(
                    (self.mu - 0.5 * (self.sigma ** 2)) * dt + self.sigma * z_values[
                        z_index])  # use GBM solution to return price paths
        return price_paths

    def call_price(self, price_matrix):
        payoffs = [max(price_matrix[-1][i] - self.strike_price, 0) for i in range(self.intervals)]
        return np.exp(-self.mu * self.T) * 1 / self.intervals * np.sum(payoffs)


spot_price = 100
average = 0.05
volatility = 0.2
time_to_maturity = 1
strike_price = 100
sim_num = 500
simulator = monteCarloSim(spot_price, average, volatility, 100, time_to_maturity, 100, strike_price)


def generate_good_call(model, sim_num):
    s = []
    for i in range(sim_num):
        prices = model.price_paths()
        s.append(model.call_price(prices))
    return np.mean(s)


price = generate_good_call(simulator, sim_num)
print(price)