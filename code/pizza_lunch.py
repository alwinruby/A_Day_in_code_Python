# Pizza Lunch Program

table_occupancy = {
    'Chair #1': 'empty',
    'Chair #2': 'empty',
    'Chair #3': 'empty',
    'Chair #4': 'empty',
}

# Loop through the dictionary's key :value pairs
for chair, status in table_occupancy.items():
    print(chair +  " is " + status)

print("\nThis table is empty, lets eat here!\n")

# Loop through the dictionary's keys only
for chair in table_occupancy.keys():
    table_occupancy[chair] = 'taken'
    print(chair + " is now " + table_occupancy[chair])

print("\nThe Pizza is delicious!")