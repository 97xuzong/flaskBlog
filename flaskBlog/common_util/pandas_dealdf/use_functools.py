import functools

# 累积函数
print(functools.reduce(lambda x, y: x + y, [i for i in range(101)]))


# 装饰器  无完全伪装 返回的是另外一个函数对象
def wrapper(func):
    def inner(*args, **kwargs):
        '''包装函数注解'''
        print("开始扩展")
        res = func(*args, **kwargs)
        print("扩展结束")
        return res

    return inner


@wrapper
def func1(name):
    '''真实函数注解'''
    print(f"{name}在扩展功能")


func1("张三")
print(func1.__name__, func1.__doc__)

print("---------------------")


# -------------使用@functools.wraps()实现完全伪装--------------------
def wrapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        '''包装函数注解'''
        print("开始扩展")
        res = func(*args, **kwargs)
        print("扩展结束")
        return res

    return inner


@wrapper
def func1(name):
    '''真实函数注解'''
    print(f"{name}在扩展功能")


func1("张三")
print(func1.__name__, func1.__doc__)
