import traceback
import time

def try_except_decorator(logger = None,
                         raise_error: bool=True,
                         max_attempts: int=2,
                         timeout: int=1,
                         print_stout: bool=True,
                         finally_at_error_case: "function"=None):
    def try_exc(func):
        def function_wrapper(*args, **kwargs):
            for attempts in range(1, max_attempts+1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    msg = f"Try except, attempt {attempts}/{max_attempts} :: {func.__name__}\n {traceback.format_exc()}"
                    _error_message(logger, msg, print_stout)
                    if attempts == max_attempts: 
                        if finally_at_error_case:
                            finally_at_error_case()
                        if raise_error:
                            raise
                    time.sleep(timeout)

        return function_wrapper
    return try_exc

def _error_message(logger, msg , print_stout):
    if print_stout:
        print(msg)
    if logger:
        logger.error(msg)
