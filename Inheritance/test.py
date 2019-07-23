class Firstclass():
    def __init__(self, *args, **kwargs):
        print("Initialized init for First Class")
        # return super().__init__(*args, **kwargs)

class Secondclass(Firstclass):
    # pass
    def __init__(self, *args, **kwargs):
        print("Initialized init for Second Class")
        return super().__init__(*args, **kwargs)

class Thirdclass(Firstclass, Secondclass):
    def __init__(self, *args, **kwargs):
        print("Initialized init for Third Class")
        return super().__init__(*args, **kwargs)

if __name__ == "__main__":
    # fc = Firstclass()
    # sc = Secondclass()
    tc = Thirdclass()
    print (Thirdclass.__mro__)