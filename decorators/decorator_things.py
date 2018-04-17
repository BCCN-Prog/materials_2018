import functools

def cacheit(func):
    func.cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        try:
            ans = func.cache[key]
        except TypeError:
            # key is unhashable
            return func(*args, **kwargs)
        except KeyError:
            # value is not present in cache
            ans = func.cache[key] = func(*args, **kwargs)
        return ans
    return functools.update_wrapper(wrapper, func)


@cacheit
def mult(x, w, y=20, z=10):
    k = (x + w *y)**z
    return k

# first call, initialize the cache
out = mult(1, 2, y=30, z=40)

# second call, use the cache
out = mult(1, 2, y=30, z=40)
