def find_prime_divisors(n):
    divisors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            if is_prime(i):
                divisors.append(i)
    return divisors


def is_prime(i):
    for j in range(2, i//2 + 1):
        if i % j == 0:
            return False
    return True


dct = {}
nums = []
for num in range(0, 4):
    nums.append(int(input("please enter your number: ")))
for num in nums:
    length = len(find_prime_divisors(num))
    dct.update({str(num): length})
print(dct)
print(max(dct, key=dct.get), max(dct.values()))


