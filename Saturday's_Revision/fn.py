def cal_avg (salary):
    total=0
    for i in salary:
        total +=i
    avg=total/len(salary)
    return avg
result=cal_avg([10000,20000,30000,40000,50000])
print(result)