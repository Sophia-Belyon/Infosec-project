def handle_error(instruction):
    user_input = input(instruction)
    if user_input.strip() == "":
        print("Invalid input.Enter a valid number: ")
    else:
        return user_input
                   
def check_case(character):
    if character.isupper():
        return "The character input is in upper case"
    elif character.islower():
        return "The character input is in lower case"
    else:
        return "Oops! It seems character input is neither in lower case nor upper case"
        
character = handle_error("Enter character: ")
verifier = check_case(character)
print(verifier)
