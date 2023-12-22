def fibonacci_sequence(n):
    n_1 = 0
    n_2 = 1
    count = 0
    n_terms = int(n)  - 2
    fina_list = [0, 1]
        
    while count < n_terms:
        ntotal = n_1 + n_2
        n_1 = n_2
        n_2 = ntotal
        fina_list.append(ntotal)
        count += 1
        
    return (fina_list)
