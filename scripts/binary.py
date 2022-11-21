import itertools

def binaryToDecimal(binary):    
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal   

def genAsciiTable(bit_n):
    asciiTable = []
    i = 65
    for x in map(''.join, itertools.product('01', repeat=bit_n)):
        asciiTable.append([x, chr(i)])
        i+=1
    return asciiTable

if __name__ == '__main__':
    code = "tic toc toc tic toc toc tic toc toc tic toc toc tic toc tic toc tic tic tic toc"
    abc = ['espace', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    asciiTable = genAsciiTable(5)
    
    bits = int(code.replace("toc", "0").replace("tic", "1").replace(' ', ''))

    a = ""
    b = 0

    n = 5
    chunks = [str(bits)[i:i+n] for i in range(0, len(str(bits)), n)]

    for c in chunks:
        for i in str(binaryToDecimal(int(c))):
            for d in abc:
                if int(i) == int(b):
                    a += d
                b += 1
            b = 0
    
    w = ''
    for c in chunks:
        for char in asciiTable:
            if char[0] == c:
                w += char[1]

    print(str(chunks), ':', w , ':', a)