employee_list = (('sushant',10000) , ('sunny',150000) , ('vibha',30000))

max_sal = 0
highest_sal = ''

def max_salary(employee_lst):
    for (name,salary) in employee_lst:
        if salary > max_sal:
            max_sal = salary
            highest_sal = name
        else:
            pass

    return(highest_sal, max_sal)

max_salary(employee_list)
