# Extension Correction
This is a CLI application for correcting files' names in directory if there is no extension written. It automatically resolves the extensions of the files and sets them to the filename.

### How to use?
1. Open the terminal
2. Ensure you have click installed:
```
pip3 install click
```
3. Run the program:
```
python3 [path-the-cloned-firectory]/extension-correction-py/extensionless.py --directory [path-to-desired-directory-for-scanning] --statistics [1 - for yes, 0 for no]
```
4. Alternatively you can run:
```
python3 [path-the-cloned-firectory]/extension-correction-py/extensionless.py
```
You will be prompted to provide the directory and determine wether you want to have statistics displyed.
5. If all is done correctly, then in case you've chosen to get statistics you will have similar output:
```
jpg  :  44
pdf  :  1
mov  :  13
xml  :  8
png  :  4
zip  :  1
Directories: 0
Not found type: 11
Changed: 37
```

### How to scale?
You can add or remove any extensions using contents of the data.json file, which is located in the same folder.
