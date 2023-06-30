#!/usr/bin/python3


def isWinner(x, nums):


    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


    def calculatePrimes(n):
        primes = []
        for i in range(2, n + 1):
            if isPrime(i):
                primes.append(i)
        return primes


    def canWin(n, primes):
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for prime in primes:
                if i - prime < 0:
                    break
                if not dp[i - prime]:
                    dp[i] = True
                    break
            else:
                continue
            break
        return dp[-1]

    winners = []
    for n in nums:
        primes = calculatePrimes(n)
        if canWin(n, primes):
            winners.append("Maria")
        else:
            winners.append("Ben")

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
