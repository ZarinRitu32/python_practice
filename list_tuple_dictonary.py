#1.list
number = [3,4,5,6,7]
number.append(8)  # add
number.remove(4)
print(number)
print("sum is:", sum(number))


#2. tuple
 
city = ("Dhaka", "Rangpur","Sylhet", "Jashore", "Khulna")
print(city[2]) #3rd city

new_city = list(city)
new_city.append("Bogura")
print(new_city)


#3.dictonary

d = {"Bangla":80, "Math":90}
d["Science"] = 95
d["Math"] = 98
print(d)
sum = sum(d.values())
avg = sum/ len(d)
print(sum)
print(avg)