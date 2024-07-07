# retrieve both director and creator

def extract_substrings(file_path, start_marker, end_marker):
    with open(file_path, 'r') as file:
        content = file.read()

    results = []

    # Function to find substring between markers
    def find_substring(content, marker, start_marker, end_marker):
        marker_index = content.find(marker)
        if marker_index == -1:
            return None
        search_start_index = marker_index + len(marker)
        start_index = content.find(start_marker, search_start_index)
        if start_index == -1:
            return None
        start_index += len(start_marker)
        end_index = content.find(end_marker, start_index)
        if end_index == -1:
            return None
        return content[start_index:end_index]

    # Find and add substring after 'direct_by'
    result = find_substring(content, 'direct_by', start_marker, end_marker)
    if result:
        results.append(result)

    # Find and add substring after 'creat_by'
    result = find_substring(content, 'creat_by', start_marker, end_marker)
    if result:
        results.append(result)

    return results


# Example usage
file_path = 'ntflx_dirs_queries/kota_factory.txt'
start_marker = 'q='
end_marker = '&amp;'
substrings = extract_substrings(file_path, start_marker, end_marker)

# Replace '+' in the substrings with ' '
cleaned_substrings = [item.replace('+', ' ') for item in substrings]
# print(cleaned_substrings)
for idx, substring in enumerate(cleaned_substrings):
    print(f"Substring {idx + 1}: {substring}")
