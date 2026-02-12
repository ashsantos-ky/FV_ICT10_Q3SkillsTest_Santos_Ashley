from pyscript import document, display

password = document.getElementById("password").value

# Check if password meets all requirements
has_error = False

if len(password) < 10:
    display("Password must be at least 10 characters long.")
    has_error = True

if not any(c.isalpha() for c in password):
    display("Password must contain at least one letter.")
    has_error = True

if not any(c.isdigit() for c in password):
    display("Password must contain at least one number.")
    has_error = True

if not has_error:
    display("Password is valid.")

    