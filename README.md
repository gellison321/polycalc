# <p align="center">polycalc
<p align="center">A small program that does basic calculus operations with univariate polynomials.


### <p align="center">[Install From pip](https://pypi.org/project/polycalc/)
```
$ pip install polycalc
```


## <p align="center">IMPLEMENTATION

## <p align="center">Generating Polynomials

$$ a = x^2 + 2x + 3$$

$$ b = 2x^2 + 3x + 4$$

``` python
from polycalc import Polynomial
a = Polynomial([3,2,1])
b = Polynomial([4,3,2])
```
## <p align="center">Accessing the Coefficients
``` python
assert a.co == [3,2,1]
```
## <p align="center">Evaluating Polynomial at x
$$\implies a(2) = 2^2 + 2*2 + 3 = 11$$
``` python
assert a.evaluate(2) == 11
```

## <p align="center">Plotting the polynomial

``` python
import matplotlib.pyplot as plt
import numpy as np
plt.plot([a.evaluate(x) for x in np.arange(-10, 10, 0.1)]);
```

## <p align="center">Adding two polynomials
$$\implies b+a = 3x^2 + 5x + 7$$
``` python
assert b.add(a).co == [7, 5, 3]
```

## <p align="center">Subtracting Polynomials
$$\implies b-a = x^2 + x + 1$$
``` python
assert b.subtract(a).co == [1,1,1]
```

## <p align="center"> Multiplying Polynomials
$$\implies b*a = 2x^4 + 7x^3 + 16x^2 + 17x + 12$$
``` python
assert a.multiply(b).co == [12,17,16,7,2]
```

## <p align="center">Dividing Polynomial by a Scalar
$$\implies b/a = 2x^2 + 3/2x + 1$$
``` python
assert b.scalar_divide(2).co == [2,3/2,1]
```

## <p align="center"> Finding Derivative of Polynomial
$$\implies a'(x) = 2x + 2 $$
``` python
assert a.derive().co == [2,2]
```

## <p align="center"> Any Order Derivative
$$\implies a''(x) = 2$$
``` python
assert a.derive().derive().co == [2]
```

## <p align="center">Finding Antiderivative of a Polynomial
$$ \implies \int a \,dx = \frac{1}{3}x^3 + x^2 + 3x + c $$

``` python
assert  a.antiderive().co == [0,3,1,1/3]
```

## <p align="center">Any Order Antiderivative
$$ \implies \int\int a \, dx\ = \frac{1}{12}x^4 + \frac{1}{3}x^3 + \frac{3}{2}x^2 + c$$
``` python
assert a.antiderive().antiderive().co == [0,0,3/2,1/3,1/12]
```

## <p align="center">Integrate Along the X Axis
$$ \implies \int_{0}^{10} a\, dx = \int a \, dx (10) -  \int a\, dx(0) = 463.333$$
``` python
assert round(a.integrate_x_axis(0,10) ,4 ) == 463.3333
```

## <p align="center">Future Development
    1. Handling negative exponents
    2. Polynomial Division
    3. Solving for roots
    4. Solving for polynominal intersections
    5. Integrating between two curves
    6. Multivariate polynomials
    7. Taylor polynomial expansion - fit to data
