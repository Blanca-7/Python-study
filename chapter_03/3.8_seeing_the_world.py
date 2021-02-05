places = ['los angeles','japan','spain','new york','miami']
print(f"\t\t\t Original: {places}")

# termporarily sorted alphabeticly
print(f"\n\t\t Alphabetical: {sorted(places)}")

# showing original list order
print(f"\n\t\t\t Original: {places}")

# termporarily reversed alphabeticly 
print(f"\nReversed alphabetical: {sorted(places, reverse=True)}")

# showing original list order
print(f"\n\t\t\t Original: {places}")

# reversing list order aka flipped
places.reverse()
print(f"\n\t\t\t Reversed: {places}")


# reversing list again order, back to it's original state
places.reverse()
print(f"\n\t\t\t Reversed: {places}")

# Sorted alphabetically
places.sort()
print(f"\n\t\t Alphabetical: {places}")

# Sorted in reverse alphabetical 
places.sort(reverse=True)
print(f"\n Reverse Alphabetical: {places}")

# Sorted in reverse alphabetical
places.sort(reverse=True)
print(f"\n Reverse Alphabetical: {places}")



