import os
  
# assign directory
directory = 'Proton Profiles'
  
# itrate over files in 
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        print(filename.path)
