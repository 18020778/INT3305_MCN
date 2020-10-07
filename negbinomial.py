import math

def prob(n, p, r):
    return math.comb(n - 1, n - r) * (p ** r) * ((1 - p) ** (n - r))

def infoMeasure(n, p, r):
    return -math.log2(prob(n, p, r))

def sumProb(N, p, r):
    sum = 0.0
    for i in range (r, N + 1):
        sum += prob(i, p, r)
    return sum

    """
    Dãy sum = prob(r,p,r) + prob(r+1,p,r) +...+ prob(N,p,N) = p**r * (1 + p - 1)**(-r) = 1 khi N -> vô cùng
    Như vậy, hàm sumProb có thể kiểm chứng được tổng xác suất của phân bố negbinomial bằng 1
    """

def approxEntropy(N, p, r):
    entropy = 0.0
    for i in range (r, N + 1):
        entropy += prob(i, p, r) * infoMeasure(i, p, r)
    return entropy

    """
    Dãy entropy = prob(1,p,r)*infoMeasure(1,p,r) +...+ prob(N,p,N)*infoMeasure(N,p,N)
    entropy là một dãy dương, tăng và có giới hạn là entropy của biến ngẫu nhiên nhị thức âm
    Do đó khi N càng lớn, hàm approxEntropy sẽ tiến đến entropy của biến ngẫu nhiên nhị thức âm và hàm này có thể dùng để tính xấp xỉ entropy
    """
print(sumProb(1000, 0.5, 4))
