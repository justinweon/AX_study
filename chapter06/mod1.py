#함수정의
def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1-num2

#변수 정의. 관례적으로 대문자로 정의. 왜 ""?


VERSION = "1.0.0"

print("모듈명:", __name__)

result = add(10,20)
print("결과:", result)