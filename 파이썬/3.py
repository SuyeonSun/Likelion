# 과일채소 프로그램

# 리스트 선언
fruit = ["사과", "오렌지", "포도", "파인애플"]
vegetable = ["당근", "호박", "양상추", "브로콜리"]

# cate 입력
cate = input("등록할 카테고리를 선택해주세요. (과일, 채소): ")
# name 입력
name = input("등록할 상품명을 입력하세요: ")

# 채소인 경우
if cate == "채소":
    if name in vegetable:  # 등록한 값이 vegetable 리스트 안에 있다면
        print("이미 등록된 채소입니다.")
    else:  # 등록한 값이 vegetable 리스트 안에 없다면
        vegetable.append(name)  # append 사용해서 vegetable 리스트에 값을 추가
# 과일인 경우
elif cate == "과일":
    if name in fruit:  # 등록한 값이 fruit 리스트 안에 있다면
        print("이미 등록된 과일입니다.")
    else:  # 등록한 값이 fruit 리스트 안에 없다면
        fruit.append(name)
# 채소와 과일 모두 아닌 경우
else:
    print("존재하지 않는 카테고리입니다.")

print(fruit, vegetable)  # 최종 리스트 출력
