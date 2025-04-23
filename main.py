#main.py
#계산기 프로그램 만들기
# 두 수를 입력받아 사칙연산을 수행하는 계산기 프로그램
# 사칙연산을 수행하는 함수 정의
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    if b == 0:
        return "0으로 나눌수 없습니다."
    return a / b

# 사용자로부터 두 수와 연산자를 입력받기
num1 = int(input ("첫 번째 숫자를 입력하세요"))
num2 = int(input ("두 번째 숫자를 입력하세요"))
simbol = input("어떤 연산을 할지 선택하세요 +, -, *, /): ")

if simbol == "+":
    
    print(plus(num1, num2))

elif simbol == "-":
    
    print(minus(num1, num2))

elif simbol == "*":
   
    print( multi(num1, num2))

elif simbol == "/":
   
    print( divi(num1, num2))

else:
    print("정확한 기호를 입력하세요.")



