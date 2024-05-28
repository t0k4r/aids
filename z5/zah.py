

def zachlanny(items, cap):
    items.sort(key=lambda item: item[0]/item[1], reverse=True)
    
    value = 0
    weight = 0
    selected = []

    i = 0
    while weight < cap and i < len(items):
        item = items[i]
        if weight + item[1] <= cap:
            selected.append(item)
            value += item[0]
            weight += item[1]
        i += 1
    
    return value, selected

items = [(60, 10), (100, 20), (120, 30)]
cap = 50

max, sel = zachlanny(items, cap)
print(max, sel)
