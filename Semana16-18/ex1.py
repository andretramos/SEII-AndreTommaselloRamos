def seq_a(tamanho):
    seq = []
    i = 1
    j = 1 
    while i <= size:
        seq.append(j)
        j += 2
        i += 1
    return seq

def seq_b(tamanho):
    seq = []
    i = 1
    j = 0
    while i <= size:
        j = j + i
        seq.append(j)
        i +=1
    return seq

def seq_c(tamanho):
    seq = []
    i = 1
    while i <= size:
        j = i*i
        seq.append(j)
        i +=1
    return seq

if __name__ == '__main__':
    size = 20        # Numero de elemento na lista
    print(seq_a(size))
    print(seq_b(size))
    print(seq_c(size))