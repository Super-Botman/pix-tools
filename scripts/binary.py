def binaryToDecimal(binary):    
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal   

if __name__ == '__main__':
    code = "tic toc toc tic toc toc tic toc toc tic toc toc tic toc tic toc tic tic tic toc"
    abc = ['espace', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    bits = int(code.replace("toc", "0").replace("tic", "1").replace(' ', ''))

    a = ""
    b = 0

    n = 5
    chunks = [str(bits)[i:i+n] for i in range(0, len(str(bits)), n)]
    print(chunks)

    for c in chunks:
        for i in str(binaryToDecimal(int(c))):
            print(i)
            for d in abc:
                if int(i) == int(b):
                    a += d
                b += 1
            b = 0
    print(str(bits), ':', binaryToDecimal(bits), ':', a)