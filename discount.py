def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage to apply
    
    Returns:
    float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Display results
    if discount_percent >= 20:
        print(f"Original price: ${original_price:.2f}")
        print(f"Discount applied: {discount_percent}%")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print(f"No discount applied (needs to be 20% or higher). Price remains: ${original_price:.2f}")
        
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")