a = """ """  # Paste the multiline input here
a = list(map(int, a.split()))
t = 0
for i in range(1, len(a)):
	if (a[i]>a[i-1]):
		t+=1
print("P1:", t)
t = 0
for i in range(3, len(a)):
	if (a[i]>a[i-3]):
		t+=1
print("P2:", t)
