Comparing two lists and deleting missing files.
---
___
This is a program for comparing two 'txt' files with paths and create third file with paths with missing paths.
Second file compare with first, all files which missing to first file will be added in third file.

How it works:
1. Use createlist.bat for create two files with paths list.
2. Run compare_files_from_lists.py
3. Check the created 'txt' file.


CMD commands for create 'txt' file with list(for createlist.bat file):
- chcp 1251\
- dir /b /s > X:\filelist.txt