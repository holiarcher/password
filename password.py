i = 0
while i <3:
	psw = input('plz enter your password:')

	if psw == 'a123456':

		print('登入成功')
		break

	n = 2 - i
	print('密码错误!还有',n,'次机会')

	i = i + 1


