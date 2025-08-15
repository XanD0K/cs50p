while True:
    try: 
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break # 'break' could also go inside the 'try' block

print(f"x is {x}")