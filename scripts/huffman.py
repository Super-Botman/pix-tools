def encode(string, table, letters_table):
    encoded_string = ""
    for w in string:
        i = 0
        for l in letters_table:
            if w == l:
                encoded_string += str(table[i])
            i = i+1
    return encoded_string

def compressionTaux(string, encoded_string, ):
    lenString = len(string)*8
    lenEncoded = len(encoded_string)
    return lenEncoded/lenString * 100

if __name__ == '__main__':
    table1 = ["00","10","010","011","1111","1100","1101","11100", "11101"]
    table2 = ["01001101","01000001","01010011","0100010","01000100","01000111","01001100","01010010"]
    letters_table = [" ", "E","O","R","B","D","S","N","U" ]

    string = "UNE ROBE BORDEE DE ROSES"

    #string_standard = encode(string, table2, letters_table)
    #string_optmised = encode(string, table1, letters_table)

    #economie = len(string_standard) - len(string_optmised)

    # print('codage standard:', string_standard)
    # print('codage optimisé:', string_optmised)
    # print("economisé : ", economie)

    print("taux de compression :", compressionTaux(string, encode(string, table1, letters_table)))
