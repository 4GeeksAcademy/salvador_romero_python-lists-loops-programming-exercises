par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
for s in par:
    if s.lower() in counts:
        counts[s.lower()] += 1
    elif s.lower() == " ":
        pass
    else:
        counts[s.lower()] = 1


print(counts)
