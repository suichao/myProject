import socket
import time
from line_profiler import LineProfiler


def get_host_ip():
    """
    获取服务器ip

    shell脚本:
    python - c \"import socket;print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s
    in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])\"
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    print(ip)
    return ip


class Timer(object):

    @classmethod
    def total_time(cls, fun):
        def wrapper(*args, **kwargs):
            s = time.time()
            fun(*args, **kwargs)
            e = time.time()
            print(f"function {fun.__name__} spend {round(e - s, 3)} seconds")
        return wrapper

    @classmethod
    def line_detail(cls, fun):
        def wrapper():
            lpf = LineProfiler(fun)
            lpf.run(fun.__name__)
            lpf.print_stats()
        return wrapper

    LineDetail = line_detail
    TotalTime = total_time
