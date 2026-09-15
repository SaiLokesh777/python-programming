# import re
# text = "The price is $100 and the quantity is 5."

# result=re.search(r"\d",text)
# print(result.group())

import re

text = "My phone number is 9876543210"

result = re.search(r"\d+", text)

if result:
    print("Number found:", result.group())
else:
    print("No number found")