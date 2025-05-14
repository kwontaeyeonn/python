class Memberinfo:
	def __init__(self,id,password,name):
		self.id = id
		self.password = password
		self.name = name
			
	def getMember(self):
		return f'{self.id},{self.password},{self.name}'


my_member  = Memberinfo("king",'123456','홍길동')
print(my_member.getMember())