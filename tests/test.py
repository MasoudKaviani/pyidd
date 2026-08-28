import numpy as np
import pytest

import pyidd


def test_fit_normal_data():
    np.random.seed(42)
    data = np.random.normal(0, 1, 1000)
    p = pyidd.PyIDD(verbose=0)
    p.fit(data)
    assert p.fitted is True
    assert len(p.distributions) > 0


def test_fit_returns_self():
    data = np.random.normal(0, 1, 100)
    p = pyidd.PyIDD(verbose=0)
    result = p.fit(data)
    assert result is p


def test_get_distributions_sorted_by_sse():
    np.random.seed(42)
    data = np.random.normal(0, 1, 500)
    p = pyidd.PyIDD(verbose=0)
    p.fit(data)
    dists = p.get_distributions()
    sses = [d[1]['SSE'] for d in dists]
    assert sses == sorted(sses)


def test_get_distributions_before_fit_raises():
    p = pyidd.PyIDD(verbose=0)
    with pytest.raises(Exception):
        p.get_distributions()


def test_plot_before_fit_raises():
    p = pyidd.PyIDD(verbose=0)
    with pytest.raises(Exception):
        p.plot()


def test_fit_invalid_data_raises():
    p = pyidd.PyIDD(verbose=0)
    with pytest.raises(Exception):
        p.fit("not numeric data")


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
