import time
def print_hey(name):
    print(f'Hi, {name}')


def ten_sec_notify():
    print(f'Its been 10 seconds')


if __name__ == '__main__':
    print_hey('PyCharm')
    for i in range(5):
        ten_sec_notify()
        time.sleep(10)