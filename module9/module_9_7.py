

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, result):
            if result % i == 0:
                print('Составное')
                return result
        print('Простое')
        return result

    return wrapper

@is_prime
def sum_three(first, second, third):
    return first + second + third

res = sum_three(2, 3, 6)
print(res)
