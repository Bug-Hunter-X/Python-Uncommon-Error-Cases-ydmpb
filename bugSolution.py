def function_with_uncommon_error_solution(a, b):
    try:
        result = a / b
        return result
    except (ZeroDivisionError, TypeError) as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
print(function_with_uncommon_error_solution(10, 2))  # Output: 5.0
print(function_with_uncommon_error_solution(10, 0))  # Output: Error: division by zero
print(function_with_uncommon_error_solution(10, "hello")) # Output: Error: unsupported operand type(s) for /: 'int' and 'str'
print(function_with_uncommon_error_solution(10, [1,2])) #Output: Error: unsupported operand type(s) for /: 'int' and 'list'