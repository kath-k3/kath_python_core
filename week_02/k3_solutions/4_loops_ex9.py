mult_table = ""

for num in range(1, 11):
    for n in range(1, 11):
        # check out this awesome formatting option with <3 ;)
        mult_table += f"{num * n: <2}|"
    mult_table += "\n"

print(mult_table)
