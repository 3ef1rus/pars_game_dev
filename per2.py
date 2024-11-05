import json
import requests

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3JlQXBpVXNlcklkIjoiVlhObGNsOHhOVFU0TXpFeU9RPT0iLCJwZXJtaXNzaW9ucyI6W10sInNlc3Npb25JZCI6IjY2MGFlMjVjMDAyZmE3MGY0MjcxMWY5NyIsInR5cGUiOiJhY2Nlc3MtdG9rZW4iLCJ1c2VySWQiOiI2NGQ2M2VjMTI2ZTA5ZjZhNTQyNGRiZmIiLCJpYXQiOjE3MTI5MDkzNzksImV4cCI6MTcxMjkyMzc3OSwiaXNzIjoiYXV0aC1hcGkifQ.kAVD3w7Z951Gwdr9QrrPrF3TStTJGOccQmNL0zh3brR0_wYCz8B3eyIUYSi_yUpaHy2Moim2vTZQ2Z9YaJ4yg-HtQ5T9AM18AFeEAF4wGjP2zgmmzVlMtMCIJghubE9hf4NnXLJBAXvQ-0asZykdaHnw0tb3UlVPbSIKAx3rF25tq-mgIJIwdmtoTM_FWIqwFYQcjXCnBT9JvywSoOBU2PzL42Lu-NgRAnsbDOqKQiJ_y7FvWCsc2a63Xr-9jgF5Ws6F0aBIkKPD-wEVgj3ooKAD0ut5ILyCkuZFLQxugoNDriCSgvEQ200bgLxijtIc1uQ2mboXXR1v8vYscIcb5asZxJ7EimxORpKe5DmMqLEG3nDYXn3Rxmsaq8k-VO_A1ITl1aDCPgPWrGOgVJjbjnpsqFEDZpWtMM53g0jKxD9vyjClnX4pirxMfHXVle0r0SqSM8dKKAm0z9wuIUcFQnMahVpc3lm6plDmzFlvnKEY0rvkBQ9qYow91-ZpPzXCHve7dzzwC0qO3R7j3WmbXjN86W0Mj0dPP6OTczB49ga29Dw7cazEopGUtW_0edB9zdjsPOR7ttghUIJmHwCNAfCXCtCSQKpEjwsaz56TBVzuXrg71RrGJJoS_0OKhTir8hjcBsf5Y4L7v7bSSE9ox4PV33RctAyFazU9C8yUsL4',
    'content-type': 'application/json',
    # 'cookie': 'intercom-id-ineyz1by=e35f5b9f-b066-457a-9aff-0a53a0f551fb; intercom-device-id-ineyz1by=e53daf4f-460c-489c-ad59-9c84706e7f2f; swapcard-cookie-consent=%7B%22accepted%22%3Atrue%7D; __stripe_mid=e1417346-a801-431d-8686-ab32cbfd508a693eca; next-i18next=ru-RU; _ga=GA1.1.746820343.1711986307; swapcard-auth-api-refresh-token=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiI2NjBhZTI1YzAwMmZhNzBmNDI3MTFmOTciLCJ0eXBlIjoicmVmcmVzaC10b2tlbiIsInVzZXJJZCI6IjY0ZDYzZWMxMjZlMDlmNmE1NDI0ZGJmYiIsImlhdCI6MTcxMTk4OTM0MCwiaXNzIjoiYXV0aC1hcGkifQ.OEUEI9HJDC5FEa680wFow4abrnoVhfOnx57j7J-eMW7Iw8LQYOQB6Bqfew0ocPtaYR_AihztAG2cVYXl8IVbYkeqlMsf4DfkZpRe7Y1D5TRvtMqs-RkkTB6g-o0lAABwMZS5BA3M6pJ7ZjX9ol0F-sGSz6sgjBm-tq64sYGHUMBkg4v0KbhvZgQYRtGbtqC6CWmw5r043-pZ7jBTxrY_dNGjLSq03spnPisjgnqqH0-icib7XiiuNScqsemJhwVwI4uAdAMmHZCXk-7Y2B4_AKcSJOjp6YMiO-K1CkU-XQ1GeSQoCPjEbJGV1QbKqwQsugQvPUv2PLCumIx6OjGlOfJHhr383w2wlUNn7x-7GXvfNFR1u28I6ru0jJhmhYHcCsMbp6dtI6i-nUx8XRJv5Wz_EI8J9GzRcJ6Rkw1Y0uN9O89GDhzItQ3Jk8STEqCpFitwzOOvWDctrjnbXRsDVHj71OOxLq8VzLKVufO_U0ORvvD8zz3d3PayHLfLoe2NZEtxnRBJeJVjezDYHHDSHykMbml2J71WgCPRA52MRL9QGkwWrKMsQpWKyoOu9Nsj7IAVIelAJRLu7xrMBf04l9TH8edHRrHRJdPJprFt2N8qnNcjZbKlaLU-kQqEqjNSqzl8LLOg2xvvfU1y-hYQuN5BB2dwUB_cnKV4tdUqQYA; intercom-session-ineyz1by=Qm9XTkI3REp3OE5wbFovbUZ2QTdMZ090eENDMEMyUC9YZzcrMHRTNkRxMlEyWjFmcWxnSWNxbUhweXBydlN4ZC0ta1pXQzR2c1BRZW12dzROL1RZQnY4UT09--a19f249e7bbdc080232e19876aeef2b602ec0ff1; _ga_VWQ0TSBSYY=GS1.1.1712909313.14.0.1712909380.60.0.0',
    'origin': 'https://attend.gdcevents.gdconf.com',
    'referer': 'https://attend.gdcevents.gdconf.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-client-origin': 'attend.gdcevents.gdconf.com',
    'x-client-platform': 'Event App',
    'x-client-version': '2.308.37',
}

