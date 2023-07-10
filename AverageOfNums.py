#Average of the list of the numbers 

"""def average(lst):
    return sum(lst) // len(lst)

lst = [1,2,3,4,5,6,7,8]
average = average(lst)"""

def Average(lst):
    sumoflist = 0 
    for i in range(len(lst)):
        sumoflist += lst[i]
    average = sumoflist//len(lst)
    return average

lst = [1,2,3,4,5,6,7,8]
average = Average(lst)

if __name__ == "__main__":

    print(average)