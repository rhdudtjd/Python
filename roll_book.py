student = {}

st = int(input("학생 수를 입력하십시오 : "))

for i in range(st):
    st_num, st_name = input("학번과 이름을 입력하십시오 : ").split()
    student[st_num] = st_name

print("\n입력 완료 되었습니다\n")
choice_num = int(input("(1) 반 명단 확인하기\n(2) 반 학생 수 확인하기\n입력하십시오 : "))
print("")
if choice_num == 1:
    print(student.values())
else:
    print(len(student),"명입니다")

