def eval_identifier(identifier):
    if len(identifier) != 10:
        raise Exception
    
    characters = {}
    digits = 0
    uppercase = 0
    
    for character in identifier:
        if not characters.get(character) and character.isalnum():
            characters[character] = 1
            if character.isdigit():
                digits += 1
            if character.isupper():
                uppercase += 1
        else:
            raise Exception
    
    if digits < 3 or uppercase < 2:
        raise Exception


for _ in range(int(input())):
    try:
        eval_identifier(input())
        print("Valid")
    except Exception:
        print("Invalid")
