all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def start_with_r(item):
    return item.startswith('R')

resulting_names = list(filter(start_with_r,all_names))
print(resulting_names)




