from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer,String,Boolean
Base=declarative_base()

class Item(Base):
    __tablename__ = "cake1" # описанине рецепта
    id = Column(Integer, primary_key=True)  # обязательно?
    name=Column(String(50))
    quantity = Column(Integer)
    cost = Column(Integer)
    sugar = Column(Integer)
    flour = Column(Integer)  # ингридиенты на 1 кг печенек
    margarine = Column(Integer)
    yeast = Column(Integer)
    beeren = Column(Integer)
    def __init__(self,id,name,quantity,cost,sugar,flour,margarine,yeast,beeren):
        self.id = id
        self.name=name
        self.quantity=quantity
        self.cost=cost
        self.sugar=sugar
        self.flour=flour
        self.margarine=margarine
        self.yeast=yeast
        self.beeren=beeren
    def __str__(self):#без этой строчки не выведет
        return f'{self.name} количество={self.quantity} стоимость={self.cost} необходимый сахар= {self.sugar} необходимая мука= {self.flour} необходимый маргарин= {self.margarine} необходимые дрожжи= {self.yeast} необходимые ягоды= {self.beeren}'

class Atem(Base):
    __tablename__ = "cakeresours"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    name=Column(String(50))
    def __init__(self,id,quantity,name):
        self.id = id
        self.name=name
        self.quantity=quantity
    def __str__(self):
        return f' id {self.id} наименование {self.quantity} количество= {self.name}'
engine=create_engine("sqlite:///C:\\Users\\Win10Pro\\PycharmProjects\\cake_market\\cake.db", echo=True)
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
a=Session()

# a.add(Item(11,"Печенька",1,1,1,1,1,1,1))
# a.add(Item(22,"Булочка",1,1,1,1,1,1,1))
# a.add(Item(33,"Тортик",1,1,1,1,1,1,1))
# a.commit()
#a.add(Item(33,"Тортик",1,1,1,1,1,1,1))
# a.add(Atem(5,1000,"Мука"))
# a.add(Atem(6,1000,"Сахар"))
# a.add(Atem(7,1000,"Маргарин"))
# a.add(Atem(8,1000,"Ягоды"))
# a.add(Atem(9,1000,"Дрожжи"))
# a.add(Atem(10,1000,"Мука"))
# a.commit()

l=a.query(Item).all()#запрос к таблице
for i in l:
    print(i)#вывод через принт всё

l=a.query(Atem).all()#запрос к таблице
for i in l:
    print(i)#вывод через принт всё
# a.add(Item(2,"Булочка",quantity,cost,sugar,flour,margarine,yeast,beeren))

