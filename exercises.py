# Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.
def returnCubes():
    return [x**3 for x in range(int(1001**(1/3))+1)]
        

# Exercise #2
# Get first prime numbers up to 100
def returnPrimesTo100():
    primes = [2]
    for x in range(3,100,2):
        prime = True
        for y in range(2,int(x*(1/2)+1)):
            if x % y == 0:
                prime = False
                break
        if prime: 
            primes.append(x)
    return primes
        

# Exercise 3
# ¶
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
def ageGroup():
    age = int(input("Someone's Age: "))
    if age < 18:
        return 'kids'
    elif age < 66:
        return 'adults'
    else: 
        return 'seniors'

print(ageGroup())