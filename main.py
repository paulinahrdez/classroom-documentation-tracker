records = []

children = [
    "Sofia", "Vincenzo", "Amara", "Ritvik", "Avery", "Arjun", "Eeshani", "Maya", "Oskar", "Agni", "Shaan", "Leonardo", "Aizel", "Shreya", "Sayu", "Arya", "Alexander", "Manan", "Amari", "Lily", "Luca", "Hannah"
]

disciplines = [
    "practical life",
    "art",
    "language",
    "sensorial",
    "geography",
    "cultural",
    "food prep",
    "environment care",
    "selfcare",
    "play",
    "water work",
    "math"
]

while True:
    print("\nClassroom Documentation Tracker")
    print("1. Add entry")
    print("2. View all entries")
    print("3. View discipline totals")
    print("4. View child summaries")
    print("5. View missing disciplines per child")
    print("6. Exit")

    choice = input("Chose an option: ")

    # ADD ENTRY
    if choice == "1":
        print("\nChildren:")
        for child in children:
            print("-", child)

        child_name = input("Enter child's name as shown: ").strip()

        if child_name not in children:
            print("Invalid child name.")
            continue
            
        week = input("Enter week code (example: 3wk1): ").strip().lower()
        work = input("Enter work captured: ").strip()

        print("\nAvailable disciplines:")
        for discipline in disciplines:
            print("-", discipline)

        selected_discipline = input("Enter discipline exactly as written: ").strip().lower()

        if selected_discipline in disciplines:
            record = {
                "child": child_name,
                "week": week,
                "work": work,
                "discipline": selected_discipline
            }
            
            records.append(record)
            print("Entry added successfully.")
        else:
            print("Invalid discipline.")

    # VIEW ALL ENTRIES
    elif choice == "2":
        if len(records) == 0:
            print("No entries yet.")
        else:
            print("\nAll Entries:")
            for r in records:
                print(f"{r['child']} | {r['week']} | {r['work']} | {r['discipline']}")

    # DISCIPLINE TOTALS
    elif choice == "3":
        week_filter = input("Enter week code (or press Enter for all): ").strip().lower()

        print("\nDiscipline Totals:")
        for discipline in disciplines:
            count = 0
            for record in records:
                if week_filter == "" or record["week"] == week_filter:
                    if record["discipline"] == discipline:
                        count += 1
            print(f"{discipline}: {count}")

    # CHILD SUMMARIES
    elif choice == "4":
        week_filter = input("Enter week code (or press Enter for all): ").strip().lower()
        
        print("\nChild Summaries:")
        for child in children:
            print(f"\n{child}:")
            for discipline in disciplines:
                count = 0
                for record in records:
                    if week_filter == "" or record["week"] == week_filter:
                        if record["child"] == child and record["discipline"] == discipline:
                            count += 1
                if count > 0:
                    print(f" {discipline}: {count}")

    # MISSING DISCIPLINES
    elif choice == "5":
        week_filter = input("Enter week code: ").strip().lower()

        print("\nMissing Disciplines per Child:")
        for child in children:
            completed = []

            for record in records:
                    if record["week"] == week_filter and record["child"] == child:
                        if record["discipline"] not in completed:
                            completed.append(record["discipline"])
            missing = []
            for discipline in disciplines:
                if discipline not in completed:
                    missing.append(discipline)
                    
            print(f"\n{child} is missing:")
            for m in missing:
                print("-", m)
                
    elif choice == "6":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")