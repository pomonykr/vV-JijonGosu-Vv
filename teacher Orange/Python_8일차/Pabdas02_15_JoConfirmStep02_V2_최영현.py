
import sys
import random

while True:
	b= []

	a = input("4인 이상의 이름을 입력하세요.(종료 : 0) : ").split()
	if '0' in a:
		sys.exit()
	
	if len(a) < 4:
		print("^\t명수를 확인하세요.")
		continue
		
	else:
		while True:
			num = random.randint(1,len(a))		# 1 ~ a의 수 값 num에 넣어줌
			if num not in b:					# b 리스트에 랜덤인 num 숫자가 없다면
				b.append(num)					# b에 비교를 위한 num 넣어줌
			else:
				continue

			if len(b) == len(a):				# a리스트 크기와 채워진 b리스트의 크기가 같다면
				print()
				break							#  18_line while문 빠져나감
	print('='*len(a)*11)
	print("이름 :",end=' ')
	for i in a:
		print(i, end='\t')
	print('이고,')
	print('-'*len(a)*11)
	print("숫자 :",end=' ')
	for i in b:
		print(i,end='\t')
	print("입니다.")
	print('='*len(a)*11,'\n')
