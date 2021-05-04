# 유저 DB 갱신 프로그램

# dictionary 변수 선언
dicUser = {}

# userinfo 함수 선언


def userinfo(comment):
    val = input(comment)  # 값의 입력
    return val


# 함수 호출 & 변수에 값 저장
name = userinfo("이름: ")
age = userinfo("나이: ")
phone = userinfo("연락처: ")

# 딕셔너리 update
# ("name"은 텍스트의 name. 따라서, "naaaame"이 되어도 상관없다. 뒤에 name은 위에서 input값을 받은 변수 값이다.)
dicUser.update({"name": name})
dicUser.update({"age": age})
dicUser.update({"phone": phone})

print(dicUser)  # 생성된 dictionary 출력
