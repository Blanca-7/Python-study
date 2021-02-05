guests = ["Dr. Einstein","Bruce Lee","Elon Musk"]
invitation = "I'd like to invite you to my dinner Party"

print(f"Dear {guests[0]}, {invitation}")
print(f"Dear {guests[1]}, {invitation}")
print(f"Dear {guests[2]}, {invitation}")
print(f"\nSorry, {guests[0]} is on vacation and won't make it to the Dinner Party!\n")

#Since Dr. Einstein won't make it, we delete his entry and insert Sadhguru as the new one
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
