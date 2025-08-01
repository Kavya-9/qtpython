colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new_colors = [colors[i] for i in range(len(colors)) if i not in (0, 4, 5)]
print(new_colors)

