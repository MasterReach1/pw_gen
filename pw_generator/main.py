from password_generator import PasswordGenerator

if __name__ == "__main__":
    while True:
        response = input("Do you have specific password requirements? Y/N")

        if response.lower() == "y":
            length = input("Enter minimum password length >> ")
            upper = input("Enter minimum uppercase letters >> ")
            lower = input("Enter minimum lowercase letters >> ")
            numbers = input("Enter minimum numbers >> ")
            symbols = input("Enter minimum symbols >> ")
            spaces = input("Enter minimum spaces >> ")
            pg = PasswordGenerator(int(length), int(upper), int(lower), int(numbers), int(symbols), int(spaces))
            print(pg.generate())
            break
        elif response.lower() == "n":
            pg = PasswordGenerator()
            print(pg.generate())
            break
        else:
            print("Invalid response.")
            continue
