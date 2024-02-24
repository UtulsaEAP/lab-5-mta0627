def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    
    x = num1
    while x > 0:
        #write your code
        digit = x % 2
        x //= 2
        binary_val += str(digit)

    return binary_val


def string_reverse(input_string): 
    reverse_input = ''
    
   #write your for loop here
    
    for char in iter(input_string):
        reverse_input = char + reverse_input
        
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)