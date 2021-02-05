guests = ["Dr. Einstein","Bruce Lee","Elon Musk"]
invitation = "I'd like to invite you to my dinner Party"

print(f"Dear {guests[0]}, {invitation}")
print(f"Dear {guests[1]}, {invitation}")
print(f"Dear {guests[2]}, {invitation}")
print(f"\nSorry, {guests[0]} is on vacation and won't make it to the Dinner Party!\n")

#Since Dr. Einstein won't make it, we delete his entry and insert Sadhguru as the new one guest
del guests[0]
guests.insert(0, "Sadhguru")
#alternative way: 
#guests[0]= "Sadhguru"

print(f"Dear {guests[0]}, {invitation}")
print(f"Dear {guests[1]}, {invitation}")
print(f"Dear {guests[2]}, {invitation}")

print("\nDear guests, i'd like to inform you that I found a bigger dinning table! Expect more guests to come!\n")

guests.insert(0, "Jonah Hill")
guests.insert(2, "Adam Sandler")
guests.append("Mila Kunis")

print(f"Dear {guests[0]}, {invitation}")
print(f"Dear {guests[1]}, {invitation}")
print(f"Dear {guests[2]}, {invitation}")
print(f"Dear {guests[3]}, {invitation}")
print(f"Dear {guests[4]}, {invitation}")
print(f"Dear {guests[5]}, {invitation}")

print("\nDear guests, unfortunately the new table won't arrive in time!\n")

rem_0 = guests.pop(0)
print(f"Dear {rem_0}, I deeply apologize to inform you that my Dinner Party is going to be delayed!")

rem_1 = guests.pop(0)
print(f"Dear {rem_1}, I deeply apologize to inform you that my Dinner Party is going to be delayed!")

rem_2 = guests.pop(0)
print(f"Dear {rem_2}, I deeply apologize to inform you that my Dinner Party is going to be delayed!")

rem_3 = guests.pop()
print(f"Dear {rem_3}, I deeply apologize to inform you that my Dinner Party is going to be delayed!\n")

print(guests)

print(f"\nDear {guests[0]} {invitation}")
print(f"Dear {guests[1]} {invitation}")

# Delete last entries in list
del guests[0]
del guests[0]

# Proof for empty list
print(guests)
