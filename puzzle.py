def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    lines = []

    for i in range(size):
       
        s = '-'.join(alphabet[size-1:i:-1] )
        
        lines.append(s.center(4*size-3, '-'))

    print(s)

N = int(input("Enter the size of the Rangoli: "))
print_rangoli(N)
