import re
import csv

# Define the regular expression pattern to match phone numbers
pattern = re.compile(r'\b\s*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})(\.[A-Za-z]{2,})?\s*\b')

# Read phone numbers from the input file
with open('emails.txt', 'r') as input_file:
    phone_numbers = input_file.readlines()

# Extract phone numbers using the regular expression pattern
extracted_phone_numbers = []
for phone_number in phone_numbers:
    match = pattern.findall(phone_number)
    if match:
        extracted_phone_numbers.append((phone_number.strip(), 'yes'))
    else:
        extracted_phone_numbers.append((phone_number.strip(), 'no'))

# Save the extracted phone numbers in a CSV file
with open('output_email.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['Phone No.', 'Extracted by Regex'])
    writer.writerows(extracted_phone_numbers)

print('Phone numbers extracted and saved to output.csv.')
