class sample():
    class_variable = 0

    def __init__(self,name):
        sample.class_variable += 1
        print("Class is initialized {} time.".format(sample.class_variable))
        self.fname = name
    def greeting(self):
        print("Hi {} ! Welcome to the class.".format(self.fname))
        print("value of class variable inside greeting of {}: {}".format(self.fname, sample.class_variable))

    # @classmethod
    # def func1(self, **kwargs):
    #     kwargs[0]

class child(sample):
    # def greeting(self, name):
    #     print("Welcome child: ",name)
    def method1(self, input1):
        print ("Value of input 1 is: ",input1)
        #type(a)
        #print("Value of input 1 is: {}".format(input1))

object_child = child("Rahul")

object_child.greeting()
object_child.method1("Input1")



# rahul = sample("Rahul")
# rahul.greeting()
# user1 = sample("User1")
# rahul.greeting()
# user2 = sample("User2")
# rahul.greeting()
# rahul.greeting("rahul")
# rahul.greeting("rahul")
# rahul.greeting("rahul")
# rahul.greeting("rahul")

# user1.greeting("User1")