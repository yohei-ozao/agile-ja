# ----これらの関数を変更する必要はありません----

names = ["Nick", "Lewis", "Nikos"]

def contains(name, list_of_names):
    if name not in list_of_names:
        return False
    else:
        return True

def get_name(name, list_of_names):
    if name in list_of_names:
        return name
    else:
        return -1

def add_name(name, list_of_names):
    list_of_names.append(name)
    return name

def add_two(num):
    return num + 2

def divide_by_two(num):
    return num / 2

def greeting(name, num):
    message = f"Hello, {name}. It is {num} degrees warmer today than yesterday"
    print(message)
    return message

# ----ここにコードを書いてください----
def my_assert(expr, msg=None):
    if not expr:
        raise AssertionError(msg if msg else "Assertion failed")

# ----難易度: 富士----

# `contains` 用のテスト `test_contains` を作成してください
def test_contains():
    names = ["Nick", "Lewis", "Nikos"]
    my_assert(contains("Nick", names), "Nick should be in the list")
    my_assert(not contains("John", names), "John should not be in the list")

# `add_name` 用のテスト `test_add_name` を作成してください
def test_add_name():
    names = ["Nick", "Lewis", "Nikos"]
    add_name("John", names)
    my_assert("John" in names, "John should be added to the list")

# `add_two` 用のテスト `test_add_two` を作成してください
def test_add_two():
    my_assert(add_two(3) == 5, "3 + 2 should be 5")
    my_assert(add_two(0) == 2, "0 + 2 should be 2")

# `divide_by_two` 用のテスト `test_divide_by_two` を作成してください
def test_divide_by_two():
    my_assert(divide_by_two(4) == 2, "4 / 2 should be 2")
    my_assert(divide_by_two(5) == 2.5, "5 / 2 should be 2.5")

# `greeting` 用のテスト `test_greeting` を作成してください
def test_greeting():
    msg = greeting("Nick", 5)
    my_assert(msg == "Hello, Nick. It is 5 degrees warmer today than yesterday", "Greeting message is incorrect")

# ----難易度: キリマンジャロ----

# `my_assert` 用のテスト `test_my_assert_false` を作成し、式がFalseと評価されたときに指定したオプションの `msg` を適切に返すかどうかをチェックしてください。
def test_my_assert_false():
    try:
        my_assert(False, "This is a test error message")
    except AssertionError as e:
        my_assert(str(e) == "This is a test error message", "Error message did not match")

# テストを実行する関数
def run_tests():
    test_contains()
    test_add_name()
    test_add_two()
    test_divide_by_two()
    test_greeting()
    test_my_assert_false()
    print("All tests passed!")

# テストを実行
run_tests()