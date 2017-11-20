#!/usr/bin/env python
import sys
try:
    for arg in sys.argv[1:]:
        salary_info_list = arg.split(':')
        salary = int(salary_info_list[1])
        wx = salary * 0.08 + salary * 0.02 + salary * 0.005 + salary * 0.06
        taxOwner = salary - 3500 - wx
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
        salary_final = format(salary - wx - tax, ".2f")
        print(salary_info_list[0] + ':' + salary_final)
except IndexError:
    print("please input your salary!!!")
except ValueError:
    print("Parameter Error!!!")
