import math
import time
import random

def transferf(k):
    o=ord(k)
    ep=math.exp2(98**(42.04/o))
    return math.floor(ep)
def ret(val):
    ans=42.04/math.log(math.log(val,2),98)
    return chr(math.floor(ans))

def runner(password):
    amt=[str(transferf(k)) for k in password]
    #print(len(''.join(amt)))
    rev=[ret(int(val)) for val in amt]
    #print(''.join(rev))
    '''
    for i in range(len(password)):
        if rev[i]==password[i]:
            pass
        else:
            print('Wrong')
    '''
for i in range(100):
    '''
    password=''
    for i in range(1000000):
        password+=chr(random.randint(33,125))
    '''
    password=[str(i) for i in range(250000)]
    password=''.join(password)
    timei=time.time()
    runner(password)
    timef=time.time()
    print(f'Program took {timef-timei} seconds to execute')








