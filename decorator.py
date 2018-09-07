import functools
import timeit

def star_in_beg(func):
    # __doc__ = "doc string"
    @functools.wraps(func)
    def wrapper_star_in_beg(*args, **kwargs):
        print "*"
        # func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_star_in_beg

def timer(func):
    @functools.wraps(func)
    def timer(*args, **kwargs):
        start_time = timeit.default_timer()

        value = func(*args, **kwargs)

        end_time =  timeit.default_timer()
        print "Time taken by {fname} is {time}".format(fname=func.__name__, time = end_time-start_time)
        return value
    return timer
