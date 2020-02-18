# doiexist

**How to execute ?**
1/
```bash
$ sudo chmod +x main.py
```
2/
```bash
$ ./main.py --path /my_folder/to/analyse -r
```


**Commands (optionals)**   
`--path` to execute the script in a given path.  
`-r` enable the script with recursive.  
`-c` to compare the file content instead juste name.

**Examples**

Check all the files from the actual folder
```bash
$ ./main.py -r
```

Check the files in a specific folderr
```bash
$ ./main.py --path /home/user/my_folder
```

Check all the content files from the actual folder  
```bash
$ ./main.py -r -c
```
