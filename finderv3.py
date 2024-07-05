# retrieve director, if not found, retrieve creator

def extract_substring(file_path, start_marker, end_marker):
    with open(file_path, 'r') as file:
        content = file.read()

    # Try to find the "direct_by" substring
    direct_by_index = content.find('direct_by')
    if direct_by_index != -1:
        search_start_index = direct_by_index + len('direct_by')
    else:
        # If "direct_by" is not found, try to find the "creat_by" substring
        creat_by_index = content.find('creat_by')
        if creat_by_index != -1:
            search_start_index = creat_by_index + len('creat_by')
        else:
            return "Neither 'direct_by' nor 'creat_by' markers found"

    # Find the start marker after the identified marker
    start_index = content.find(start_marker, search_start_index)
    if start_index == -1:
        return "Start marker not found after identified marker"

    start_index += len(start_marker)

    # Find the end marker after the start marker
    end_index = content.find(end_marker, start_index)
    if end_index == -1:
        return "End marker not found after start marker"

    return content[start_index:end_index]


# Example usage
file_path = './temp_dir_files/kota_factory.txt'
start_marker = 'q='
end_marker = '&amp;'
substring = extract_substring(file_path, start_marker, end_marker)

# there is a '+' sign in between the strings. let's remove that:
cleaned_substring = substring.replace('+', ' ')
print(cleaned_substring)
