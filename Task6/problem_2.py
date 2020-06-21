 
n, x = list(map(int, input().split()))
n_bosy = 0
for i in range(n):
  s,d = input().split()
  if(s == "+"):
    x += int(d)
  else:
    if(abs(int(d)) > x):
      n_bosy = n_bosy + 1
    else:
      x -= abs(int(d))
 
print(f'{x} {n_bosy}')
