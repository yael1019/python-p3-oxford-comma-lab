def oxford_comma(items):
    str = ' '
    for index, item in enumerate(items):
        # print(index, items[index])
        if index != len(items) - 1:
            str += ','.join([item])
        else:
            str += ', and '.join([item])
    return str
print(oxford_comma(['kiwi', 'salad', 'banana']))