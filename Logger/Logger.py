import time


def log_request_time(func):
    def wrapper_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        time_diff = time.time() - start
        print("Request Time ⏰ - ", args, " is ", time_diff)
        return result
    return wrapper_func