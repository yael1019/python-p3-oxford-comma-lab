def oxford_comma(items):
    if len(items) < 3:
        return ' and '.join(items)
    items[len(items) - 1] = 'and ' + items[len(items) - 1]
    return ', '.join(items)
print(oxford_comma(['kiwi', 'salad', 'banana']))