class Dog():
  name = ""
  age = 0
  __breed = None
  def __init__(self, dog_name, dog_age, dog_breed):
    self.name = dog_name
    self.age = dog_age
    self.__breed = dog_breed
  def speak(self, sound):
    print(self.name, "says", sound)

  def run(self, speed):
    print(self.name, "runs", speed, "mph")

  def description(self):
    print(self.name, "is a", self.age,  "year old", self.__breed)

  def define_buddy(self, buddy):
    self.buddy = buddy
    buddy.buddy = self


scout = Dog("Scout", 2, "Belgian Malinois")
print(scout) #<__main__.Dog object at 0x0000018882A50FD0> this was the output and I feel this is just the location of where scout is
##print(scout.__breed) # There was an error saying there is no attribute breed, which I think means that the two underscore needs to be removed in class Dog
print(scout.name)
print(scout.age)
#When I removed the two underscores, I did indeed get the breed of the dog like I wanted

scout.speak("woof")
scout.description()
skippy = Dog("Skippy", 3, "Maltese")
skippy.description()
