"""
Creates a list of factors for any given positive integer.
"""

num = int(raw_input('Please enter a number: '))

def factor_tree(num):
    i = 2
    L1 = []
    while i**2 <= num:
        while num % i == 0: #Locates smallest and largest factors of num
            if num == 2 or i**2 == num:
                L1.append([i,i])
                break
            print 'i =', i
            num = num / i #Assigns largest factor to num
            L1.append([i,num])
            print 'num =', num
        i += 1
    if not L1: #Kicks in only if num is prime
            L1.append([1,num])
    return L1

print factor_tree(num)
