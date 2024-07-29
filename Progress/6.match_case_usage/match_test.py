def runMatch():
    prompt = input("Hello or Goodbye?: ")
    
    match prompt:
        case "Hello":
            print("Hello World")
        case "Goodbye":
            print("Goodbye World")

runMatch()
