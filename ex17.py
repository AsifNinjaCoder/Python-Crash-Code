# All the Code Written By Asif date 24th September 2021
# more files read and write
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print(f"Coopying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f" the input file is {len(indata)} bytes long ")
print(f"does the output file exists? {exists(to_file)}")
print("Ready,hit Return to continue,ctrl-c to abort.")

input()

out_file= open(to_file,'w')
out_file.write(indata)

print("Alright,all done.")

out_file.close()
in_file.close()
