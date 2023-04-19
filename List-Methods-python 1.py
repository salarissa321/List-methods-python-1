

#----------------
#---Lists Methods----
#----------------


# append()

myFriends = ["Salar", "Issa", "Gamel"]
myOldFriends = ["Abo Abass" , "Abo Saed" , "Kasabeh"]
myFriends.append("Raman")
myFriends.append(100)
myFriends.append(24.89)
myFriends.append(True)
myFriends.append(myOldFriends)
print(myFriends) # ['Salar', 'Issa', 'Gamel', 'Raman', 100, 24.89, True] # ['Salar', 'Issa', 'Gamel', 'Raman', 100, 24.89, True, ['Abo Abass', 'Abo Saed', 'Kasabeh']]
print(myFriends[2]) # Gamel
print(myFriends[6]) # True
print(myFriends[7]) # ['Abo Abass', 'Abo Saed', 'Kasabeh']
print(myFriends[7][2]) # Kasabeh

# extend()

a = [1,2,3,4]
b = ["A" , "B" , "C"]
c = [ "One" , "Two"]

a.extend(b)
a.extend(c)
print(a) # [1, 2, 3, 4, 'A', 'B', 'C'] # [1, 2, 3, 4, 'A', 'B', 'C', 'One', 'Two']

# remove()

x = [1,2,3,4, "Salar" , True, "Issa" , "Issa"]
x.remove("Salar")
print(x) # [1, 2, 3, 4, True, 'Issa', 'Issa']


# Sort()

y = [1, 2, 100 , 120 , -10 , 17, 29]
# y = ["A" , "Z" , "C"] # ['Z', 'C', 'A']
y.sort(reverse=True) # [120, 100, 29, 17, 2, 1, -10]
print(y) # [-10, 1, 2, 17, 29, 100, 120] 


# reverse()

r = [1, 4, 6 , 70 , 100 , "Salar" , 150]
r.reverse()
print(r) # [150, 'Salar', 100, 70, 6, 4, 1]




