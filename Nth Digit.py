def findNthDigit(self, n):
    n -= 1		#n-=1是因为n要表示一个相对位置，下面的first + n/digits就是在first基础上的相对位置
    for digits in range(1, 11):
        first = 10**(digits - 1)
        if n < 9 * first * digits:
            return int(str(first + n/digits)[n%digits])
        n -= 9 * first * digits

