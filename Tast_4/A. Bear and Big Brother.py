a , b = map(int, input().split())
cnt = 0
while a <= b:
	a = a * 3
	b = b * 2
	cnt = cnt  + 1
print(cnt)
