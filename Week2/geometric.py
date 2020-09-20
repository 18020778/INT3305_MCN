import math

def prob(n, p):
    return p*((1-p)**(n-1))*1.0

def infoMeasure(n, p):
    return -math.log2(prob(n, p))

def sumProb(N, p):
    sum = 0.0
    for i in range(1, N + 1):
        sum += prob(i,p)
    return sum

    """
    Dãy sum = prob(1,p) + prob(2,p) +...+ prob(N,p) = 1 - (1-p)**N
    Nếu N càng lớn thì sum càng xấp xỉ 1. 
    Như vậy, hàm sumProb có thể kiểm chứng được tổng xác suất của phân bố geometric bằng 1
    """

def approxEntropy(N, p):
    entropy = 0.0
    for i in range(1, N + 1):
        entropy += prob(i,p) * infoMeasure(n,p)
    return entropy 

    """
    Dãy entropy = prob(1, p) * inforMeasure(1,p) +...+ prob(N, p) * inforMeasure(N, p)
                = log(1/p) * (1-(1-p)**N) + (1-p)/p * log(1/(1-p))
    Khi N tiến tới vô cùng, dãy entropy = log(1/p) + (1-p)/p * log(1/(1-p)) 
    Như vậy khi dãy entropy có giới hạn như trên thì nó xấp xỉ entropy của nguồn tin geometric
    hay approxEntropy xấp xỉ entropy
    """

print (approxEntropy(1000, 0.5)) # xấp xỉ 2  
 