print "\nLetter Helper"

# read template file

file = open("letter_template.txt",'r')
template = file.read()

# read tags file
with open("tags.txt",'r') as f:
    tags = f.readlines()

tags = [x.strip() for x in tags]

# read data file
with open("data.txt",'r') as f:
    data_content = f.readlines()

data_content = [x.strip() for x in data_content]

num_tags = len(tags)
num_letters = len(data_content) / num_tags

print "\n"

# generate letters

index = 0

for i in range(0,num_letters):

    # take the template

    letter = template

    # find and replace tags
    for j in range(0, num_tags):
        letter = letter.replace(tags[j], data_content[index+j])

    # write the generated letter
    out_file = str(i+1) + ". " + data_content[index] + ".txt"
    file = open(out_file,'w')
    file.write(letter)
    file.close()
    print "Letter " + str(i+1) + " generated.\n"

    index += num_tags

input("Press Enter to exit...")
