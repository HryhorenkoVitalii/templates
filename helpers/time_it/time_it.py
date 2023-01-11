import time
from datetime import datetime
from collections import defaultdict

class TimeIt():
    '''Execute time '''
    def __init__(self, logger=None, msg=None, print_stout: bool=True):
        self.logger = logger
        self.msg = msg
        self.print_stout=print_stout

    def __enter__(self):
        self.time_start = time.time()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        msg_time = self._time_form(time.time()-self.time_start)
        result_msg = f"{self.msg} :: {msg_time}" if self.msg else msg_time
        if self.logger:
            self.logger(result_msg)
        if self.print_stout:
            print(result_msg)

    def _time_form(self, time):
        result = ""
        if time <= 60:
            result["seconds"] = time
            return str(result)
        result["minutes"] = int(time // 60)
        result["seconds"] = (time) % 60
        if result["minutes"] > 60:
            result["hours"] = int(result["minutes"] // 60)
            result["minutes"] = result["minutes"] % 60
            if result["hours"] > 24:
                result["days"] = int(result["hours"] // 24)
                result["hours"] = result["hours"] % 24
        return str(result)

     
def time_it_decorator(logger=None, msg=None):
    def time_it(func):
        def function_wrapper(*args, **kwargs):
            with TimeIt(logger=logger, msg=msg):
                result = func(*args, **kwargs)
                return result
        return function_wrapper
    return time_it
