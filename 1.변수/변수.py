#해당 변수.py 에서는 여러 가지 변수의 정의를 설명을 목적으로 하고 있습니다.

#1. 변수(variable)=====================================================
    #1) 정의 : 어떤 값을 저장하기 위한 메모리 공간
    #2) 변수 선언 규칙
#(1) 변수 이름만 봐도 어떤 변수인지 해석할 수 있어야 함
#(2) 너무 함축적인 별명은 좋지 않음
#(3) 영문 대소문자, _, 숫자를 이용
#(4) 숫자로 시작하면 안 됨
#(5) 파이썬은 미리 변수를 선언하지 않아도 됨
#(6) 하지만 코드가 길면 변수를 미리 선언하는 것이 좋음


#2. 기본적인 변수 선언 및 할당===========================================

# 숫자 변수
num1 = 10
num2 = 3.14

# 문자열 변수
name = "김철수"
message = "안녕하세요!"

# 리스트 변수
fruits = ["사과", "바나나", "오렌지"]

# 튜플 변수
numbers = (1, 2, 3, 4, 5)

# 딕셔너리 변수
person = {"이름": "박지영", "나이": 27, "직업": "개발자"}

# 출력
print(num1, type(num1))  # 10 <class 'int'>
print(num2, type(num2))  # 3.14 <class 'float'>
print(name, type(name))  # 김철수 <class 'str'>
print(message, type(message))  # 안녕하세요! <class 'str'>
print(fruits, type(fruits))  # ['사과', '바나나', '오렌지'] <class 'list'>
print(numbers, type(numbers))  # (1, 2, 3, 4, 5) <class 'tuple'>
print(person, type(person))  # {'이름': '박지영', '나이': 27, '직업': '개발자'} <class 'dict'>

#3. 여러 변수 동시 선언================================================

# 여러 변수 동시 선언 및 할당
x, y, z = 1, 2.5, "Hello"

# 출력
print(x, type(x))  # 1 <class 'int'>
print(y, type(y))  # 2.5 <class 'float'>
print(z, type(z))  # Hello <class 'str'>

#4. 변수 값 변경=======================================================

# 변수 값 변경
num = 10

print(num)  # 10

num = 20

print(num)  # 20

#5. f-string 사용=====================================================

# f-string 사용
name = "김민수"
age = 30

message = f"안녕하세요, {name}님! 당신은 {age}살입니다."

print(message)  # 안녕하세요, 김민수님! 당신은 30살입니다.
