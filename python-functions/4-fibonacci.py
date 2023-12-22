def fibonacci_sequence(n):
    n_1 = 0
    n_2 = 1
    count = 0
    n_terms = int(n)  - 2

    if n_terms + 2 == 0:
        fina_list = []
        return fina_list
        SystemExit
    
    elif n_terms < 0:
        fina_list = [0]
        return fina_list
        SystemExit
    
    
    else:
        fina_list = [0,1]
        
    while count < n_terms:
        ntotal = n_1 + n_2
        n_1 = n_2
        n_2 = ntotal
        fina_list.append(ntotal)
        count += 1
        
    return (fina_list)
