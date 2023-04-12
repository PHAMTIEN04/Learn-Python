def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generatePrimes(start, end):
    primes = []
    for i in range(start, end+1):
        if isPrime(i):
            primes.append(i)
    return primes

def primeSum(n, m, start=2):
    if m == 1:
        if isPrime(n) and n >= start:
            return [n]
        else:
            return None
    else:
        result = []
        for p in generatePrimes(start, n//m):
            sublist = primeSum(n-p, m-1, p+1)
            if sublist is not None:
                result = [p] + sublist
                break
        if len(result) == m and len(set(result)) == m: # check if all primes are different
            return result
        else:
            return None

M = 3
N = 10

result = primeSum(N, M)
if result is None:
    print("Không tồn tại cách phân tích", N, "thành tổng", M, "số nguyên tố khác nhau.")
else:
    print("Các số nguyên tố sum:", result)