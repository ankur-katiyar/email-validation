import pandas as pd
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

start_time = datetime.now()
df = pd.read_csv("email_addresses.csv")
end_time = datetime.now()
print("Read Duration: {}".format(end_time - start_time))


def validate_email_address(email):
    try:
        return validate_email(email).email
    except EmailNotValidError as e:
        return str(e)


# Apply the validate_email() function to each element in the "email" column
fdf = df["email"].str.strip().apply(lambda x: validate_email_address(x))
end_time = datetime.now()
print("DF Apply Duration: {}".format(end_time - start_time))
