def echo(value, newline=True):
    if newline:
        print(value)
    else:
        print(value, end='')
    
echo('Kursus')
echo('Pemrograman ')
echo('Python 3', True)