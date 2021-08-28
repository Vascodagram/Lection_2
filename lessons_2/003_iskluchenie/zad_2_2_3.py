class Worker:
    def __init__(self, name, surname, departament, year_hiring):
        self.name = name
        self.surname = surname
        self.departament = departament
        self.year_hiring = year_hiring

    @staticmethod
    def read_worker():
        name = int('')
        surname = int('')
        departament = int('')
        year_hiring = int('')
        return Worker(name, surname, departament, year_hiring)

