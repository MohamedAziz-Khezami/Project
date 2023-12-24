exp=input("Expression: ")

x,y,z=exp.split(" ")

match y:
    case "+":
        print(f"{float(int(x)+int(z)):.1f}")
    case "-":
         print(f"{float(int(x)-int(z)):.1f}")
    case "*":
         print(f"{float(int(x)*int(z)):.1f}")
    case "/":
         print(f"{float(int(x)/int(z)):.1f}")