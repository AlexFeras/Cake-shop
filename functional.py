from Base import*

class Simplebiscuits():
    def __init__(self,quantity,name):
        self.name=name
        self.quantity = quantity#задаваемое количество печенья
    @classmethod #сам класс имеет метод, а не его объект
    def cook_and_safe(self,quantity,name): #рецепт, каждый раз,когда есть нужное количество ингридиентов,печём печенье
        if a.query(Atem).filter(Atem.id==1).first()>=a.query(Item).filter(Item.flour)*self.quantity \
                and a.query(Atem).filter(Atem.id==2).first() >= a.query(Item).filter(Item.yeast)*self.quantity \
                and a.query(Atem).filter(Atem.id==3).first() >= a.query(Item).filter(Item.margarine)*self.quantity \
                and a.query(Atem).filter(Atem.id==4).first() >= a.query(Item).filter(Item.sugar) * self.quantity:
            k = a.query(Item).filter(Item.name == name).first()#ищем место на складе дл этого печенья
            k.quantity += self.quantity  # если все условия выполнены, то печём заданное количество && складываем выпечку на склад
            k=self.__init__(quantity,name) #возвращаем объект класса
            k.use_resourses()#применяем к каждому объекту метод use_resourses
            return k
    def use_resourses(self,session):
        tmp=["Мука","Маргарин","Сахар"]
        tmp_eng=["flour","margarine","yeast"]
        for i in  range(len(tmp)):#все ресурсы которые в tmp
            k = session.query(Atem).filter(Atem.name==tmp[i]).first()
            k.quantity = k.quantity - self.__dict__[tmp_eng[i]] * self.quantity
        session.commit()
        # TODO
    def __str__(self):# не работает
        return f'Печенек приготовлено-{k}'

class SimpleCake():
    def __init__(self,quantity,name):
        self.name=name
        self.quantity = quantity#задаваемое количество печенья
    @classmethod
    def cook_and_safe(self,quantity,name): #рецепт, каждый раз,когда есть нужное количество ингридиентов,печём печенье
        if a.query(Atem).filter(Atem.id==1).first()>=a.query(Item).filter(Item.flour)*self.quantity \
                and a.query(Atem).filter(Atem.id==2).first() >= a.query(Item).filter(Item.yeast)*self.quantity \
                and a.query(Atem).filter(Atem.id==3).first() >= a.query(Item).filter(Item.margarine)*self.quantity:
            k = a.query(Item).filter(Item.name == name).first()
            k.quantity += self.quantity
            k=self.__init__(quantity,name)
            k.use_resourses()
            return k
    def use_resourses(self,session):
        tmp = ["Мука", "Маргарин", "Сахар"]
        tmp_eng = ["flour", "margarine", "yeast"]
        for i in range(len(tmp)):  # все ресурсы которые в tmp
            k = session.query(Atem).filter(Atem.name == tmp[i]).first()
            k.quantity = k.quantity - self.__dict__[tmp_eng[i]] * self.quantity
        session.commit()

