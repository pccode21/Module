"""连续质数计算"""
def prime_number(m):
    for i in range(2, m):
        if m % i == 0:
            return False
    return True

def main():
    n = eval(input('Please enter the first number:'))
    n_ = int(n)  # 需要考虑用户输入的数字N可能是浮点数，应对输入取整数
    n_ = n_ + 1 if n_ < n else n_  # 舍去小数部分与原来进行比较
    count = 5
    while count > 0:
        if prime_number(n_):
            if count > 1:
                print(n_, end=',')  # 单行输出，质数间用逗号,分割
            else:
                print(n_, '')  # 最后一个输出后不用逗号
            count -=1
        n_ +=1


if __name__ == '__main__':
    main()
