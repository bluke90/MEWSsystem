import datetime
now = datetime.datetime.now()
__now = now.strftime("%Y_%m_%d_%H_%M_%S")
dateT = 1
print(__now)
def add():
    __dateT = "SFE24561FS24gbs52d2456S12"
    with open("MSG_{0}.txt".format(__now), "w") as f:
        f.write("\n check")
add()