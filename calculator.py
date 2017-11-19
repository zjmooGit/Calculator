#!/usr/bin/env python3
import sys
try:
    salary = int(sys.argv[1])
    taxOwner = salary - 3500
    if taxOwner <= 0:
        tax = 0
    elif taxOwner > 0 and taxOwner <= 1500:
        tax = taxOwner * 0.03
    elif taxOwner > 1500 and taxOwner <= 4500:
        tax = taxOwner * 0.1 - 105
    elif taxOwner > 4500 and taxOwner <= 9000:
        tax = taxOwner * 0.2 - 555
    elif taxOwner > 9000 and taxOwner <= 35000:
        tax = taxOwner * 0.25 - 1005
    elif taxOwner > 35000 and taxOwner <= 55000:
        tax = taxOwner * 0.3 - 2755
    elif taxOwner > 55000 and taxOwner <= 80000:
        tax = taxOwner * 0.35 - 5505
    else:
        tax = taxOwner * 0.45 - 13505
    taxRes = format(tax, ".2f")
    print(taxRes)
except IndexError:
    print("please input your salary!!!")
except ValueError:
    print("Parameter Error!!!")
