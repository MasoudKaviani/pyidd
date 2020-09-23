import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels.api as sm
import matplotlib
import matplotlib.pyplot as plt
import warnings

class PyIDD:
    def __init__(self):
        self.distributions = {}
        self.data = pd.Series()
        self.x = []
    
    def plot(self, bins=100, top=5, figsize=(16, 12)):
        sd = sorted(self.distributions.items(), key=lambda x: x[1]['SSE'])
        ax = self.data.plot(kind='hist', bins=bins, normed=True, alpha=0.5, figsize=figsize)
        sd = sd[:top]
        # print(self.distributions)
        for k, v in sd:
            pdf = v['pdf']
            sse = round(v['SSE'], 2)
            pd.Series(pdf, self.x).plot(ax=ax, legend=True, label=str(k) + str(' (' + str(sse) + ')'))

    def get_distributions(self):
        return self.distribution
    
    def fit(self, data):
        try:
            data = pd.Series(data)
        except Exception:
            raise Exception('The data must be an one dimensional array')
        
        self.data = data
        bins = 200
        y, x = np.histogram(data, bins=bins, density=True)
        x = (x + np.roll(x, -1))[:-1] / 2.0
        self.x = x

        CDISTRIBUTIONS = [
            st.alpha, st.anglit, st.arcsine, st.argus, st.beta, st.betaprime, st.bradford,
            st.burr, st.burr12, st.cauchy, st.chi, st.chi2, st.cosine, st.crystalball,
            st.dgamma, st.dweibull, st.erlang, st.expon, st.exponnorm, st.exponweib,
            st.exponpow, st.f, st.fatiguelife, st.fisk, st.foldcauchy, st.foldnorm,
            st.frechet_r, st.frechet_l, st.genlogistic, st.gennorm, st.genpareto,
            st.genexpon, st.genextreme, st.gausshyper, st.gamma, st.gengamma, st.genhalflogistic,
            st.geninvgauss, st.gilbrat, st.gompertz, st.gumbel_r, st.gumbel_l, st.halfcauchy,
            st.halflogistic, st.halfnorm, st.halfgennorm, st.hypsecant, st.invgamma, st.invgauss,
            st.invweibull, st.johnsonsb, st.johnsonsu, st.kappa4, st.kappa3, st.ksone, st.kstwo,
            st.kstwobign, st.laplace, st.levy, st.levy_l, st.logistic, st.loggamma,
            st.loglaplace, st.lognorm, st.loguniform, st.lomax, st.maxwell, st.mielke, st.moyal,
            st.nakagami, st.ncx2, st.ncf, st.nct, st.norm, st.norminvgauss, st.pareto, st.pearson3,
            st.powerlaw, st.powerlognorm, st.powernorm, st.rdist, st.rayleigh, st.rice, st.recipinvgauss,
            st.semicircular, st.skewnorm, st.t, st.trapz, st.triang, st.truncexpon, st.truncnorm,
            st.tukeylambda, st.uniform, st.vonmises, st.vonmises_line, st.wald, st.weibull_min,
            st.weibull_max, st.wrapcauchy
        ]
        
        best_distribution = st.norm
        best_params = (0.0, 1.0)
        best_sse = np.inf

        for distribution in CDISTRIBUTIONS:
            try:
                with warnings.catch_warnings():
                    warnings.filterwarnings('ignore')
                    # print('distribution: ' + str(type(distribution).__name__))

                    params = distribution.fit(data)
                    arg = params[:-2]
                    loc = params[-2]
                    scale = params[-1]
                    

                    pdf = distribution.pdf(x, loc=loc, scale=scale, *arg)
                    sse = np.sum(np.power(y - pdf, 2.0))

                    # print('#SSE: ' + str(sse))

                    self.distributions[str(type(distribution).__name__)] = {
                        'SSE': sse,
                        'params': params,
                        'pdf': pdf
                    }

                    if best_sse > sse > 0:
                        best_distribution = distribution
                        best_params = params
                        best_sse = sse
            except Exception:
                pass

# data = pd.Series(sm.datasets.elnino.load_pandas().data.set_index('YEAR').values.ravel())
# p = PyIDD()
# p.fit(data)
# p.plot()