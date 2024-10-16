class InvalidDomainException(Exception):  # defines custom exception class
    pass


def parse_email(email_address):
    username, domain = email_address.split("@")
    if "." not in domain:
        raise InvalidDomainException(f"domain '{domain}' doesn't contain '.'")
    return username, domain


if __name__ == "__main__":
    email_addresses = [
        "jane.doe@example.com",
        "jane.doeexample.com",
        "john@@example.com",
        "john.doe@example.com",
        "john@example",
    ]
    for email in email_addresses:
        try:
            user, dom = parse_email(email)
        except (ValueError, InvalidDomainException) as ex:
            print(f"Error ({ex}) for {email}")
        except SystemError:
            print("There can be multiple except clauses")
        else:
            print(f"Hello, {user}!")
        finally:
            print("Executes every time")
