# codeup 6022번 문제

# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.
# 년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력한다.

# codeup 6022번 풀이

yymmdd = input()
print(f"{yymmdd[0:2]} {yymmdd[2:4]} {yymmdd[4:6]}")