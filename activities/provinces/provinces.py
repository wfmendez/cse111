def main():
    text_list = read_list("provinces.txt")
    
    print(text_list)
    
    print()
    
    text_list.pop(0)
    text_list.pop()
    
    print(text_list)
    
    new_list = change_elements(text_list, "AB", "Alberta")
    
    print()
    
    print(new_list)
    
    print()
    
    num_alberta = sum_element(new_list, "Alberta")
    
    print(f"Alberta occurs {num_alberta} times in the modified list.")
    
def read_list(filename):
    text_list = []
    
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    return text_list

def change_elements(list, old_element, new_element):
    new_list = []
    
    for element in list:
        if element == old_element:
            element = new_element
            new_list.append(element)
        else:
            new_list.append(element)
            
    return new_list

def sum_element(list, name_element):
    sum = 0
    
    for element in list:
        if element == name_element:
            sum += 1
            
    return sum

if __name__ == "__main__":
    main()