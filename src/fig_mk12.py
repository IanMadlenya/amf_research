"""
Comparative graph between MK12 and this model.
"""
import copy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy
numpy.seterr(divide="ignore")

from convertible_bond import dS_total as dS, payoff, B
from model import FDEModel

def main():
    N = 200
    S = range(121)
    Sl = 0
    Su = 200
    dS.sigma = 0.25
    dS.lambd_ = 0.062
    dSv = copy.copy(dS)
    dSv.lambd_ = lambda S: 0.062 * (S / 50)**-0.5
    dSv.cap_lambda = True
    B.R = 0.4
    model1 = FDEModel(N, dS, payoff)
    model2 = FDEModel(N, dSv, payoff)
    plt.plot(S, model1.price(Sl, Su, N).V[0][S])
    plt.plot(S[1:], model2.price(Sl + 1, Su, N - 1).V[0][S[:-1]])
    plt.ylim([40, 160])
    plt.xlabel("Stock Price")
    plt.ylabel("Convertible Bond Price")
    plt.title("Convertible Bond Price Profile, N = %i, R = %i%%" % (N, B.R * 100))
    plt.legend(["Constant $\\lambda$", "Synthesis $\\lambda$"], loc=2)
    plt.savefig("../common/fig_mk12.png")
    plt.savefig("../common/fig_mk12.svg")
    #plt.show()

if __name__ == "__main__":
    main()
