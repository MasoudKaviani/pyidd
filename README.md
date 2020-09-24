# PyIDD
Identify the Distribution of your Data <br />
This package helps you for identifing the distribution of your data. For example if you want to know whether your data follow Normal distribution, you can use this package!

## Installation

```
pip install pyidd
```

## Usage
```python
import pyidd
import statsmodels.api as sm

# Load sample dataset (data is an one dimensional array)
data = sm.datasets.elnino.load_pandas().data.set_index('YEAR').values.ravel()

# verbose=0 means silent while fitting and verbose=1 means say anything you do while fitting
p = pyidd.PyIDD(verbose=1)
p.fit(data)

# After fitting, you can get distribution sorted by Sum of Squered Error that fit your data, so the first distribution is the distribution that is closer to your data
p.get_distributions()

# You can also plot distributions and your data to see this visualy. top=10 means that you want to plot top 10 distributions that match your data
p.plot(top=10)

```
<img src="examples/test.png" />
