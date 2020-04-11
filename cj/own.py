import time


def set_tag(tag='my'):        # 由于此装饰器需要参数，所以要再套一层
    def my_decorator(func):    # 装饰器的核心，接受函数对象做参数，返回包装后的函数对象
        def my_wrapper(*arg, **kvargs):    # 包装的具体过程
            sign = "<" + tag + ">"
            return sign + func(*arg, **kvargs) + sign
        return my_wrapper
    return my_decorator


def now_time(func): # 打印当前时间
    def wrapper(*args, **kwargs):
        print(time.ctime())
        return func(*args, **kwargs)

    return wrapper


# 打印函数时间装饰器
def run_time(func): # 打印时间
    def inner(*args, **kwargs):
        old_time = time.time()
        result = func(*args, **kwargs)
        func_name = str(func).split(' ')[1]
        print('{} use time: {}s'.format(func_name, time.time() - old_time))
        return result

    return inner


@run_time    # 用@标签在定义函数时套上装饰器
def hello(name='CJ'):
    time.sleep(2)
    return 'hello ' + name


if __name__ == '__main__':
    print(hello())
