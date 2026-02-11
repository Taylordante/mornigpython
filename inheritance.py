#Parents Class/Super Class/Base Class
class Animal:
    isMammal = True

    def speak(self):
         print("Animal is speaking")

    def move(self):
           print("Animal is moving")
#Child class/Sub Class/Derived Class

class Cat:
      def sound(self):
        print("Cat is Meowing")

      def climb(self):
        print("Cat is climbing a tree")

class Horse:
    hasTail = True

    def neigh(self):
        print("Horse is neighing")

a = Animal()
c = Cat
h = Horse


