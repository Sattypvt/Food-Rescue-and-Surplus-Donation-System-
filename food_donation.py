
from decimal import Decimal


class FoodDonation:

    organization_name = "MIET Food Rescue Organization"

    def __init__(self, donation_id, donor_name, food_category,
                 quantity_kg, hours_to_expiry):

        self.donation_id = donation_id
        self.donor_name = donor_name
        self.food_category = food_category
        self.quantity_kg = quantity_kg
        self.hours_to_expiry = hours_to_expiry

    def estimated_meals(self, meal_size_kg=0.40):

        quantity = Decimal(str(self.quantity_kg))
        meal_size = Decimal(str(meal_size_kg))

        return int(quantity // meal_size)

    def priority_level(self):

        if self.hours_to_expiry <= 4:
            return "CRITICAL"

        elif self.hours_to_expiry <= 12:
            return "PRIORITY"

        else:
            return "NORMAL"

    def display_summary(self):

        print("\n---------- DONATION DETAILS ----------")
        print("Donation ID:", self.donation_id)
        print("Donor Name:", self.donor_name)
        print("Food Category:", self.food_category)
        print("Quantity:", self.quantity_kg, "kg")
        print("Remaining Hours:", self.hours_to_expiry)
        print("Estimated Meals:", self.estimated_meals())
        print("Pickup Priority:", self.priority_level())

    def __str__(self):

        return (
            f"{self.donation_id} | "
            f"{self.donor_name} | "
            f"{self.food_category} | "
            f"{self.priority_level()}"
        )


# Test Q3: Creating donation objects

if __name__ == "__main__":

    donation1 = FoodDonation(
        "D001", "Green Oven Bakery",
        "Baked Food", 8.5, 6
    )

    donation2 = FoodDonation(
        "D002", "Fresh Mart",
        "Fruits", 5.0, 3
    )

    print("Organization:", FoodDonation.organization_name)

    donation1.display_summary()
    donation2.display_summary()

    print("\nObject String Representation:")
    print(donation1)
    print(donation2)
