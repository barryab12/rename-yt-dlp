import os
import re

folder_path = "./"

for filename in os.listdir(folder_path):
    match = re.match(r".* - (\d+ .*) \[.*\](\.mp4)", filename)
    if match:
        new_name = match.group(1) + match.group(2)
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        os.rename(old_file, new_file)