json_data = [
    {
        'operationName': 'CurrentEventPersonProviderQuery',
        'variables': {
            'eventId': 'RXZlbnRfMTY4MzkxNQ==',
        },
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': '6d731832c717dfd97567da6934ba7e609e89dc9daad212ff9ff2bd73f8fea6ad',
            },
        },
    },
    {
        'operationName': 'ContentViewAdsQuery',
        'variables': {
            'eventSlug': 'game-developers-conference-2024',
        },
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': '941de0c4ddd8cf381fc8a2d929aa818c2c80bf2e88f190cfb9d45984012698f7',
            },
        },
    },
    {
        'operationName': 'PersonUserId',
        'variables': {
            'personId': 'RXZlbnRQZW9wbGVfMjkzMTY4MTA=',
        },
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': '109137c30f77f624ffa4263a20e90a0a4fc9e9e7ddade6a7a5039a935b69e1b0',
            },
        },
    },
    {
        'operationName': 'EventPersonDetailsQuery',
        'variables': {
            'skipMeetings': True,
            'withEvent': True,
            'personId': 'RXZlbnRQZW9wbGVfMjkzMTY4MTA=',
            'userId': '',
            'eventId': 'RXZlbnRfMTY4MzkxNQ==',
        },
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': '8277c430fdaca5eb97969046e434f876a09af31e8e7940ed50ec234e9c052e77',
            },
        },
    },
    {
        'operationName': 'SingleCommunityQuery',
        'variables': {},
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': '0fbbcdbf8bde4a9b8986bb9982f3d875d0ffb56f8e742c28ec9e958cc2729f8c',
            },
        },
    },
    {
        'operationName': 'ApplicationProvider_CurrentCommunity',
        'variables': {
            'communitySlug': 'game-events',
        },
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': '23de4b566f56b122085ecc57cbb5a46c62c7d13c363293f4d100b16f2c1ee477',
            },
        },
    },
]

response = requests.post('https://attend.gdcevents.gdconf.com/api/graphql',
                         headers=headers, json=json_data)
print(response.status_code)

print(response.json())
json_data = json.dumps(response.json(), indent=2)

# Запись JSON-данных в файл
print(json_data)
