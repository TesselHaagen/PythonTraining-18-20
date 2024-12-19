def banner(name):
    """
    This function prints a banner around the given name.

    Args:
    - name (str): th einput name. 
    """
    print("*"*4 + "*"*len(name))
    print(f"* {name} *")
    print("*"*4 + "*"*len(name))


input_name = input("What is your name?\n")
banner(input_name)