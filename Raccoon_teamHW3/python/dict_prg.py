# 빈 딕셔너리 생성
my_dict = {}

# 키-값 쌍 추가
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'

# 값 가져오기
print(my_dict['name'])  # 출력: 'John'
print(my_dict['age'])   # 출력: 30
print(my_dict['city'])  # 출력: 'New York'

# 딕셔너리의 모든 키와 값 출력
for key, value in my_dict.items():
    print(f'{key}: {value}')

    # 딕셔너리에 특정 키가 있는지 확인
if 'name' in my_dict:
    print('name 키가 존재합니다.')

# 딕셔너리에서 키가 없는 경우 기본값 사용
age = my_dict.get('age', '키가 없습니다.')
print(f'나이: {age}')

# 키-값 쌍 삭제
del my_dict['city']


# 딕셔너리의 키를 반복
for key in my_dict.keys():
    print(key)

# 딕셔너리의 값만 반복
for value in my_dict.values():
    print(value)

# 딕셔너리의 키와 값 모두 반복
for key, value in my_dict.items():
    print(f'{key}: {value}')

# 딕셔너리 메서드 사용
# 딕셔너리의 키를 반복
for key in my_dict.keys():
    print(key)

# 딕셔너리의 값만 반복
for value in my_dict.values():
    print(value)

# 딕셔너리의 키와 값 모두 반복
for key, value in my_dict.items():
    print(f'{key}: {value}')



