
print("====================================")
print("   SMART WASTE SEGREGATION SYSTEM")
print("====================================")

waste_data = {
    "banana peel": ["Biodegradable", "Green Bin",
                    "Use for composting."],
    "vegetable waste": ["Biodegradable", "Green Bin",
                        "Use for composting."],
    "paper": ["Recyclable", "Blue Bin",
              "Send for paper recycling."],
    "plastic bottle": ["Recyclable", "Blue Bin",
                       "Clean and send for recycling."],
    "glass bottle": ["Recyclable", "Blue Bin",
                     "Send to a glass recycling centre."],
    "battery": ["Hazardous", "Special Collection",
                "Give to an authorized battery collection centre."],
    "medicine": ["Hazardous", "Special Collection",
                 "Return to an authorized medicine collection point."]
}

while True:
    print("\n1. Identify Waste")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        waste = input("Enter waste item name: ").lower().strip()

        if waste in waste_data:
            category, bin_name, suggestion = waste_data[waste]

            print("\n----- WASTE REPORT -----")
            print("Waste Item:", waste.title())
            print("Category:", category)
            print("Dustbin:", bin_name)
            print("Suggestion:", suggestion)

        else:
            print("\nWaste item not found.")
            print("Please enter another item.")

    elif choice == "2":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
