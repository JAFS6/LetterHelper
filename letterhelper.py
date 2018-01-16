print "\nLetter Helper"

#read template file

file = open("letter_template.txt",'r')
template = file.read()

#print "\nTemplate:\n" + template + "\n"

#read data file
with open("data.txt",'r') as f:
    data_content = f.readlines()

data_content = [x.strip() for x in data_content]

num_letters = len(data_content) / 2

print "\n"

index = 0

for i in range(0,num_letters):

    out_file = str(i) + ". " + data_content[index] + ".txt"

    #find and replace content
    letter = template.replace("<business_name>", data_content[index])
    letter = letter.replace("<sector>", data_content[index+1])

    #print "\nLetter: \n" + letter + "\n"

    file = open(out_file,'w')
    file.write(letter)
    file.close()
    print "Letter " + str(i+1) + " generated.\n"

    index += 2
