#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
names = []
REPLACE = "[name]"
with open(r".\Input\Names\invited_names.txt") as f:
    for i in f:
        names.append(i.strip())
#Replace the [name] placeholder with the actual name.

with open(r".\Input\Letters\starting_letter.txt") as f:
    x  = f.read().strip()
    for i in names:
        new_letter = x.replace(REPLACE,i)
        with open(f".\Output\ReadyToSend\letter_to_{i}", "w") as o:
            o.write(new_letter)
#Save the letters in the folder "ReadyToSend".