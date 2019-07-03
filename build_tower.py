def build_tower(n):
	biggest = 2 * n - 1
	return [' '*((biggest-i)//2)+'*'*i +' '*((biggest-i)//2) for i in range(1, biggest+1,2)]
