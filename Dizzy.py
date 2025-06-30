string = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24" #This is our mystry code!! We want Decodding this.

splinter = string.split(' ') #Splinter who is turtles master :)

answer=[] #Finally we have an answer in shape of array
for i in range(100): #We are making an array of 100 elements
    answer.append("*")
    
def print_string_from_list(request):
    print(''.join(request)) #This will print the answer in string format

for part in splinter:
    character = part[0] #This is the first character of each part
    index = int(part[1: ]) #other is the index of that character
    print(character, index) 
    answer[index]=character
    print_string_from_list(answer)
    
print_string_from_list(answer) 