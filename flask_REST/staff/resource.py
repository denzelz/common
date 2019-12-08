class Staff:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


staff = [Staff('Jack', 'AA321912', 'cook', 130),
         Staff('Lory', 'AB435261', 'waiter', 200),
         Staff('Mike', 'AH151683', 'administrator', 300),
         Staff('Greg', 'NV612618', 'waiter', 100)]
