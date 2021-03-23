import os

n = 20
for r in range(10):
    c = n*r
    for i in range(50):
        file = 'r{}-c{}-i{}.cnf'.format(r,c,i)
        os.system('makewff -cnf 3 20 c > {}'.format(file))