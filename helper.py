import random,math

class Helper:

    @staticmethod
    def generateNumber(length,exact = True):
        number = ""

        for _ in range(length - 1):
            number += str(random.randint(0,1))

        number = ''.join(('1', number))

        
        return int(number,2)

    @staticmethod
    def generatePrimeNumber(length, k = 20):
        n = Helper.generateNumber(length)

        while not Helper.testMiller(n,k):
            n += 2

        return n 

    @staticmethod
    def testMiller(p,k):    
        temp = p - 1           
        s = 0
        while temp % 2 == 0:
            temp //= 2
            s += 1
        d = temp
        x = 0
        for _ in range(k):
            x = random.randint(2, p - 1)
            if Helper.AEA(x, p)[0] == 1:
                if pow(x, d, p) == 1 or pow(x, d, p) == (-1) % p:
                    continue
                else:
                    for r in range (1, s):
                        xr = pow(x, d * pow(2,r), p)
                        if xr == (-1)%p:
                            return True
                        elif xr == 1:
                            return False
                        else:
                            continue
                    return False
            elif Helper.AEA(x, p)[0] > 1:
                return False
        return True


    @staticmethod
    def AEA(n1,n2):
        if n2 == 0:
            return [n1, 1, 0]
        else:
            [gcd, u, v] = Helper.AEA(n2, n1 % n2)
            return [gcd, v, u - n1 // n2 * v]


    