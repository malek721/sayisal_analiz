import math
import sympy as smp


def usAlma(base, k):
    us = 1
    for i in range(k):
        us = base*us
    return us


def faktorial(k):
    num = k
    factor = 1
    for i in range(k):
        factor *= num
        num -= 1
    return factor


def turev(y, n):
    if n == 0:
        return f.subs([(x,y)]).evalf()
    else:
        dfdx = smp.diff(f, x, n)
        return dfdx.subs([(x,y)]).evalf()


x = smp.symbols('x', real=True)
f = smp.cos(x)
toplam = 0

for i in range(1):
    toplam += (turev(0, i)*usAlma((3.14/5), i))/faktorial(i)

kesme_Hatasi = smp.cos(math.pi/5)-toplam
print("kesme Hatasi =" + str("{:.15f}".format(kesme_Hatasi)))

toplam = 0
for i in range(3):
    toplam += (turev(0, i)*usAlma((math.pi/5), i))/faktorial(i)


kesme_Hatasi = smp.cos(math.pi/5)-toplam
print("kesme Hatasi =" + str("{:.15f}".format(kesme_Hatasi)))

