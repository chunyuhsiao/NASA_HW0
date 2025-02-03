from Crypto.Util.number import *
datafile = open("data.txt", "r")
data = datafile.readlines()
p_data = data[0].split(' ')
q_data = data[1].split(' ')
n_data = data[2].split(' ')
phi_data = data[3].split(' ')
e_data = data[4].split(' ')
d_data = data[5].split(' ')
p = int(p_data[2])
q = int(q_data[2])
n = int(n_data[2])
phi = int(phi_data[2])
e = int(e_data[2])
d = int(d_data[2])
datafile.close()
message = int(input('message = '))
d_log = 0
d2bit = []
msb = 1
test = d
while msb < test:
    d_log += 1
    msb *= 2
if msb > test:
    d_log -= 1
    msb //= 2
for i in range(0, d_log + 1):
    if msb <= test:
        d2bit.insert(0, 1)
        test -= msb
        msb //= 2
    else:
        d2bit.insert(0, 0)
        msb //= 2
mod_all_power = [message % n]
for i in range(1, d_log + 1):
    mod_all_power.append((mod_all_power[i - 1] * mod_all_power[i - 1]) % n)
original = 1
for i in range(0, d_log + 1):
    if d2bit[i] == 1:
        original = (original * mod_all_power[i]) % n
binary_data = long_to_bytes(original).decode()
print(binary_data)