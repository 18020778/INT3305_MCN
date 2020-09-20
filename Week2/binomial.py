import math

def prob(n, p, N):
    return math.comb(N, n) * (p**N)

def infoMeasure(n, p, N):
    return -math.log2(prob(n, p, N))

def sumProb(N, p):
    sum = 0.0
    for i in range (1, N + 1):
        sum += prob(i, p, N)
    return sum

    """
    Dãy sum = prob(1,p,N) + prob(2,p,N) +...+ prob(N,p,N) = (p + 1 - p)**N = 1
    Như vậy, hàm sumProb có thể kiểm chứng được tổng xác suất của phân bố binomial bằng 1
    """

def approxEntropy(N, p):
    entropy = 0.0
    for i in range (1, N + 1):
        entropy += prob(i, p, N) * infoMeasure(i, p, N)
    return entropy

    """
    Các symbol của biến ngẫu nhiên nhị thức là hữu hạn, do đó entropy cũng hữu hạn (bị chặn trên)
    Khi N càng lớn thì approxEntropy(N, p) càng xấp xỉ với entropy nên hàm này cho phép tính xấp xỉ entropy.
    """

print(approxEntropy(100, 0.5))