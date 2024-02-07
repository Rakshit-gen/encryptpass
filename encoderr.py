import random
import math
import numpy as np
import cmath
import time
import hashlib
import os


def solve(a, b, c, d):

    if (a == 0 and b == 0):                     
        return np.array([(-d * 1.0) / c])       

    elif (a == 0):                              

        D = c * c - 4.0 * b * d                       
        if D >= 0:
            D = math.sqrt(D)
            x1 = (-c + D) / (2.0 * b)
            x2 = (-c - D) / (2.0 * b)
        else:
            D = math.sqrt(-D)
            x1 = (-c + D * 1j) / (2.0 * b)
            x2 = (-c - D * 1j) / (2.0 * b)
            
        return np.array([x1, x2])               

    f = findF(a, b, c)                          
    g = findG(a, b, c, d)                       
    h = findH(g, f)                             

    if f == 0 and g == 0 and h == 0:            
        if (d / a) >= 0:
            x = (d / (1.0 * a)) ** (1 / 3.0) * -1
        else:
            x = (-d / (1.0 * a)) ** (1 / 3.0)
        return np.array([x, x, x])              

    elif h <= 0:                               

        i = math.sqrt(((g ** 2.0) / 4.0) - h)  
        j = i ** (1 / 3.0)                      
        k = math.acos(-(g / (2 * i)))          
        L = j * -1                             
        M = math.cos(k / 3.0)                   
        N = math.sqrt(3) * math.sin(k / 3.0)    
        P = (b / (3.0 * a)) * -1                

        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

        return np.array([x1, x2, x3])          

    elif h > 0:                                 
        R = -(g / 2.0) + math.sqrt(h)          
        if R >= 0:
            S = R ** (1 / 3.0)                  
        else:
            S = (-R) ** (1 / 3.0) * -1          
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))                
        else:
            U = ((-T) ** (1 / 3.0)) * -1        

        x1 = (S + U) - (b / (3.0 * a))
        x2 = -(S + U) / 2 - (b / (3.0 * a)) + (S - U) * math.sqrt(3) * 0.5j
        x3 = -(S + U) / 2 - (b / (3.0 * a)) - (S - U) * math.sqrt(3) * 0.5j

        return np.array([x1, x2, x3])           

def findF(a, b, c):
    return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0

def findG(a, b, c, d):
    return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a **2.0)) + (27.0 * d / a)) /27.0

def findH(g, f):
    return ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)
def func_encoder(k):
    p=ord(k)
    for u in range(2,ord(k)):
        p+=ord(k)*u
    return p

def func_decoder(p):
    return chr(math.ceil(-1*solve(1,-1,0,2*p)[0].real))


def encode(a):
    s=[func_encoder(i) for i in a]
    s=s[::-1]
    s=[str(t) for t in s]
    s=''.join(s)
    return s

def decode(b):
    b=[b[j:j+6] for j in range(0,len(b)-5,6)]
    b=b[::-1]
    ans=[func_decoder(int(d)) for d in b]
    return ''.join(ans)
def runner(password):
    for i in password:
        if i in '[@_!$%^&*()<>?/\|}{~:]# ' or i.isdigit():
            print('Invalid Password')
            break
    else:
        valll=encode(password)
        print(encode(password))
        #print(decode(encode(password))==password)
        print(decode(encode(password)))

'''
while 1==1:
    password=input('')
    runner(password)
'''
    

#--------------------------------------------------------------------#

def hashh(password):
    salt = os.urandom(32)
    hash_object = hashlib.sha256()
    hash_object.update(salt + password.encode())
    hashed = hash_object.hexdigest()
    return hashed

while 1==1:
    print(hashh(input('')))

#------Test----#
'''
for i in range(100):
    p=''
    for u in range(10000):
        j=chr(random.randint(65,90))
        p+=j
    y=time.time()
    runner(p)
    h=time.time()
    print(f'Time required by myalgo : {h-y}')
    u=time.time()
    hashh(p)
    uv=time.time()
    print(f'Time required by hashing : {uv-u}')
'''





