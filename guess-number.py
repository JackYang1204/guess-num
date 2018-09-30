import random
r = random.randint(1, 100)
i = 0
while True:
	i += 1  #等於 i = i + 1
	num = input('請猜數字: ')
	num = int(num)
	print('進行第', i, '次猜測')
	if num == r:
		print('猜對了!')
		break
	else:
		print('猜錯了!')
		if num > r:
			print('比正確答案大')
		else:
			print('比正確答案小')
			