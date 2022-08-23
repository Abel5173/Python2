def fibonacciSeries(numbers):
    if numbers == 1:
        n = [0]
        return n
    elif numbers == 2:
        n = [0,1]
        return n
    else:
        n = [0, 1]
        i = 1
        while len(n) <= numbers:
            a = n[i-1] + n[i]
            n.append(a)
            i+=1
        return n

n = fibonacciSeries(10)
print(*n)
