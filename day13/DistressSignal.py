import sys
from read_AoCinputs import read_txt_list 


def compare_signals(signal:list):

    sum = 0
    for i in range(0,len(signal),3):
        package1 = create_list(signal[i])
        package2 = create_list(signal[i+1])

        test = compare_packages(package1, package2)
        if test:
            sum += (i//3+1)
    return sum


def create_list(package:str):
    plist = put_package_into_list(package)
    for i in range(len(plist)):
        if is_item_package(plist[i]):
            plist[i] = create_list(plist[i])
        else:
            plist[i] = int(plist[i]) 
    return plist


def is_item_package(item:str):
    return item[0] == "[" and item[-1]=="]"


def put_package_into_list(package:str):

    package = package[1:-1]
    items = []

    open = 0
    start_idx = 0
    for counter in range(len(package)):
        if package[counter] == "[":
            open += 1
        if package[counter] == "]":
            open -= 1
        if package[counter]=="," and open == 0:
            items.append(package[start_idx:counter])
            start_idx = counter+1
        # last item
        if counter == len(package)-1:
            items.append(package[start_idx:])

    return items


def compare_packages(left:list, right:list):
    for i in range(len(left)):
        if i<len(right):

            if type(left[i]) is int and type(right[i]) is int:
                if left[i] < right[i]:
                    return True
                elif left[i] > right[i]:
                    return False
                else:
                    continue

            elif type(left[i]) is list and type(right[i]) is int:
                result = compare_packages(left[i], [right[i]] )
                if result is None:
                    continue
                else:
                     return result
            
            elif type(left[i]) is int and type(right[i]) is list:
                result =  compare_packages([left[i]], right[i])
                if result is None:
                    continue
                else:
                     return result

            elif type(left[i]) is list and type(right[i]) is list:
                result = compare_packages(left[i], right[i])
                if result is None:
                    continue
                else:
                     return result
        else:
            return False

    # left side run out of items
    if len(left) < len(right):
        return True
    else:
        return None


def compare_item(item1:str, item2: str):
# Assumes no empty items

    if is_item_package(item1) and is_item_package(item1):
        return compare_packages(item1, item2)

    elif is_item_package(item1):
        return compare_packages(item1, "["+item2 + "]")

    elif is_item_package( item2 ):
        return compare_packages("["+item1 + "]", item2)

    # both should be integers
    else:
        if int(item1) < int(item2):
            return True
        else:
            return False 


def sort_packages(signal:list):

    packages = []
    for i in range(0,len(signal),3):
        package1 = create_list(signal[i])
        package2 = create_list(signal[i+1])
        packages.append(package1)
        packages.append(package2)

    sorted_packages = [[[2]],[[6]]]

    for package in packages:
        for i in range(len(sorted_packages)):
            if compare_packages(package, sorted_packages[i]):
                sorted_packages.insert(i,package)
                break
        sorted_packages.append(package)

    docoder_key = 1
    docoder_key *= (sorted_packages.index([[2]])+1)
    docoder_key *= (sorted_packages.index([[6]])+1)
    return docoder_key

# Defining main function
def main():
    
    signal_file = str(sys.argv[1])
    signal = read_txt_list(signal_file)

    sum_cor_sig = compare_signals(signal)
    print()
    print("Sum of correct signal idx is ", sum_cor_sig)

    decoder_key = sort_packages(signal)
    print("Decoder Key is ", decoder_key)


# main
if __name__=="__main__":
    main()