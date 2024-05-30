

def zachlanny(items, cap):
    items.sort(key=lambda item: item[0]/item[1], reverse=True)
    print(items)
    value = 0
    weight = 0
    selected = []

    i = 0
    while weight < cap and i < len(items):
        item = items[i]
        if weight + item[0] <= cap:
            selected.append(item)
            value += item[1]
            weight += item[0]
        i += 1
    
    return weight, value, selected


# cap=10
cap=7
# items= [(3,5),(1,2),(4,8),(5,9),(2,3),(3,6),(4,7),(2,4)]
items = [(3,5),(1,2),(4,8),(5,9), (2,3)]

weg,max, sel = zachlanny(items, cap)
print(weg,max, sel)
