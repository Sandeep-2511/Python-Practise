C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o','p']
def list(S, step):
    return [S[i::step] for i in range(step)]
print(list(C,3))