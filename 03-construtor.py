class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    
    def __str__(self):
        return f'Filme: {self.name}'    
        
movie = Movie("Super Mario Bros", 2023, False, 6.0, 130)
movie2 = Movie("Patos", 2023, False, 6.0, 120)
print(movie.name)
print(movie2.name)


print(movie)
print(movie2)