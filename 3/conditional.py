def conditional(answer: int) -> str:
    if answer == 3 :
        return "equals"
    elif answer < 9 :
        return "less than"
    if answer > 10:
        return "greater than"
    if answer <= 7:
        return 'less than or equal'
    if answer >= 12:
        return "greater than or equal"  
    if answer != 5 :
        return 'not equals'  
    else:
        return 'Break'

