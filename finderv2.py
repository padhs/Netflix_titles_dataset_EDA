# retrieve only director

def extract_substring_after_direct_by(file_path, start_marker, end_marker):
    with open(file_path, 'r') as file:
        content = file.read()

    # Find the position of the "direct_by" substring
    direct_by_index = content.find('direct_by')
    if direct_by_index == -1:
        return "direct_by marker not found"

    # Start searching for the substring after the "direct_by" marker
    search_start_index = direct_by_index + len('direct_by')

    # Find the start marker after the "direct_by" marker
    start_index = content.find(start_marker, search_start_index)
    if start_index == -1:
        return "Start marker not found after 'direct_by'"

    start_index += len(start_marker)

    # Find the end marker after the start marker
    end_index = content.find(end_marker, start_index)
    if end_index == -1:
        return "End marker not found after start marker"

    return content[start_index:end_index]


# Example usage
file_path = 'ntflx_dirs_queries/kota_factory.txt'
start_marker = 'q='
end_marker = '&amp;'
substring = extract_substring_after_direct_by(file_path, start_marker, end_marker)
# there is a '+' sign in between the strings. let's remove that:
cleaned_substring = substring.replace('+', ' ')
print(cleaned_substring)

