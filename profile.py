import functools
import datetime
from types import FunctionType


def profile(something):
    @functools.wraps(something)
    def wrapped(*args, **kwargs):
        print(something.__qualname__ + ' started')

        start = datetime.datetime.now()
        something(*args, **kwargs)
        working_time = datetime.datetime.now() - start
        print('{} finished in {} seconds'.format(something.__qualname__, datetime.timedelta.total_seconds(working_time)))

    return wrapped


def profile_for_klass(klass):
    class_methods = [x for x, y in klass.__dict__.items() if type(y) == FunctionType]
    for attr_name in class_methods:
        attr = getattr(klass, attr_name)
        setattr(klass, attr_name, profile(attr))
    return klass


@profile
def foo():
    pass

@profile_for_klass
class Bar:
    def __init__(self):
        pass

foo()
Bar()



