
# =====================================================
# FOOD RESCUE AND SURPLUS DONATION COORDINATION SYSTEM
# Subject: Python Programming (COM-501)
# Group: 9
# File: main.py
# =====================================================

import time

from food_donation import FoodDonation

from rescue_utils import (
    calculate_meals,
    classify_priority,
    summarize_donations
)


FILENAME = "rescue_records.txt"


# -----------------------------------------------------
# GET NEXT UNIQUE DONATION ID
# -----------------------------------------------------

def get_next_donation_number():

    max_id = 0

    try:

        with open(FILENAME, "r") as file:

            for line in file:

                fields = line.strip().split("|")

                if len(fields) == 5:

                    try:

                        number = int(
                            fields[0].strip().replace("D", "")
                        )

                        max_id = max(max_id, number)

                    except ValueError:
                        continue

    except FileNotFoundError:
        pass

    return max_id + 1


# -----------------------------------------------------
# Q5: SAVE DONATION RECORDS
# -----------------------------------------------------

def save_donation(donation):

    try:

        with open(FILENAME, "a") as file:

            file.write(
                f"{donation.donation_id}|"
                f"{donation.donor_name}|"
                f"{donation.food_category}|"
                f"{donation.quantity_kg}|"
                f"{donation.hours_to_expiry}\n"
            )

        print("Donation saved successfully!")

    except OSError as error:

        print("Unable to save donation:", error)


# -----------------------------------------------------
# Q5: READ SAVED DONATION RECORDS
# -----------------------------------------------------

def read_records():

    try:

        with open(FILENAME, "r") as file:

            print("\n========== SAVED RECORDS ==========")

            for number, line in enumerate(file, 1):

                fields = line.strip().split("|")

                # Detect malformed records
                if len(fields) != 5:

                    print("Malformed record at line:", number)
                    continue

                try:

                    donation_id, donor, category, quantity, hours = fields

                    quantity = float(quantity)
                    hours = int(hours)

                    print("\nDonation ID:", donation_id)
                    print("Donor:", donor)
                    print("Category:", category)
                    print("Quantity:", quantity, "kg")
                    print("Remaining Hours:", hours)

                except ValueError:

                    print("Invalid numeric record at line:", number)

    except FileNotFoundError:

        print("Error: Donation record file not found!")


# -----------------------------------------------------
# Q1 AND Q2: MAIN DONATION APPLICATION
# -----------------------------------------------------

def main():

    donations = []

    food_categories = set()

    donation_counter = get_next_donation_number()

    print("\n==========================================")
    print(" FOOD RESCUE AND SURPLUS DONATION SYSTEM")
    print("==========================================")

    print("\nOrganization:", FoodDonation.organization_name)

    print("\nAvailable Food Categories:")
    print("Baked Food")
    print("Fruits")
    print("Vegetables")
    print("Cooked Food")
    print("Dairy Products")

    print("\nEnter DONE as donor name to finish ordering.")

    # Q2: Multiple donation input loop

    while True:

        print("\n--------------------------------")

        donor_name = input("Enter donor name: ").strip()

        if donor_name.upper() == "DONE":
            break

        if not donor_name:

            print("Donor name cannot be empty!")
            continue

        food_category = input("Enter food category: ").strip()

        if not food_category:

            print("Food category cannot be empty!")
            continue

        try:

            quantity = float(
                input("Enter quantity in kg: ")
            )

            hours = int(
                input("Enter remaining hours: ")
            )

            # Validate input

            if quantity <= 0 or hours <= 0:

                print("Invalid donation!")
                print("Quantity and hours must be positive.")
                continue

            # Q1: Display input data types

            print("\n--- INPUT DATA TYPES ---")

            print("Quantity type:", type(quantity))
            print("Remaining hours type:", type(hours))

            # Create donation object

            donation_id = f"D{donation_counter:03d}"

            donation = FoodDonation(
                donation_id,
                donor_name.title(),
                food_category.title(),
                quantity,
                hours
            )

            # Store donation

            donations.append(donation)

            food_categories.add(food_category.title())

            donation_counter += 1

            # Save record

            save_donation(donation)

            # Display donation result

            print("\n--- DONATION RESULT ---")

            print("Donor:", donation.donor_name)

            print("Food Category:", donation.food_category)

            print(
                "Estimated Complete Meals:",
                calculate_meals(quantity)
            )

            print(
                "Pickup Priority:",
                classify_priority(hours)
            )

            print("\nDonation successfully recorded!")

        except ValueError:

            print("\nInvalid numeric input!")
            print("Please enter a valid quantity and hours.")

    # -------------------------------------------------
    # FINAL DONATION SUMMARY
    # -------------------------------------------------

    if len(donations) == 0:

        print("\nNo valid donations were recorded.")

    else:

        print("\n==========================================")
        print("          FINAL DONATION SUMMARY")
        print("==========================================")

        # Q4: Measure processing time

        start_time = time.perf_counter()

        # Q4: Lambda expression for sorting

        sorted_donations = sorted(
            donations,
            key=lambda donation: donation.hours_to_expiry
        )

        print("\n--- PRIORITY-WISE DONATION LIST ---")

        for donation in sorted_donations:

            print(donation)

            print(
                "Estimated Meals:",
                donation.estimated_meals()
            )

        # Q4: Summary function from module

        total_quantity, total_meals, priority_counts = (
            summarize_donations(donations)
        )

        end_time = time.perf_counter()

        print("\n--- TOTAL STATISTICS ---")

        print("Total Donations:", len(donations))

        print("Total Quantity:", total_quantity, "kg")

        print("Total Estimated Meals:", total_meals)

        print("\n--- PICKUP PRIORITY COUNTS ---")

        print("CRITICAL:", priority_counts["CRITICAL"])

        print("PRIORITY:", priority_counts["PRIORITY"])

        print("NORMAL:", priority_counts["NORMAL"])

        print("\nUnique Food Categories:", food_categories)

        print(
            "\nReport Processing Time:",
            round(end_time - start_time, 6),
            "seconds"
        )

    # Q5: Read saved donation records

    read_records()


# -----------------------------------------------------
# PROGRAM EXECUTION
# -----------------------------------------------------

if __name__ == "__main__":

    main()
