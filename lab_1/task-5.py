def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Total number of lines: {len(lines)}")
        file.seek(0)
        content = file.read()
        num_lines = content.count('\n') + (1 if content and not content.endswith('\n') else 0)
        return num_lines

if __name__ == "__main__":
    filename = "abc.txt"  # Use a text file, not .docx
    lines_count = count_lines(filename)
    print(f"Number of lines (counted by function): {lines_count}")
