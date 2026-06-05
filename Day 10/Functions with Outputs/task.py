def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "Fucking Diabolical Fam, you didn't enter shite"
    full_name = f_name.title()+ " " + l_name.title()
    return (f"Full Name: {full_name}")

formated_name = format_name(input("Enter Your first name and shit yo:"),input("Enter your last name or some:"))
print(formated_name)

