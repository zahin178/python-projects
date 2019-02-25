

def binsrch(array,number):
    a = True
    counter = 0
    start = 0
    end = len(array)-1
    while a == True:
        counter = counter + 1
        avg = (start + end)//2
        num = array[avg]
        if num == number:
            a = False
            print('The number of iteration',counter)
            return avg
        elif num < number:
            start = avg + 1
        elif num > number:
            end = avg - 1
        if end < start:
            print('Sorry there is no such number in the array')
            a = False
        
    

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
	  41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

print(binsrch(primes,40))
