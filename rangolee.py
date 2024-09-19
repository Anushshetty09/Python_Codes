def print_rangoli(size):
    alpha="abcdefghijklmnopqrstuvwxyz"
    list=[]
    
    for i in range(size):
        s="-".join(alpha[size-1:i:-1]+alpha[i:size])
        
        list.append(s.center(4*size-3, "-"))
        
    print('\n'.join(list[::-1]+list[1:]))
    
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)