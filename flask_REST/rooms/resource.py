class Rooms:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


rooms = [Rooms(101, 1, 'available', 130),
         Rooms(201, 2, 'sold out', 200),
         Rooms(301, 3, 'sold out', 300),
         Rooms(401, 4, 'available', 100)]
