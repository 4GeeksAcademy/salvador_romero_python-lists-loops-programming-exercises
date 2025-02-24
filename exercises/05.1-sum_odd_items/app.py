my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(my_list):
    sum_odd=0
    for n in my_list:
        if n%2!=0:
            sum_odd+=n
    return sum_odd

print(sum_odds(my_list))