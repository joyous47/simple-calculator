# q2_error_handling.py

def handle_file_errors():
    """
    Asks the user for a filename and attempts to read it.
    Handles errors such as missing files, permission errors,
    or other unexpected issues.
    """
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("\n✅ File opened successfully.")
            print("📄 File content:\n")
            print(file.read())

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


if __name__ == "__main__":
    handle_file_errors()
