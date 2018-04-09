## Deceivingly simple function
The file [`maxima.py`](maxima.py) contains a function, `find_maxima`, that finds local maxima in a list and returns their indices. Please read the last sentence again: it returns the *indices*, not the *values*. ;)

1. Test the function with these input arguments and others of your own invention until you are satisfied that it does the right thing for typical cases (remember that the function returns the indices of the maxima):
   
    ```python
    x = [0, 1, 2, 1, 2, 1, 0]
    x = [-i**2 for i in range(-3, 4)]
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    ```

2. Now try with the following inputs:
   ```python
   x = [4, 2, 1, 3, 1, 2]
   x = [4, 2, 1, 3, 1, 5]
   x = [4, 2, 1, 3, 1]
   ```
3. You may think that the code is now clean and robust... Look at the output of the function for the input list
    
    ```python
    x = [1, 2, 2, 1]
    ```
    Does the output correspond to your intuition? Think about a reasonable default behavior in this situation, and meditate on how such a simple function can hide so many complications

4. Implement the “reasonable behavior” you conceived in c), adding a new test.
   Make sure that your function handles these inputs correctly (include them in the tests):
   ```python
   x = [1, 2, 2, 3, 1]
   x = [1, 3, 2, 2, 1]
   x = [3, 2, 2, 3]
   ```
