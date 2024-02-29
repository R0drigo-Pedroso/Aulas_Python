class Movie: 
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0
    
# Primeiro filme
movie = Movie()
movie.name = "Super Mario Bors"
movie.yearLaunch = 2023
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 130

# Segundo Filme
patos = Movie()
patos.name = "Patos"
patos.yearLaunch = 2022
patos.includedPlan = False
patos.note = 5.0
patos.durationMinutes = 120

print("## Dados do Filme##\n")
print(f'Nome do filme: {movie.name}\nAno do Lançamento {movie.yearLaunch}\n')
print(f'Nome do filme: {patos.name}\nAno do Lançamento {patos.yearLaunch}\n')