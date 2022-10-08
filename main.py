from functools import reduce
def main():

    lista=[2,4,7,9,13,16]
    l=list(filter(lambda x:x%2==0,lista))
    s=reduce(lambda a,b:a+b,l)
    print(f'Estos son los numeros pares de la lista : ',l)
    print(f'Esta es la suma de los numeros pares de la lista',s)

if __name__ == '__main__':
    main()


