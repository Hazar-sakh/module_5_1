class House:
    #создаем класс с атрибутами name и numbers_of_floors
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        lof = []
        if 1 <= new_floor < self.number_of_floors:
            lof.append(1)
            print(lof[-1])
            for i in lof:
                if 1 <= i < new_floor:
                    lof.append(i + 1)
                    print(lof[-1])
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
