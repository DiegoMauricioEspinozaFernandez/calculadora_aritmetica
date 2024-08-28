from my_calculator import Calculator
"""def main():
    calculadora = Calculator()
    print(calculadora.sumar(1, 2))
    print(calculadora.dividir(10, 2))

if __name__ == "__main__":
    main()"""
class CalculatorProgram:
    def __init__(self):
        self.calc = Calculator()
    
    
    def run(self):
        
        while True:
            print("\nSelect an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Modulo")
            print("6. Exit")
            
            choice = input("Enter the number of the operation you want to perform (1/2/3/4/5/6): ")

            if choice == '6':
                print("Thank you for using the calculator! Goodbye.")
                break

            if choice in ['1', '2', '3', '4', '5']:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))

                    if choice == '1':
                        print(f"Result: {self.calc.add(num1, num2)}")
                    elif choice == '2':
                        print(f"Result: {self.calc.subtract(num1, num2)}")
                    elif choice == '3':
                        print(f"Result: {self.calc.multiply(num1, num2)}")
                    elif choice == '4':
                        print(f"Result: {self.calc.divide(num1, num2)}")
                    elif choice == '5':
                        print(f"Result: {self.calc.modulo(num1, num2)}")

                except ValueError:
                    print("Error: Please enter valid numbers.")
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    program = CalculatorProgram()
    program.run()
    