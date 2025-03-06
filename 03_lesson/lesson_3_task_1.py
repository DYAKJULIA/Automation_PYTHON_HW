class User:

    def __init__(self, first_name, last_name):
        self.username = first_name
        self.surname = last_name

    def get_name(self):
        return self.username

    def get_surname(self):
        return self.surname

    def get_info(self):
        return (f"Фамилия: {self.surname}, имя: {self.username}")