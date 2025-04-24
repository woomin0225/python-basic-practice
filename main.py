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

# while 조건문 만들기

while True:

# 사용자로부터 두 수와 연산자를 입력받기
# 연산자 잘못 입력시 되돌아가는 범위 축소

    try:
        num1 = int(input ("첫 번째 숫자를 입력하세요 = "))
        print(f"첫번째로 입력한 숫자는 {num1} 입니다.")
        num2 = int(input ("두 번째 숫자를 입력하세요 = "))
        print(f"두번째로 입력한 숫자는 {num2} 입니다.")
    

        while True:
            simbol = input("어떤 연산을 할지 선택하세요 (예시 : +, -, *, /): ")
            print(f"입력한 연산자는 {simbol} 입니다")

            if simbol == "+":
                print(f"연산 결과는 {num1}{simbol}{num2} = {plus(num1, num2)} 입니다")
                break

            elif simbol == "-":
                print(f"연산 결과는 {num1}{simbol}{num2} = {minus(num1, num2)} 입니다")
                break

            elif simbol == "*":
                print(f"연산 결과는 {num1}{simbol}{num2} = {multi(num1, num2)} 입니다")
                break

            # 사용자에게 자리수 입력 받기

            elif simbol == "/":
                while True:
                    try:
                        decimal = int(input("소수점 몇 번째 자리까지 계산하시겠습니까? (예: 3):"))
                        result = divi(num1, num2)

                        if isinstance(result, str):
                            print(result)
                        else:
                            print(f"연산 결과는 {num1} {simbol} {num2} = {result:.{decimal}f} 입니다")
                        break

                    except ValueError:
                        print("숫자만 입력하세요!")    
                        continue
                break
            else:
                print("정확한 기호를 입력하세요!")
                
    except ValueError:
        print("숫자만 입력하세요!")    
        continue
        

# 계산 완료 후 재실행 유무 묻기

    while True:
        
        try:
            again = input("다시 계산하시겠습니까? (y/n)")

            if again.lower() == "y":
                break

            elif again.lower() == "n" :
                print("프로그램을 종료합니다")
                exit()

            else:
                print("정확한 값을 입력해주세요!")

        except ValueError:
            print("정확한 값을 입력해주세요!")