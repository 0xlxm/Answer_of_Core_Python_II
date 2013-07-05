#! /usr/bin/env python

unit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
within_twety = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eithteen', 'nineteen', 'twenty']
decade = [None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def convert(num):
    ''' convert a num to an Englist style,(eg: 89->eighty-nine). '''
    str_num = str(num)
    if len(str_num) == 1:
        return unit[num]
    if len(str_num) == 2 and 10 <= num <= 20:
        num_within_20 = within_twety[num-10]
        return num_within_20
    elif num % 10 == 0:
        num_20_90 = decade[num//10]
        return num_20_90
    else:
        num_21_99 = decade[num//10] + '-' + unit[num%10]
        return num_21_99

if __name__ == '__main__':
    while True:
        try:
            num = input('Enter a number between 0 ~ 1000: ')
            if num < 0 or num > 1000:
                continue
        except:
            continue
        break
    if len(str(num)) < 3:
        print convert(num)

    elif len(str(num)) == 3:
        if num % 100 == 0:
            print unit[num//100] + 'hundred'
        else:
            print unit[num//100] + ' hundred and ' + convert(num%100)
    elif len(str(num)) == 4:
        print 'one thousand'
