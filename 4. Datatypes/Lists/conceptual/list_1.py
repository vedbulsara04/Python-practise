# Simple program to demonstrate list data type

formula_one_team = ["Mercedes AMG Petronas Formula1 team", "Scuderria Ferrari Formula1 team", "Oracle Red Bull Racing",
                    "Aston Martin Aramco Cognizant F1 Team", "BWT Alpine F1 Team", "McLaren Fromula1 team",
                    "MoneyGram Haas F1 Team", "Alfa Romeo F1 Team Stake", "Scuderia AlphaTauri", "Williams Racing"]

# Printing with reference to indexes.
print(formula_one_team[0])
print(formula_one_team[-5])


all_mercedes_f1_drivers = ["Michael Schumacher", "Nico Rosberg"]             # Old list.
new_merc_drivers = "Lewis Hamilton", "Valtteri Bottas", "George Russell"   # Updating the list
all_mercedes_f1_drivers.append(new_merc_drivers)                             # Appending to the list.

print(all_mercedes_f1_drivers)
