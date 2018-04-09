# TESTING
- start right away with the [`maxima.py`](maxima.py) function and the corresponding [`maxima_exercise.md`](maxima_exercise.md)
- how do you keep track of the manual testing?


## the agile development workflow
  - add a test for the new functionality
  - implement the new functionality (!) ⟶ yes, *after* implementing the test ;)
  - run test suite ⟶ debug until all tests are green again
  - optimize and/or refactor

## test automation 
  - [`pytest`](http://pytest.org)
  - side effect: trust
  - side effect: faster development cycles
  - side effect: better code

## testing scientific code
  - floating point equality: [`np.isclose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isclose.html), [`np.allclose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)
  - classical reference: [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) ⟶ rewrite for humans: [Why don’t my numbers add up?](http://floating-point-gui.de)

## random bits
  - test simple but general cases
  - test corner cases and boundary conditions
  - numerical fuzzing and the importance of the random seed
  - for learning algorithms, for example to verify that they don't get stuck in local optima:
      - test stability of one optimal solution:
          - start from optimal solution
          - start from little perturbation of optimal solution
      - generate data from the model with known parameters and recover the parameters

