from Crypto.Util.number import *
datafile = open("data.txt", "r")
data = datafile.readlines()
p_data = data[0].split(' ')
q_data = data[1].split(' ')
n_data = data[2].split(' ')
phi_data = data[3].split(' ')
e_data = data[4].split(' ')
p = int(p_data[2])
q = int(q_data[2])
n = int(n_data[2])
phi = int(phi_data[2])
e = int(e_data[2])
datafile.close()
def getinverse(e0, phi0):
    e1 = e0
    phi1 = phi0
    is_e = e0 > phi0
    a = 1
    b = 0
    c = 0
    d = 1
    while a * e0 + b * phi0 > 1 and c * e0 + d * phi0 > 1:
        if is_e:
            mul = e1 // phi1
            e1 -= phi1 * mul
            a -= c * mul
            b -= d * mul
            is_e = False
        else:
            mul = phi1 // e1
            phi1 -= e1 * mul
            c -= a * mul
            d -= b * mul
            is_e = True
    if is_e == False:
        while a < 0:
            a += phi0
        return a
    else:
        while c < 0:
            c += phi0
        return c
datafile = open('data.txt', 'a')
datafile.write('d = ' + str(getinverse(e, phi)))
datafile.close()