"""随机密码生成"""
import random

def gen_pwd(length):
    a = random.randint(pow(10, length - 1), pow(10, length))
    return a


def main():
    random.seed(18)
    # 我们调用 random.random() 生成随机数时，每一次生成的数都是随机的。
    # 但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，
    # 如这里的18，这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。
    length = eval(input('Please inter the number of digits for the password:'))
    # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    for _ in range(3):
        print(gen_pwd(length))


if __name__ == '__main__':
    main()
