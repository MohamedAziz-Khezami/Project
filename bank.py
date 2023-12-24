ph=input("Greeting: ")
ph=ph.lower()
match ph:
    case "hey" | "how you doing?":
        print("$20")
    case "what's happening?" | "what's up?":
        print("$100")
    case _:
        print("$0")
