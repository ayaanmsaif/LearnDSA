import time 

start = time.time() 

def fibonacci2(n): 
    fibNumbers = [0,1]
    for i in range(2, n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    return fibNumbers[n]

fibonacci2(10)

end = time.time()

time = end - start
print(time)



