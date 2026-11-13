
from decimal import Decimal


# Calculate complete meals
def calculate_meals(quantity, meal_size_kg=0.40):

    quantity = Decimal(str(quantity))
    meal_size = Decimal(str(meal_size_kg))

    return int(quantity // meal_size)


# Classify pickup priority
def classify_priority(hours):

    if hours <= 4:
        return "CRITICAL"

    elif hours <= 12:
        return "PRIORITY"

    else:
        return "NORMAL"


# Generate donation summary
def summarize_donations(donations):

    total_quantity = sum(
        donation.quantity_kg for donation in donations
    )

    total_meals = sum(
        calculate_meals(donation.quantity_kg)
        for donation in donations
    )

    priority_counts = {
        "CRITICAL": 0,
        "PRIORITY": 0,
        "NORMAL": 0
    }

    for donation in donations:

        priority = classify_priority(
            donation.hours_to_expiry
        )

        priority_counts[priority] += 1

    return total_quantity, total_meals, priority_counts
