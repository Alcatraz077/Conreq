"""Capabilities used while in DEBUG, that turn off in production environments."""
from functools import wraps

from conreq.utils.generic import get_debug_from_env

# Helper function for doing nothing
def do_nothing(function=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator(function)


# Helper class for doing nothing
class DoNothing(object):
    def __call__(self, target):
        return target


# Set functionality depending on whether we are in DEBUG=True
if get_debug_from_env():
    from silk.profiling.profiler import silk_profile

    class performance_metrics(silk_profile):
        pass


else:

    class performance_metrics(DoNothing):
        pass
