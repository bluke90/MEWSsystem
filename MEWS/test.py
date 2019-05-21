import time
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import numpy as np
import array
amountStorm = 0
x = 200
y = 25000
q = [0, 10]
p = [0, 1250]
__amountStorm = [0, 0]

def recive():
    global amountStorm
    global x
    global y
    print("101")
    body = "x storm"
    bodyList = list(body)

    if bodyList[0] == "x":
        print("102")
        while True:
            x += 5
            amountStorm += 500
            amountStorm / 4
            amountStorm -= 880
            if amountStorm <= y:
                q[1] += 5
                x += 4
                amountStorm += x
                y += 1
                q.append(x)
            else:
                q[1] -= 5
                y -= 10
                x -= 100
                q.append(y)
                amountStorm -= y
                amountStorm -= x
            print(amountStorm)
            time.sleep(.0005)
            __amountStorm.append(amountStorm)
            if amountStorm == 15304:
                return
            continue
        z = np.array(__amountStorm).reshape((-1, 1))

        print(__amountStorm)
    return(__amountStorm)

recive()
regr = linear_model.LinearRegression()
z = np.array(__amountStorm).reshape((-1, 1))
regr.fit(z, q)
print(z)
print("Coef: \n", regr.coef_)
print("intercept: \n", regr.intercept_)
print(regr.predict(x))


