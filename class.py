class dim2vec:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def dist(self):
		return (self.x**2 + self.y**2)**0.5
	def quadrant(self):
		x, y = self.x, self.y
		if(x > 0 and y > 0):
			return 1
		elif(x > 0 and y < 0):
			return 2
		elif(x < 0 and y < 0):
			return 3
		else:
			return 4

x, y = map(int, input().split())
obj1 = dim2vec(x, y)
print(obj1.dist())
print(obj1.quadrant())
		
