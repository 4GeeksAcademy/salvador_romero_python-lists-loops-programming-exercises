incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
def concatenate(row):
    return row["name"]+" "+row["last_name"]

def data_transformer(my_list):
        return (list(map(concatenate,my_list)))

print(data_transformer(incoming_ajax_data))