def open_file(mode) :
    f = open("friend-list.txt", mode)
    text = input("write : ") + "\r\n"
    f.write(text)
    f.close()
    

mode = input("w.new a.append")
open_file(mode)
