def cmpGen(conv):
    return lambda x,y: (0 if conv(x)==conv(y) else (1 if conv(x)>conv(y) else -1))
