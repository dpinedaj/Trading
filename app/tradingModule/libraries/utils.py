from functools import wraps

class Utils:

    @staticmethod
    def try_exc(f):
        @wraps(f)
        def new_function(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as exc:
                print('Error:', str(exc))
        return new_function

    @staticmethod
    def try_exc_none(f):
        @wraps(f)
        def new_function(*args, **kwargs):
            value = None
            try:
                value = f(*args, **kwargs)
            except Exception as exc:
                print('Error:', str(exc))

            return value
        return new_function
