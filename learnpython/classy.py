class Car(object):
	condition = "new"
	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg = mpg
	def displayCar():
		return "This is a " +self.color+" "+self.model+" with "+str(self.mpg)+" MPG."
myCar = Car("DeLorean", "silver", 88)
print myCar.displayCar
