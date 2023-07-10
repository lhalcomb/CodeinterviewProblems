
def fib(n):
    FibArray = [0,1]
    if n <= 0:
        print("n must be a real number")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fib(n-1) + fib(n-2)
        FibArray.append(temp_fib)
        return temp_fib
    
if __name__ == "__main__":

    print(fib(9))