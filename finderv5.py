import os
import pandas as pd
import numpy as np


def extract_substring(file_path, begin_marker, last_marker):
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
    start_index = content.find(begin_marker, search_start_index)
    if start_index == -1:
        return "Start marker not found"

    start_index += len(begin_marker)

    # Find the end marker after the start marker
    end_index = content.find(last_marker, start_index)
    if end_index == -1:
        return "End marker not found"

    return content[start_index:end_index]


def process_files_in_directory(directory_path, start_marker, end_marker):
    all_results = {}
    for textfile in os.listdir(directory_path):
        if textfile.endswith(".txt"):  # Process only text files
            file_path = os.path.join(directory_path, textfile)
            director_substring = extract_substring(file_path, start_marker, end_marker)
            # Replace the '_6_9' with '/' & replace '+' with ' ' before storing it in a dictionary
            cleaned_director_substring = director_substring.replace('+', ' ')
            cleaned_text_file = textfile.replace('_6_9', '/')
            _txt_remove = cleaned_text_file.replace('.txt', '')
            all_results[_txt_remove] = cleaned_director_substring
            # remove the file after substring extraction:
            os.remove(file_path)
    return all_results


# Example usage
directory_path = "./ntflx_dirs_queries"
start_marker = 'q='
end_marker = '&amp;'
results = process_files_in_directory(directory_path, start_marker, end_marker)


# input directors from dictionary
df = pd.read_csv('./dataset/netflix_titles.csv')
# match title and fill the directors in the dataset
for title, director in results.items():
    df.loc[(df['title'] == title) & (df['director'].isna()), 'director'] = director

df.to_csv('./dataset/ntflx_titles_with_dirs.csv')
print(df.info())
