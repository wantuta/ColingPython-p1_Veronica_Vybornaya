def integers():
    number = 1
    while True:
        yield number
        number +=1
        
def squares():
    int_num = integers()
    for numbers in int_num:
        yield numbers**2
