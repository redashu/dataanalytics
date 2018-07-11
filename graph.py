#!/usr/bin/python2


import matplotlib.pyplot  as plt
import mpld3

batsm=["virat","dhoni","sachin","ashutoshh"]
run=[100,120,78,98]

bol=["soy","bhazii","asif","morkel"]
avg=[2,6,10,5]

plt.xlabel("playnames")
plt.ylabel("runs")
plt.title("cricker performence chart")
plt.bar(batsm,run,label="batsman")
plt.bar(bol,avg,label="bowlers")
plt.legend()
mpld3.show()





