import functools
import datetime
from types import FunctionType

def profile(something):

    @functools.wraps(something)
    def wrapped(*args, **kwargs):
        if type(something) is type:
            class_methods = [x for x, y in something.__dict__.items() if type(y) == FunctionType]
            for attr_name in class_methods:

                attr = getattr(something, attr_name)
                print(attr.__qualname__ + ' started')
                start = datetime.datetime.now()
                attr(something,*args, **kwargs)
                working_time = datetime.datetime.now() - start
                print('{} finished in {} seconds'.format(attr.__qualname__,
                                                         datetime.timedelta.total_seconds(working_time)))
        else:
            print(something.__qualname__ + ' started')

            start = datetime.datetime.now()
            something(*args, **kwargs)
            working_time = datetime.datetime.now() - start

            print('{} finished in {} seconds'.format(something.__qualname__,
                                                     datetime.timedelta.total_seconds(working_time)))
    return wrapped


@profile
def foo():
    pass

@profile
class Bar:
    def __init__(self):
        pass

foo()
Bar()



