def read_and_write_file():
    try:
        # Open the original file for reading
        with open("input.txt", "r") as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)
        
        print("File successfully read and modified content written to 'output.txt'.")
    except FileNotFoundError:
        print("Error: The file 'input.txt' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def error_handling_lab():
    try:
        # Ask user for the filename
        filename = input("Enter the filename: ")
        
        # Try to open the file for reading
        with open(filename, "r") as file:
            content = file.read()
        
        print("File content successfully read:")
        print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
error_handling_lab()
# Run the function
read_and_write_file()
