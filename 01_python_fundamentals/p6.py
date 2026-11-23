subject = "Html"
match subject.upper():
    case "HTML":
        print("Hypertext Markup Language")
    case "CSS":
        print("Cascading Style Sheet")
    case _:
        print("Unknown")