# 딕셔너리의 리스트 생성
student1 = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student2 = {'name': 'Bob', 'age': 22, 'grade': 'B'}
student3 = {'name': 'Charlie', 'age': 21, 'grade': 'C'}

student_list = [student1, student2, student3]

# 리스트의 딕셔너리 항목 출력
for student in student_list:
    print(f"이름: {student['name']}, 나이: {student['age']}, 학점: {student['grade']}")

# 새로운 학생 추가
new_student = {'name': 'David', 'age': 19, 'grade': 'A'}

student_list.append(new_student)

# 업데이트된 리스트 출력
for student in student_list:
    print(f"이름: {student['name']}, 나이: {student['age']}, 학점: {student['grade']}")

    # 학점이 'A'인 학생 검색
for student in student_list:
    if student['grade'] == 'A':
        print(f"학점 'A' 학생: {student['name']}")

# 나이가 21세 이상인 학생 검색
for student in student_list:
    if student['age'] >= 21:
        print(f"21세 이상 학생: {student['name']}")

