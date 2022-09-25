def narcissistic(number):
    var = [int(i) for i in str(number)]
    var2 = [j**len(var) for j in var]
    if sum(var2) == number:
        return True
    else:
        return False

narcissistic(10)