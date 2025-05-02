# codeup 6020번 문제

# 주민번호는 다음과 같이 구성된다.
# XXXXXX-XXXXXXX
# 주민번호를 입력받아 형태를 바꿔 출력해보자.
# '-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.

# codeup 6020번 풀이

num1,num2 = input().split('-')
print(f"{num1}{num2}")