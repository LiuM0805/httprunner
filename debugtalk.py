import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


# 时间戳
def get_request_id():
    return f"HRUN-{int(time.time() * 1000)}"


def sleep(n_secs):
    time.sleep(n_secs)


def expected_status_code(a, b):
    return a + b
