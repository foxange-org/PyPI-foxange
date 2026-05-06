def is_prime(number:int)->bool:
    if(number<=1): return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def is_composite_number(number:int)->bool:
    if(number<=1): return False
    for i in range(2,number):
        if number % i == 0:
            return True
    return False

def pow(number1:float,number2:float)->float:
    return number1 ** number2

def radical_sign(number:int,inx:int=2)->float:
    return pow(number,(1/inx))

def factor(number:int,key=lambda x: True,recur=False)->list[int]:
    ans:list = []
    limit = int(radical_sign(number)) + 1
    for i in range(1,limit):
        if number % i == 0:
            if key(i):
                ans.append(i)
            j = number // i
            if (i != j and key(j)) or (recur and key(j)):
                ans.append(j)
    return ans

def prime_factors(n: int) -> list[int]:
    if n <= 1:
        return []
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2  
    if n > 1:
        factors.append(n)
    return factors

def sum(*value):
    ans = 0
    for i in value:
        if type(i)==int or type(i)==float:
            ans += i
        elif type(i)==list:
            for j in i:
                ans += j
    return ans

def digit_separation(number:int)->list:
    ans = []
    string = str(number)
    for ch in string:
        ans.append(int(ch))
    return ans

def is_perfect_number(number:int)->bool:
    number2 = sum(factor(number))
    return number2 == 2 * number

def is_excess_number(number:int)->bool:
    number2 = sum(factor(number))
    return number2 > 2 * number

def is_deficit(number:int)->bool:
    number2 = sum(factor(number))
    return number2 < 2 * number

def is_amicable_numbers(number1:int,number2:int)->bool:
    temp_number1 = sum(factor(number1)) - number1
    temp_number2 = sum(factor(number2)) - number2
    return temp_number1 == number2 and temp_number2 == number1

def is_engagements_number(number1:int,number2:int)->bool:
    def sum_without_1_and_self(n):
        return sum(factor(n)) - n - 1
    return sum_without_1_and_self(number1) == number2 and sum_without_1_and_self(number2) == number1

def is_smith_number(number: int) -> bool:
    if number <= 1 or is_prime(number):
        return False
    factors = prime_factors(number)
    sum_factors_digits = sum(digit_separation(f) for f in factors)
    sum_original_digits = sum(digit_separation(number))
    return sum_factors_digits == sum_original_digits

def is_niven_number(number:int)->bool:
    return number % sum(digit_separation(number))==0

def is_moran_number(number:int)->bool:
    if not is_niven_number(number):
        return False
    temp = number // sum(digit_separation(number))
    return is_prime(temp)

def is_self_power_number(number:int)->bool:
    digits = digit_separation(number)
    size = len(digits)
    temp = 0
    for i in digits:
        temp += pow(i,size)
    return temp == number

def is_narcissus_number(number:int)->bool:
    return len(str(number)) == 3 and is_self_power_number(number)

def is_palindrome_number(number:int)->bool:
    temp = digit_separation(number)
    return temp == temp[::-1]

def is_reversible_prime(number:int)->bool:
    if not is_prime(number):
        return False
    rev = int(str(number)[::-1])
    return rev != number and is_prime(rev)

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def isqrt(n: int) -> int:
    if n < 0:
        raise ValueError
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def reverse_int(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev

def bin_to_int(bin_str: str) -> int:
    return int(bin_str, 2)

def int_to_bin(n: int) -> str:
    return bin(n)[2:]

def digits_count(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n:
        count += 1
        n //= 10
    return count

def combination(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    res = 1
    for i in range(1, k + 1):
        res = res * (n - k + i) // i
    return res

if __name__ == "__main__":
    # import time
    # import math
    # start = time.time()
    # print("math's",math.pow(10,34))
    # end = time.time()
    # print(end-start)
    # start =0
    # end = 0
    # start = time.time()
    # print("foxange's",pow(10,34))
    # end = time.time()
    # print(end-start)
    pass