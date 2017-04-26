import math


def gauss1(f,n):
    [x,w] = p_roots(n+1)
    G=sum(w*f(x))
    return G

def gauss(f,n,a,b):
    [x,w] = p_roots(n+1)
    G=0.5*(b-a)*sum(w*f(0.5*(b-a)*x+0.5*(b+a)))
    return G

if __name__ == '__main__':
    main()
