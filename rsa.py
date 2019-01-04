from helper import *

class RSA:
    @staticmethod
    def encrypt(m,e,n):
        return (m ** e) % n
    
    @staticmethod
    def decrypt(c,d,n):
        return (c ** d) % n
    
    @staticmethod
    def sign(m,d,n):
        return (m ** d) % n
    
    @staticmethod
    def verify(s,e,n):
        return (s ** e) % n

    @staticmethod
    def sendKey(k,e1,n1,d,n):
        return [ RSA.encrypt(k, e1, n1), RSA.encrypt(RSA.sign(k, d, n), e1, n1) ]

    @staticmethod
    def receiveKey(k1,s1,d1,n1,e,n):
        k = RSA.decrypt(k1, d1, n1)
        if  RSA.verify(RSA.decrypt(s1, d1, n1), e, n) == k:
            return k

    @staticmethod
    def oiler(p,q):
        return ( p - 1 ) * ( q - 1 )

    @staticmethod
    def generateKeys(length):
        p = Helper.getPrimeNumber(length)
        q = Helper.getPrimeNumber(length)
        
        n = p * q
        
        oiler = RSA.oiler(p,q)
    
        e = 2 ** 16 + 1

        d = Helper.AEA(e,oiler)[1] % oiler
        
        return [e,n,d]