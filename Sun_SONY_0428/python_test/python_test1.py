# 定义一个基本的4S店类
class CarStore(object):

    # 仅仅是定义了有这个方法，并没有实现，具体功能，这个需要在子类中实现
    def createCar(self, typeName):
        pass

    def order(self, typeName):
        # 让工厂根据类型，生产一辆汽车
        self.car = self.createCar(typeName)
        self.car.move()
        self.car.stop()


# 定义一个北京现代4S店类
class XiandaiCarStore(CarStore):

    def createCar(self, typeName):
        self.carFactory = CarFactory()
        return self.carFactory.createCar(typeName)


# 定义伊兰特车类
class YilanteCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 定义索纳塔车类
class SuonataCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")


# 定义一个生产汽车的工厂，让其根据具体得订单生产车
class CarFactory(object):

    def createCar(self, typeName):
        self.typeName = typeName
        if self.typeName == "伊兰特":
            self.car = YilanteCar()
        elif self.typeName == "索纳塔":
            self.car = SuonataCar()

        return self.car


suonata = XiandaiCarStore()
suonata.order("索纳塔")
