import pandas as pd
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from concurrent.futures import ThreadPoolExecutor


def validate_email_addresses_chunk(chunk):
    # Apply the validate_email() function to each element in the chunk
    return chunk.apply(lambda x: validate_email_address(x))


def validate_emails(email):
    try:
        return validate_email((email)).email  # (was added in the initial code)
    except EmailNotValidError as e:
        return str(e)


def validate_email_address(email):
    return email.apply(lambda x: validate_emails(x))


start_time = datetime.now()
# Use chunksize to read the CSV file in smaller chunks
dfs = pd.read_csv("email_addresses.csv", chunksize=100)
with ThreadPoolExecutor() as executor:
    # Apply the validation function to each chunk in parallel
    fdfs = list(executor.map(validate_email_addresses_chunk, dfs))
# Concatenate the results from each chunk into a single DataFrame
fdf = pd.concat(fdfs)
print(fdf)
end_time = datetime.now()
print("DF Apply Duration: {}".format(end_time - start_time))
