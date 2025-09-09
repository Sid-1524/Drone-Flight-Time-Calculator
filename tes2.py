capacity=eval(input("Enter capacity - "))
discharge=80
AUW=eval(input("Enter weight - "))
power=eval(input("Enter power in watts/kg - "))
voltage=eval(input("Enter voltage - "))
AAD=AUW*power/voltage
time=capacity*discharge/AAD
print("time of flight for given specs - ", time)
