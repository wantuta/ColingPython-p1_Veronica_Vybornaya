def integers():
    number = 1
    while True:
        yield number
        number +=1
  

def squares():
    int_num = integers()
    for numbers in int_num:
        yield numbers**2
       
def take(n, generator):
    checking = 0
    num = []
    for numbers in generator:
        if checking >= n:
            break
        num.append(numbers)
        checking += 1
    return num
