#open-cmd

#pip install phonenumbers

import phonenumbers

from phonenumbers import carrier

mobile_no = input("Enter Your Phone Number With Country Code:")

service_provider = phonenumbers.parse(mobile_no)

print(carrier.name_for_number(service_provider,"en"))