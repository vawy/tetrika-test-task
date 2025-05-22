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


tests = [
    {
        'input': (1, 2), # a=1, b=2
        'answer': 3,
    },
    {
        'input': (-10, 5), # a=-10, b=5
        'answer': -5,
    },
    {
        'input': (1.5, 2), # a=1.5 (float, а нужен int)
        'answer': None, # Ожидается TypeError
    },
    {
        'input': ("1", 2), # a="1" (str, а нужен int)
        'answer': None, # Ожидается TypeError
    },
    {
        'input': (1,), # Нет b (передан только a)
        'answer': None, # Ожидается TypeError
    },
    {
        'input': (), # Нет ни a, ни b
        'answer': None, # Ожидается TypeError
    },
    {
        'input': (1, 2, 3), # Передано 3 аргумента (a, b, c)
        'answer': None, # Ожидается TypeError
    },
]

if __name__ == '__main__':
    all_passed = True
    for i, test in enumerate(tests):
        try:
            result = sum_two(*test['input'])
            if test['answer'] is not None and result == test['answer']:
                print(f"Test {i} passed")
            else:
                print(f"Test {i} NOT passed: got {result}, expected {test['answer']}")
                all_passed = False
        except TypeError:
            if test['answer'] is None:
                print(f"Test {i} passed (TypeError as expected)")
            else:
                print(f"Test {i} NOT passed: unexpected TypeError")
                all_passed = False
        except Exception as e:
            print(f"Test {i} NOT passed: unexpected {type(e).__name__}: {e}")
            all_passed = False

    if all_passed:
        print('ALL TESTS PASSED')
