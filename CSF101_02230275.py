################################
# Your Name:tobden thapa
# Your Section:1ME
# Your Student ID Number:02230275
################################
# REFERENCES
# Links that you referred while solving
# the problem
# https://www.youtube.com/watch?v=u-OmVr_fT4s
################################
# SOLUTION
# Your Solution Score:46581
# Put your number here:5
###############################
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def calculate_score(key, count_dict):
    total_value = sum(count_dict.get(value, 0) for value in key)
    return total_value

file_path = 'input_5_cap1.txt'
point_dict = {'A X': 2, 'A Y': 4, 'A Z': 9, 'B X': 1, 'B Y': 5, 'B Z': 7, 'C X': 1, 'C Y': 6, 'C Z': 7}

value = read_input(file_path)
total_score = calculate_score(value,point_dict)
print("Total score is:", total_score)
