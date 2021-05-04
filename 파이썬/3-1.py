# 과제 3-1)

# 리스트 선언
fruit = ['사과', '오렌지', '포도', '파인애플']
vegetable = ['당근', '호박', '양상추', '브로콜리']


def AddNew(cate, name):  # AddNew 함수
    if cate == "채소":
        if name in vegetable:
            print("이미 등록된 채소입니다.")
        else:
            vegetable.append(name)
    elif cate == "과일":
        if name in fruit:
            print("이미 등록된 과일입니다.")
        else:
            fruit.append(name)
    else:
        print("존재하지 않는 카테고리입니다.")


def GetShowList(vegetable, fruit):  # GetShowList 함수
    print(vegetable, fruit)


# Input 입력
cate = input("등록할 카테고리를 선택해주세요. (과일, 채소): ")
name = input("등록할 상품명을 입력하세요: ")

# 함수 호출
AddNew(cate, name)
GetShowList(vegetable, fruit)
