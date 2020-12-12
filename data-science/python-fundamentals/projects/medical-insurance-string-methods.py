# ----- Codecademy ----- #

# Python Fundamentals
# Python Strings
# Project: Medical Insurance

medical_data = """Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""


# -------------------- Code for the project. -------------------- #

# ------- Iteration 1. ------- #
print("\n" + medical_data)


# ------- Iteration 2. ------- #
updated_medical_data = medical_data.replace("#", "$")
print("\n" + updated_medical_data)


# ------- Iteration 3, 4, 5 ------- #
num_records = 0

for character in updated_medical_data:
    if character == "$":
        num_records += 1

print(f"\nThere are {num_records} medical records in the data.\n")


# ------- Iteration 6. ------- #
medical_data_split = updated_medical_data.split(";")
print(medical_data_split)


# ------- Iteration 7 and 8. ------- #
medical_records = []

for record in medical_data_split:
    medical_records.append(record.split(","))

print(medical_records)


# ------- Iteration 9, 10, 11, 12, and 13. ------- #
medical_records_clean = []

for record in medical_records:
    record_clean = []

    for item in record:
        record_clean.append(item.strip())

    medical_records_clean.append(record_clean)

print(medical_records_clean)


# ------- Iteration 14 and 15. ------- #
for record in medical_records_clean:
    record[0] = record[0].upper()
    print(record[0])


# ------- Iteration 16, 17, and 18. ------- #
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
    for i in range(len(record)):
        if i == 0:
            names.append(record[i])
        elif i == 1:
            ages.append(record[i])
        elif i == 2:
            bmis.append(record[i])
        else:
            insurance_costs.append(record[i])

print(names)
print(ages)
print(bmis)
print(insurance_costs)

# ------- Iteration 19, 20, and 21. ------- #
total_bmi = 0

for bmi in bmis:
    total_bmi += float(bmi)

average_bmi = total_bmi / len(bmis)

print(f"Average BMI: {average_bmi}")
