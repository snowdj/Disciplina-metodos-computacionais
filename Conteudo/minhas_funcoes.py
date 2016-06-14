def prod_escalar_vetor(a, x):
    
    '''
    Esta funcao calcula o produto entre o
    escalar "a" e o vetor "x"
    
    input
    
    a: float - escalar
    x: numpy array - vetor
    
    output
    
    y: float - produto entre "a" e "x" 
    '''

    y = a*x
    
    return y

def produto_escalar(x, y):
    
    '''
    Esta funcao calcula o produto escalar entre dois
    vetores x e y
    
    input
    
    x: numpy array - vetor
    y: numpy array - vetor
    
    output
    
    c: float - produto escalar entre os 
       vetores x e y
    '''
    c = 0.0
    
    if len(x) != len(y):
        raise ValueError('x e y devem ter o mesmo numero de elementos')

    for i in range(len(x)):
        c += x[i]*y[i]
    
    return c