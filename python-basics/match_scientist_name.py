def create_scientist_dict():
    """Reads scientists.txt and creates a dictionary mapping letters to AI scientist names."""
    scientist_dict = {}
    try:
        with open('data/scientists.txt', 'r') as file:
            for line in file:
                letter, scientist = line.strip().split(': ')
                scientist_dict[letter] = scientist
    except FileNotFoundError:
        print("The file 'scientists.txt' was not found.")
    return scientist_dict

def get_scientist_name(scientist_dict):
    """Prompts the user for their name and returns the corresponding AI scientist name."""
    while True:
        try:
            name = input("Enter your First [space] Last name: ")
            if not name:
                raise ValueError("Input cannot be empty.")
            first_letter = name[0].upper()
            if first_letter in scientist_dict:
                print(f"Unique AI scientist name with the first letter: {scientist_dict[first_letter]}")
                break
            else:
                print("No scientist found for the given first letter. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    scientist_dict = create_scientist_dict()
    if scientist_dict:
        get_scientist_name(scientist_dict)
        
# def create_scientist_dict():
#     scientist_dic = {}

#     try:
#         with open("./data/scientists.txt") as f:
#             for line in f:
#                 scientist_dic[line[0]]= line[3:].replace("\n","")
#         return scientist_dic
#     except FileNotFoundError as e:
#         print("File not found {} :)".format(e))

# def get_scientist_name():

#     scientist_name = input("Enter scientist first and last name: ")
   
#     while scientist_name == "":
#         scientist_name = input("Enter scientist first and last name: ")
#         if(scientist_name != ""):
#             first_letter = scientist_name[0].upper()
#             scientists = create_scientist_dict()
#             found_scientist = scientists[first_letter]
#             if(found_scientist):
#                 print(found_scientist)
#             else:
#                 print("Name not found ): ")
        

# def main():
#     print(get_scientist_name())

# if __name__ == "__main__":
#     main()