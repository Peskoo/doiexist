# Lycos

Search if there is duplicates files into your system.  
You'll can find mp3, or avi files with differents titles but same content for example.

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

**Examples**

Check all the files from the actual folder
```bash
$ ./main.py -r
```

Check the files in a specific folderr
```bash
$ ./main.py --path /home/user/my_folder
```
