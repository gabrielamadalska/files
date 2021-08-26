grade = int(input("Enter a number: ")) 
list = list(range(1,grade + 1))     #tworzenie listy, gdzie maksem jest wybrana liczba tym samym dzielnik


new_list= []        #nowa lista, żeby wrzucić tu dzielniki
for element in list:
    if grade % element == 0:
        
        new_list.append(element)
print(new_list)
