def num2eng():
    lists = ['zero','one','two','three','four','five','six','seven','eight','nine']
    new =''

    while True:
        try:
            iput = int(raw_input('Please input a int(0~1000): '))
            if iput <0 or iput >1000:
                continue
        except:
            continue
        break

    iput = str(iput)
    for j in iput:
        new += lists[int(j)]+'-'
    return new[0:-1]

print num2eng()
