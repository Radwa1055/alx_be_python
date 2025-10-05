def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling.

    Args:
        numerator (str/float): The numerator of the division.
        denominator (str/float): The denominator of the division.

    Returns:
        str: Result of division or error message.
    """
    try:
        # تحويل المدخلات لأرقام
        num = float(numerator)
        denom = float(denominator)

        # التحقق من القسمة على صفر
        if denom == 0:
            return "Error: Cannot divide by zero."

        # القسمة الناجحة
        return f"The result of the division is {num / denom}"

    except (ValueError, TypeError):
        return "Error: Please enter numeric values only."
