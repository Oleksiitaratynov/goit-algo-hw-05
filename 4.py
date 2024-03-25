def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return "Give me name and phone please."
        except KeyError as e:
            return "No such contact found."
        except IndexError as e:
            return "Provide full information, please."
    return inner

@input_error
def get_contact(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"