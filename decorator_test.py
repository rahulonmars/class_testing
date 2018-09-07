from decorator import star_in_beg, timer

@star_in_beg
def func1():
    print "Name ::"

# @star_in_beg
# def func2(name):
#     print "Name :",name
#     return False

@timer
def func2(name):
    for i in range(10):
        print name,i
    return False

# func1()
func2("Text")
# print "closed"