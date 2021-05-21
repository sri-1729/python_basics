n, k = map(int, input().split())
arr = list(map(int, input().split()))
l, r, count = 0, n - 1, 0
while(l < r):
	if(arr[l] + arr[r] == k):
		count = count + 1
		l+=1
		r-=1
	elif(arr[l] + arr[r] < k):
		l+=1
	else:
		r-=1
print(count)
		
	

