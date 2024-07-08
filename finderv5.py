import os
import pandas as pd


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
            return "null"

    # Find the start marker after the identified marker
    start_index = content.find(start_marker, search_start_index)
    if start_index == -1:
        return "Start marker null"

    start_index += len(start_marker)

    # Find the end marker after the start marker
    end_index = content.find(end_marker, start_index)
    if end_index == -1:
        return "End marker null"

    return content[start_index:end_index]


def process_files_in_directory(directory_path, start_marker, end_marker):
    all_results = {}
    for textfile in os.listdir(directory_path):
        if textfile.endswith(".txt"):  # Process only text files
            file_path = os.path.join(directory_path, textfile)
            director_substring = extract_substring(file_path, start_marker, end_marker)
            all_results[textfile] = director_substring
            # remove the file after substring extraction:
            os.remove(file_path)
    return all_results


# Example usage
directory_path = "./ntflx_dirs_queries"
start_marker = 'q='
end_marker = '&amp;'
results = process_files_in_directory(directory_path, start_marker, end_marker)

# Print results
'''
for filename, substring in results.items():
    print(results)
    print(f"File: {filename}")
    print(f"Substring: {substring}")
'''

'''
This should print a dictionary of string:string datatype
We will use pandas to create a df of this dictionary.
save it to a csv file
since the title and director are in key:value paris, the csv file will have wide dataset
transpose it to convert into long dataset
merge the csv with original dataset.
Do the same with cast ?
'''

df = pd.DataFrame(results)
transpose_df = df.transpose()
transpose_df.to_csv('./dataset/transposed_dirs.csv')
# last step: merge with original dataset in excel
