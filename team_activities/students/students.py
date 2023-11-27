import csv

ID_NUMBER = 0

def main():
    students_dict = read_dictionary("students.csv", ID_NUMBER)
    
    id_number = input("Please enter your ID-NUMBER: ").replace("-", "")
    
    
    if id_number in students_dict:
        
        name = students_dict[id_number]
        print(name[1])
    else:
        print("No such student")
        lengh_id = len(id_number)
        if lengh_id > 9:
              print("You are adding too many digits")
        if lengh_id < 9:
              print("You are adding too few digits")
              
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
     dictionary and return the dictionary.
    
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
        """
    
    dictionary = {}
    
    with open(filename, "rt") as csv_file:
        
        reader = csv.reader(csv_file)
        
        next(reader)
        
        for row_list in reader:
            
            if len(row_list) != 0:
                
                key = row_list[key_column_index]
                
                dictionary[key] = row_list
    
    return dictionary

if __name__ == "__main__":
    main()    