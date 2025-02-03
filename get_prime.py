from Crypto.Util.number import *
p = getPrime(2048)
q = getPrime(2048)
n = p * q
n_log = 0
msb = 1
test = n
while msb < test:
    n_log += 1
    msb *= 2
if msb > test:
    n_log -= 1
while n_log != 4095:
    p = getPrime(2048)
    q = getPrime(2048)
    n = p * q
    n_log = 0
    msb = 1
    test = n
    while msb < test:
        n_log += 1
        msb *= 2
    if msb > test:
        n_log -= 1
phi = (p - 1) * (q - 1)
e = 65537
datafile = open('data.txt', 'w')
datafile.write('p = ' + str(p) + ' \nq = ' + str(q) + ' \nn = ' + str(n) + ' \n')
datafile.write('phi = ' + str(phi) + ' \ne = ' + str(e) + ' \n')
datafile.close()
