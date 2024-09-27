def encode_num(n):
    str_n=str(n)
    encoded_value=""
    for digit in str_n:
        squared_digit=int(digit)**2
        str_squared_digit=str(squared_digit)
        encoded_value+=str_squared_digit
    return int(encoded_value)
n=int(input())
result=encode_num(n)
print(result)
