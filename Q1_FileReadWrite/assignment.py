# q1_read_write.py

def read_and_write_file():
    """
    Reads content from an input file, converts it to uppercase,
    and writes the modified content to a new output file.
    Includes robust error handling for common file-related issues.
    """
    input_filename = input("Please enter the name of the file you want to read: ")
    output_filename = "modified_" + input_filename

    file_content = ""
    read_success = False

    print(f"\nAttempting to read from '{input_filename}'...")
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            file_content = infile.read()
        print("✅ File read successfully.")
        read_success = True

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred while reading the file: {e}")

    if read_success:
        modified_content = f"--- MODIFIED CONTENT FROM ORIGINAL FILE ---\n\n"
        modified_content += file_content.upper()
        modified_content += f"\n\n--- END OF MODIFIED CONTENT ---"

        print(f"Attempting to write to '{output_filename}'...")
        try:
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                outfile.write(modified_content)
            print(f"✅ Modified content successfully written to '{output_filename}'.")

        except Exception as e:
            print(f"❌ An error occurred while writing to the file: {e}")
    else:
        print("File operation halted. Please fix the read error and try again.")


if __name__ == "__main__":
    read_and_write_file()
