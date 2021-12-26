alpha = ["a", "b", "c","d","e","f","g","h","i","j","k","l", "m","n","o","p", "q","r","s","t", "u","v","w","x","y","z"]

def back(text, num) :
    after = ""
    for line in lines :
        for c in line :
            if c in alpha :
                after += alpha[(alpha.index(c)+num)%26]
            else :
                after += c
    return after          

    
f = open("caesar_chiper.txt", "r")

lines = f.readlines()

f.close()
after = back(lines, 3)

print(after)
