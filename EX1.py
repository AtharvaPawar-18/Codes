A = input("Enter status of Room A (Dirty/Clean): ").capitalize()
B = input("Enter status of Room B (Dirty/Clean): ").capitalize()
location = input("Enter vacuum location (A/B): ").upper()

for i in range(4):
    print("Location:", location)

    if location == "A":
        if A == "Dirty":
            print("Action: Suck")
            A = "Clean"
        else:
            print("Action: Move Right")
            location = "B" 

    else:
        if B == "Dirty":
            print("Action: Suck")
            B = "Clean"
        else:
            print("Action: Move Left")
            location = "A"

print("Final State: ")
print("Room A:", A)
print("Room B:", B)