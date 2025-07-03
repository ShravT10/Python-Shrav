#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# print(final_list)
# ['Aang', 'Zuko', 'Appa', 'Katara', 'Sokka', 'Momo', 'Uncle Iroh', 'Toph']

final_list = []

names = open("Mail Merge Project Start/Input/Names/invited_names.txt",'r')
namelist = names.readlines()

for x in namelist:
    p = x.strip("\n")
    final_list.append(p)

with open("Mail Merge Project Start\Output\ReadyToSend\example.txt") as invite:
    con = invite.read()
    for z in final_list:
        with open(f"Mail Merge Project Start\Output\ReadyToSend\{z}_letter.txt",'w') as letter:
            x = con.replace("Aang" , z)
            letter.write(x)
            

        
