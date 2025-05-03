# calculator_v2.py
# 개선된 계산기 프로그램 만들기
# 여러 숫자를 입력받아 연산을 수행하는 계산기 프로그램

import time
import sys
import math
# 함수 정의
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
# 계산기 사용 설명서
def show_help():
        print("="*75)
        print("                               계산기 사용법")
        print("="*75)
        print()
        print("     1. 원하는 숫자를 입력합니다.")
        print("     2. 연산자를 입력하고 1번과 2번을 원하는 만큼 반복합니다.")
        print("          (예: 5 + 3 * 2 = → 결과: 11)")
        print("     3. 'sqrt' 입력 시 제곱근 계산도 가능합니다. (예: sqrt 4 → 2.0)")
        print("     4. '=' 입력 시 지금까지 입력한 연산의 결과를 보여줍니다.")
        print("     5. 'exit' 입력 시 프로그램이 종료됩니다.")
        print("     6. 계산 결과는 자동 저장됩니다. 'load'로 불러올 수 있습니다.")
        print("     ※. 연산은 순서대로가 아닌 우선순위에 의해 계산됩니다.")
        print("     계산을 시작 하시려면 start를 입력해주세요")
        print()
        print("="*75)
        print()

# 명령어 함수 정리

def commands(cmd):
        if cmd.lower() == "help":
                show_help()
                return True
        elif cmd.lower() == "exit":
                print("프로그램이 3초뒤 종료됩니다.")
                for i in range(3,0,-1):
                        print(f"{i}...")
                        time.sleep(1)
                sys.exit()
                
        elif cmd.lower() == "back":
               return "back"
        return False
        #back 입력해도 초기화면으로 돌아가지 않음

# 카운트다운을 위한 설정

show_help()

while True:
        save = input("숫자를 입력하세요: ")
        if save.lower() == "sqrt":
                num = input("제곱근을 구할 숫자를 입력해주세요: ")
                if commands(num):
                      continue
                try:
                      result = math.sqrt(float(num))
                      print(f"{num}의 제곱근은 {result}입니다.")
                except ValueError:
                      print("음수의 제곱근은 계산할 수 없습니다.")
                except Exception as e:
                      print(f"에러 발생: {e}")
                continue

        cmd_result = commands(save)
        if cmd_result == "back":
                continue
        elif cmd_result:
                continue

        if not save.replace(".", "", 1).isdigit():
                print("숫자만 입력할 수 있습니다!")
                continue


        # 몇 번 입력 받을지 사용자의 선택에 맞기기 위해 반복문 설정

        while True:
                print(f"{save}")
                operator = input("연산자를 입력하세요: ")
                cmd_result = commands(operator)
                if cmd_result == "back":
                        continue
                elif cmd_result:
                        continue
                if operator.lower() == "sqrt":
                        num = input("제곱근을 구할 숫자를 입력해주세요: ")
                        if commands(num):
                              continue
                        try:
                                result = math.sqrt(float(num))
                                print(f"{num}의 제곱근은 {result}입니다.")
                        except ValueError:
                                print("음수의 제곱근은 계산할 수 없습니다.")
                        except Exception as e:
                                print(f"에러 발생: {e}")
                        continue

                if operator == "=":
                        try:
                                result = eval(save)
                                print(f"연산결과는 {save} = {result} 입니다.")
                                end = (input("초기 화면으로 돌아가기 : back\n프로그램 종료하기 : exit\n"))
                                cmd_result = commands(end)
                                if cmd_result == "back":
                                       break
                                elif cmd_result:
                                       continue
                                if commands(end):
                                        continue
                        except ZeroDivisionError:
                                print("0으로 나눌 수 없습니다.")
                        except Exception as e:
                                print(f"에러 발생: {e}")
                        break

                elif operator not in ["+","-","*","/"]:
                        print("올바른 연산자를 입력하세요! ( + - * / = 만 허용)")
                        continue

                print(f"{save}{operator} ")

                while True:
                        number = input("숫자를 입력하세요: ")
                        if number.lower() == "sqrt":
                                num = input("제곱근을 구할 숫자를 입력하세요: ")
                                if commands(num):
                                        continue
                                try:
                                        result = math.sqrt(float(number))
                                        print(f"{num}의 제곱근은 {result}입니다.")
                                except ValueError:
                                        print("음수의 제곱근은 계산할 수 없습니다.")
                                except Exception as e:
                                        print(f"에러 발생: {e}")
                                        continue
                        if commands(number):
                                continue
                        if not number.replace(".", "", 1).isdigit():
                                print("숫자만 입력할 수 있습니다!")
                                continue
                
                        save += operator + number
                        break




        

        
        

