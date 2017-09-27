print("                    This is a genral knowledge quiz")

playername = input("What is your name: ")
playerage = input("What is your age: ")
text_file = open("Info_Players.txt", "w")

text_file.write("PlayerOne")
text_file.write("\n         Name : " + playername)
text_file.write("\n          Age : " + playerage)

text_file.close()



print (" Answer with the chioices a,b or c ")
print(" Make sure you keep your Caps lock off")
print(" Here are 3 diffrent topics to choose from")
print("     1.  Football")
print("     2.  Music")
print("     3.  General Knowledge")
Menu = input ("Make your Choice [1-3]: ")


level = input("Easy, Medium or Hard?: ")

# FOOTBALL

if level in ['easy','Easy']:
    import footballeasy

if level in ['medium','Medium']:
    import footballmedium

if level in ['hard','Hard']:
    import footballhard
