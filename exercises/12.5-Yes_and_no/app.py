the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def wikwok(num):
    if num ==1:
        return 'wiki'
    else:
        return 'woko'

print(list(map(wikwok,the_bools)))