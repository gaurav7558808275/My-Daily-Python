import re

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""  

output_1 = re.findall('\d',string)
output_2 = re.findall('\d+',string)
print(output_1,output_2)