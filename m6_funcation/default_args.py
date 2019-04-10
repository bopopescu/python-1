def sum_avg(n1=1,n2=100):
    total = 0
    for i in range (n1,n2+1):
        total += i
    avg = total / (n2-n1+1)
    return total,avg
def main():
    total, avg = sum_avg()
    print('sum = {0},average = {1}'.format(total, avg))
    total, avg = sum_avg(n2=2)
    print('sum = {0},average = {1}'.format(total, avg))
    total, avg = sum_avg(10, 150)
    print('sum = {0},average = {1}'.format(total, avg))
    total, avg = sum_avg(100,1000)
    print('sum = {0},average = {1}'.format(total,avg))

main()