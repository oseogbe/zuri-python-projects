class Student:
    # [assignment] Skeleton class. Add your code here
    def _init_(self, name, age, tracks, score):
        self.name, self.age, self.tracks, self.score = name, int(age), tracks, score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        try:
            self.age = int(age)
        except ValueError:
            # if the value passed is not a valid integer raise an error
            print('Please enter a valid value for age')

    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age('ree')
Bob.add_track("UI/UX")
Bob.get_score()