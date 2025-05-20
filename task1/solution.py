def strict(func):
    def wrapper(*args):
        annotations = func.__annotations__

        for i, (arg_name, expected_type) in enumerate(annotations.items()):
            if i >= len(args):
                break
            if not isinstance(args[i], expected_type):
                raise TypeError

        return func(*args)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
