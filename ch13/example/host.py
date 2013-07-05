#! /usr/bin/env python

class HotelRoomCalc(object):
    'Hotel room rate calculator'

    def __init__(self, rt, sales = 0.085, rm = 0.1):
        ''' HotelRoomCalc default arguments:
        sales tax = 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt
        print 'Haha'

    def calcTotal(self, days=1):
        'Calculate total; defult to daily rate'
        daily = round((self.roomRate *
            (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily

def main():
    sfo = HotelRoomCalc(299)
    print sfo.calcTotal()
    print sfo.calcTotal(2)
    sea = HotelRoomCalc(189, 0.086, 0.058)
    print sea.calcTotal()
    print sea.calcTotal(4)
    wasWkDay = HotelRoomCalc(169, 0.045, 0.02)
    wasWkEnd = HotelRoomCalc(119, 0.045, 0.02)
    print wasWkDay.calcTotal(5) + wasWkEnd.calcTotal()

if __name__ == '__main__':
    main()
