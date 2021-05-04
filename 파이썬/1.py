# 시험 점수 자동 채점 프로그램
cut = 65
maximum = 100
minimum = 0

# 점수 입력
num1 = int(input("창사코:"))
num2 = int(input("선형대수:"))
num3 = int(input("컴퓨터공학:"))

print(num1, num2, num3)  # 점수 출력

if num1 > maximum or num2 > maximum or num3 > maximum:  # 하나라도 100을 넘는 숫자가 있다면
    print("잘못된 점수가 입력되었습니다.")
elif num1 < minimum or num2 < minimum or num1 < minimum:  # 하나라도 0보다 작은 숫자가 있다면
    print("잘못된 점수가 입력되었습니다.")
elif num1 > cut and num2 > cut and num3 > cut:  # 모두 cut 점수 이상이라면
    print("합격입니다!")
else:  # 모두 cut 점수 이상을 만족하지 못한다면
    print("불합격입니다. 재수강하세요.")
