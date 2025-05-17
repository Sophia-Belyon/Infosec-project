# Roman(i)
values  = []
count = 0 # Counts inputs entered so far
while count < 5:
    user_input = input(f"Enter value {count + 1}: ")
    if user_input.strip() == "":
            print("Invalid input.Enter a valid number: ")
    else:
        values.append(int(user_input))
        count = count + 1 # Keeps track of no of entries 
   

# Roman(ii)
average = sum(values) / len(values)
print(f"Average of values = {average}")