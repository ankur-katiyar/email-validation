import pandas as pd

# import swifter
from email_validator import validate_email, EmailNotValidError


df = pd.read_csv("email_addresses.csv")
from datetime import datetime

start_time = datetime.now()


def evalid(email):
    i = 0
    count = 0
    ir = []
    email = email.to_string(index=False)
    # print(type(email))
    try:
        email = validate_email((email)).email  # (was added in the initial code)
        # print(email)
        return email
    except EmailNotValidError as e:
        # print(e)
        return str(e)
        ir.append(email)
        count += 1
    i += 1
    # print(str(i)+' done')
    # print(str(count)+ ' total records impacted: ', ir)


fdf = df.apply(evalid, axis=1, result_type="broadcast")
end_time = datetime.now()
print("Duration: {}".format(end_time - start_time))
# import pdb
# pdb.set_trace()
