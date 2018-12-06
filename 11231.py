
tables.
der = [['asdas', 1231, 'Vasy'],['asdas', 1231, 'Vasy'],['asdas', 1231, 'Vasy'],['asdas', 1231, 'Vasy']]

for i in der:
    print('|'.join(str(x).ljust(10) for x in i))