


class Student:

    def stdAddress(self):
        print('Muthu')
    def stdPincode(self):
        print(600002)
    def lunch(self):
        print('Meals')


class Staff(Student):
    def lunch(self):
        super().lunch()
        print('Idly')


Staff().lunch()