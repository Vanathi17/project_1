def main():
  while True:
    operator = input("Enter an operator (+ - * / ** %): ")

    if operator == "q":
      break

    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    if operator == "+":
      print(num1, "+", num2, "=", num1 + num2)
    elif operator == "-":
      print(num1, "-", num2, "=", num1 - num2)
    elif operator == "*":
      print(num1, "*", num2, "=", num1 * num2)
    elif operator == "/":
      print(num1, "/", num2, "=", num1 / num2)
    elif operator == "**":
      print(num1, "**", num2, "=", num1 ** num2)
    elif operator == "%":
      print(num1, "%", num2, "=", num1 % num2)
    else:
      print(f"{operator} is not a valid operator")

if __name__ == "__main__":
  main()
