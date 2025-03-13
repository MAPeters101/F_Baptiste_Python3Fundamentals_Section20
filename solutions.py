'''
Question 1
Your code uses a few functions in the math module here and there, but you also
tend to use the sin, cos and tan functions and the pi constant very frequently.

Write some import statements that you think would be helpful in this scenario.

Solution
First we'll import the math module itself, so we can use functions in there by
prefixing the module name:

import math
So now we can access functions such as sin or gcd this way:

math.sin(math.pi)
math.gcd(10, 5)
But since we use pi, sin, cos, and tan very frequently it might be nice not to
have to always use the module name prefix - so, we'll import those symbols
explicitly as well:

from math import pi, sin, cos, tan
And now we can use those symbols directly:

sin(pi)
As well as retain the ability to reach into the math module for other
functions:

math.asin(1)
Question 2
There is a library that we installed for our course called matplotlib.

We can certainly import that library using its full name, but whenever we need
to reach into that module we need to type out matplotlib.som_func - since we
use this library quite often, typing out matplotlib every time gets tiring.

Write an import function that allows you to reference that module using the
name mpl instead of the full name matplotlib.

Solution
For this, we simply need to alias the module when we import it:

import matplotlib as mpl
And now we can use the name mpl instead of the full original matplotlib name.
'''