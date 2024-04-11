def create_file():
    try:
    
        with open('my_file.txt', 'w') as file:
            
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with text and numbers: 789\n")
        print("File 'my_file.txt' created and initial content written successfully.")
    except IOError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        
        pass

def read_file():
    try:
    
        with open('my_file.txt', 'r') as file:
            
            content = file.read()
            print(f"Contents of 'my_file.txt':\n{content}")
    except FileNotFoundError:
        print("Error: File 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied to open 'my_file.txt'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def append_to_file():
    try:
        
        with open('my_file.txt', 'a') as file:
            
            file.write("This is an appended line\n")
            file.write("Appending more text\n")
            file.write("Last line for appending\n")
        print("Content appended to 'my_file.txt' successfully.")
    except FileNotFoundError:
        print("Error: File 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied to open 'my_file.txt'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    
    create_file()

    read_file()

    
    append_to_file()
