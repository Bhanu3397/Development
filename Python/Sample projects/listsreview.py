from traceback import print_tb


first_names= ['Ainsley','Ben','Chani','Depak']
preferred_size= ["Small", "Large", "Medium"]
preferred_size.append('Medium')
print(preferred_size)
print(' ')
customer_data = [['Ainsley','Small', True],['Ben','Large',False],['Chani','Medium',True],['Depak','Medium',False]]
print(customer_data)
print(' ')
customer_data[2][2]=False
print(customer_data)
print(' ')
customer_data[1].remove(False) #Removiing shipping option
print(customer_data)
print(' ')
new_customer_data = [["Amit", "Large", True], ["Karim", "X-Large", False]]
customer_data_final =  customer_data+new_customer_data
print(' ')
print(customer_data_final)

student_data = [["Ali", 90], ["Bob", 87.5], ["Cam", 80.3], ["Doug", 77.45]]
print(student_data[-1][-1])