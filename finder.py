# find the director name from the source code:

def extract_substring(file_path, start_marker, end_marker):
    with open(file_path, 'r') as file:
        content = file.read()

    start_index = content.find(start_marker)
    if start_index == -1:
        return "Start marker not found"

    start_index += len(start_marker)
    end_index = content.find(end_marker, start_index)
    if end_index == -1:
        return "End marker not found"

    return content[start_index:end_index]


# Example usage
file_path = './temp_dir_files/kota_factory.txt'
start_marker = 'q='
end_marker = '&amp;'
substring = extract_substring(file_path, start_marker, end_marker)
print(substring)
