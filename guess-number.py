import random
r = random.randint(1, 100)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了!')
		break
	else:
		print('猜錯了!')
		if num > r:
			print('比正確答案大')
		else:
			print('比正確答案小')
			