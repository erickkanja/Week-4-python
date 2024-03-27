class Person():
  def __init__(self, name, age, gender) :
    self.name = name
    self.age = age
    self.gender = gender
  def introduce(self):
    print("Your name is", self.name, "you are", self.age, "years old and you are a ", self.gender)

person1 = Person("Erick", 20, "male")
person1.introduce()
