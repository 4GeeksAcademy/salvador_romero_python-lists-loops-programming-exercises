all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here

def filter_colors(item):
    return item['sexy']
def generate_li(item):
    return f"<li>{item['label']}</li>"
colors_filtered = (list(filter(filter_colors,all_colors)))
print(list(map(generate_li,colors_filtered)))