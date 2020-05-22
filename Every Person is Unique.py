class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
      self.first_name = first_name
      self.last_name = last_name
      self.birth_date = birth_date
      self.job = job
      self.working_years = working_years
      self.salary = salary
      self.country = country
      self.city = city
      self.gender = gender

    def name(self):
        return self.first_name + ' ' + self.last_name

    def age(self):
        current_month = 1
        current_day = 1
        current_year = 2018
        
        year = int(self.birth_date[-4:])
        month = int(self.birth_date.split('.')[1])
        day = int(self.birth_date.split('.')[0])
        
        if month <= current_month and day <= current_day:
            return current_year - year
        else:
            return current_year - year - 1

    def work(self):
        if self.gender == 'unknown':
            return 'Is a ' + self.job
        elif self.gender == 'male':
            return 'He is a ' + self.job
        else:
            return 'She is a ' + self.job
    
    def money(self):
        money = int(self.salary * 12 * self.working_years)
        return "{:,}".format(money).replace(',', ' ')

  
    def home(self):
        return 'Lives in ' + self.city + ", " + self.country
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

   
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
