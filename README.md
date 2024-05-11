# synchronize_folders
Basically this program synchronizes two folders: source and replica in certain intervals you can set them from the command line.<br />
The program will maintain a full, identical copy of source folder at replica folder.<br />
File creation/copying/removal operations sare be logged to a file and to the console output.<br />
To run this program you need to have python installed.<br />
To execute this program you have to do few steps.<br />
1.Navigate to the directory where your Python script is saved using the cd command. For example
```
$ cd path_to_script_directory
```
2. Once you're in the correct directory, you can call the Python script using the python command followed by the script filename and the required command-line arguments. For example:
```
$ python script_name.py source_folder_path replica_folder_path log_file_path interval
```
For example:
```
$ python synchronize_folders.py C:\source_folder C:\replica_folder C:\logs\sync_log.txt 5
```
if you are not sure with the arguments you can always get more info with:
```
$ python script_name.py -h
```
