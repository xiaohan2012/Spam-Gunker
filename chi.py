import math

def chi2P(chi, df):
    """Return prob(chisq >= chi, with df degrees of
freedom).

    df must be even.
    """
    assert df & 1 == 0
    # XXX If chi is very large, exp(-m) will underflow to 0.
    m = chi / 2.0
    sum = term = math.exp(-m)
    for i in range(1, df//2):
        term *= m / i
        sum += term
    # With small chi and large df, accumulated
    # roundoff error, plus error in
    # the platform exp(), can cause this to spill
    # a few ULP above 1.0. For
    # example, chi2P(100, 300) on my box
    # has sum == 1.0 + 2.0**-52 at this
    # point.  Returning a value even a teensy
    # bit over 1.0 is no good.
    return min(sum, 1.0)
