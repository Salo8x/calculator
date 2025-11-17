from calculator import Calculator

print("Calculator is Running on main")

c = Calculator()
def display():
    
    operations = ['+','-','/','x']
    print('Welcome which operation you want to perform? or type(exit) to quit.')
    res = input('+, - , x , / : ')
    
    if res == 'exit':
        print("Thank you for your time")
        print("Calculator is exiting, thanks")
        return
    if res in operations:      
        try:
            choice = int(input("How many numbers you want to enter : "))
            l1 = []
            
            for i in range(choice):
                try:
                    num = int(input("Enter the number : "))
                    l1.append(num)
                except ValueError:
                    print("Please enter the integer")
                    again = int(input("Enter the number again : "))
                    l1.append(again)
                
            
            if res == '+':
                result = c.add(l1)
            
            elif res == '-':
                result = c.subtract(l1)
                
            elif res == 'x':
                result = c.multiply(l1)
                
            elif res == '/':
                result = c.divide(l1)
            else:
                print('Please enter the correct operation')
                display()
                
        
            print(result)
            display()
            
        # except ValueError as e:
        #     print('Error :', e)
        
        except Exception as e:
            print("Unexpected error:", e)
            display()
    
    else:
        print('Please enter the valid operation')
        display()

display()

