import sys
from read_AoCinputs import read_txt_list 


def read_code_file(code_file:list):
    code_list = read_txt_list(code_file)
    code_array = []
    index_zero = 0
    for  index, number in enumerate(code_list):
        code_array.append((index,int(number)))
        if int(number) == 0:
            index_zero = index
    return code_array, index_zero

def print_code(code:list):
    for element in code:
        print(element[1], end=" ")
    print()

def decode(orginal: list, working_code:list):
    lenght = len(working_code)-1
    for element in orginal:
        index = working_code.index(element)
        ele = working_code.pop(index)
        number = ele[1]
        new_index = 0
        if number >= 0:
            new_index = (index + number) 
            if new_index >= lenght:
                x = new_index // lenght
                new_index -= lenght*x
        else:
            new_index = (index + number)
            if new_index <= 0:
                x = (-new_index) // lenght
                new_index += lenght*x
        working_code.insert(new_index, ele)

    return working_code


def real_decode(orginal: list, working_code:list):
    orgi = orginal.copy()
    for i in range(len(working_code)):
        working_code[i] = (working_code[i][0],working_code[i][1]*811589153)
        orgi[i] = (orgi[i][0],orgi[i][1]*811589153)

    for i in range(10):
        working_code = decode(orgi, working_code)
    
    return working_code


def analyse_decoded(decoded:list, index_zero):
    length = len(decoded)
    index_zero = decoded.index((index_zero, 0))
    index1 = (index_zero + 1000) % length
    index2 = (index_zero + 2000) % length
    index3 = (index_zero + 3000) % length
    num1 = decoded[index1][1]
    num2 = decoded[index2][1]
    num3 = decoded[index3][1]
    print(num1, num2, num3)
    return num1 + num2 + num3



##################################################################

# Defining main function
def main():
    
    code_file = str(sys.argv[1])
    original_code, index_zero = read_code_file(code_file)

    decoded = original_code.copy()
    decoded = decode(original_code, decoded)
    codesum = analyse_decoded(decoded, index_zero)
    print("Code sum is ", codesum)
    print()

    decoded = original_code.copy()
    real_decoded = real_decode(original_code, decoded)
    codesum = analyse_decoded(real_decoded, index_zero)
    print("real Code sum is ", codesum)
    print()

# main
if __name__=="__main__":
    main()