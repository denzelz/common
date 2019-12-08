class Tenants:
    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number


tenants = [Tenants('Jack', 'AA321912', 25, 'male', {'city': 'New York', 'street': 'Wall street 43'}, 101),
          Tenants('Lory', 'AB435261', 32, 'male', {'city': 'Chicago', 'street': 'Washington street 28'}, 223),
          Tenants('Mike', 'AH151683', 57, 'female', {'city': 'Los Angeles', 'street': 'Hollywood street 43'}, 411),
          Tenants('Jena', 'NV612618', 62, 'female', {'city': 'Texas', 'street': 'Rodeo street 34'}, 324)]
