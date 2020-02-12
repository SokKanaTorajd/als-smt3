def add_matrix(a,b):
	result = [[0,0,0],
         	[0,0,0],
         	[0,0,0]]
 
	for i in range(len(a)):
		for j in range(len(a[0])):
			result[i][j] = a[i][j] + b[i][j]

	for r in result:
		print(r)

	return a,b

X = [[9,8,7],
    [4,5,6],
    [3,2,1]]

Y = [[7,8,9],
    [6,5,4],
    [1,2,3]]

add_matrix(X,Y)