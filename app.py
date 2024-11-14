# app.py
def main():
    animal = input("What is your favourite animal: ")
    print(f"My favourite animal is also {animal}")
    main()  # Recursively call main to keep the program running

if __name__ == '__main__':
    main()
