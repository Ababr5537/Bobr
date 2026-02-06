class TrafficLight:
    def __init__(self, location):
        self.location = location
        self.color = "червоний"

    def change_color(self, new_color):
        self.color = new_color
        print(f"На {self.location} тепер колір: {self.color}")

light1 = TrafficLight("Перехрестя Соборної")
light2 = TrafficLight("Вулиця Лесі Українки")

light1.change_color("зелений")
light2.change_color("жовтий")
