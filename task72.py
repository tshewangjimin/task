def calculate_area(length, width):
    return length * width

def calculate_discounted_price(original_price, discounted_percentage):
    discount = original_price * (discounted_percentage/100)
    return original_price - discount 

def apply_discount(original_price, discount_percentage):
    discount_price = calculate_discounted_price(original_price,discount_percentage)
    return f"The discounted price is:{discount_price}"

def shopping_cart(original_price, discount_percentage):
    message = apply_discount(original_price, discount_percentage)
    print(message)

shopping_cart(50, 20)