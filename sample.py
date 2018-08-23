def a(**kwargs):
    if kwargs is not None:
        for key,value in kwargs.items():
            print("Key: {}  Value: {}".format(key,value))

a(sample="TEST",sample2="Test2")

a = {a:1,1:2}
print(len(a))