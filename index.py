from rsa import *
from helper import *


class App:

    @staticmethod
    def main():
        
        keys = RSA.generateKeys(150)                                                                   
        n1 = int('35C0DF0167CA66E54046F122B74618AC8718AB21DE55F09E7863C68C3DD3BEC265D893D66FF52D',16) 
        e1 = int('10001', 16)                                                                      
        k1, s1 = RSA.sendKey(Helper.generateNumber(250), e1, n1, keys[2], keys[1])
        print('Key:             ' + hex(k1))   
        print('Signature:       ' + hex(s1))
        print('Modulus:         ' + hex(keys[1]))
        print('Public exponent: ' + hex(keys[0]))


App.main()