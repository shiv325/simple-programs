def isPalindrome(num) :
    strNum = str(num)
    if strNum == strNum[::-1] :
        return True
    return False

def isArmstrong(num) :
    sumCubeDigits = 0
    x = num
    while x > 0 :
        sumCubeDigits += (x % 10) ** 3
        x //= 10
    if sumCubeDigits == num :
        return True
    return False

def isPerfect(num) :
    sumDivisors = 0
    for i in range(1, num // 2 + 1) :
        if num % i == 0 :
            sumDivisors += i
    if sumDivisors == num :
        return True
    return False

n = int(input("Enter Number => "))
if isArmstrong(n) :
    print("Armstrong Number")
if isPalindrome(n) :
    print("Palindrome Number")
if isPerfect(n) :
    print("Perfect Number")
