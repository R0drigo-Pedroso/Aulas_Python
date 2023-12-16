import os

# help('os')

# 1 Desligar o ocmputador
# os.system("shutdown /s") # Deligar o computador em 60s
# os.system("shutdown /s /t 0") # Deligar o computador imediatamente
# os.system("shutdown now") # Linux


# - 2 Concelar desligamento
# os.system("shutdown /a")

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")


def turn_off_s_hour():
    os.system("shutdown /s")


def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800")


def cancel_shutdown():
    os.system("shutdown /a")


""" turn_off_one_hour()
cancel_shutdown()
turn_off_half_an_hour()
 """

turn_off_s_hour()
# cancel_shutdown()
