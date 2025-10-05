def safe_divide(numerator, denominator):
    
    try:
         numerator = float("input(enter the first number ")
         denominator = float("input(enter the second number ")
     
     
         if denominator == 0:
           return "Error: Cannot divide by zero."
       
           return f"The result of the division is {numerator / denominator}"

    except (ValueError, TypeError):
         return "Error: Please enter numeric values only."
