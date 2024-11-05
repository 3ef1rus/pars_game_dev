import requests
import json
import csv
auth_key = 'd'
headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'authorization': auth_key,
    'content-type': 'application/json',
    # 'cookie': 'intercom-id-ineyz1by=e35f5b9f-b066-457a-9aff-0a53a0f551fb; intercom-device-id-ineyz1by=e53daf4f-460c-489c-ad59-9c84706e7f2f; swapcard-cookie-consent=%7B%22accepted%22%3Atrue%7D; __stripe_mid=e1417346-a801-431d-8686-ab32cbfd508a693eca; next-i18next=ru-RU; _ga=GA1.1.746820343.1711986307; swapcard-auth-api-refresh-token=eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uSWQiOiI2NjBhZTI1YzAwMmZhNzBmNDI3MTFmOTciLCJ0eXBlIjoicmVmcmVzaC10b2tlbiIsInVzZXJJZCI6IjY0ZDYzZWMxMjZlMDlmNmE1NDI0ZGJmYiIsImlhdCI6MTcxMTk4OTM0MCwiaXNzIjoiYXV0aC1hcGkifQ.OEUEI9HJDC5FEa680wFow4abrnoVhfOnx57j7J-eMW7Iw8LQYOQB6Bqfew0ocPtaYR_AihztAG2cVYXl8IVbYkeqlMsf4DfkZpRe7Y1D5TRvtMqs-RkkTB6g-o0lAABwMZS5BA3M6pJ7ZjX9ol0F-sGSz6sgjBm-tq64sYGHUMBkg4v0KbhvZgQYRtGbtqC6CWmw5r043-pZ7jBTxrY_dNGjLSq03spnPisjgnqqH0-icib7XiiuNScqsemJhwVwI4uAdAMmHZCXk-7Y2B4_AKcSJOjp6YMiO-K1CkU-XQ1GeSQoCPjEbJGV1QbKqwQsugQvPUv2PLCumIx6OjGlOfJHhr383w2wlUNn7x-7GXvfNFR1u28I6ru0jJhmhYHcCsMbp6dtI6i-nUx8XRJv5Wz_EI8J9GzRcJ6Rkw1Y0uN9O89GDhzItQ3Jk8STEqCpFitwzOOvWDctrjnbXRsDVHj71OOxLq8VzLKVufO_U0ORvvD8zz3d3PayHLfLoe2NZEtxnRBJeJVjezDYHHDSHykMbml2J71WgCPRA52MRL9QGkwWrKMsQpWKyoOu9Nsj7IAVIelAJRLu7xrMBf04l9TH8edHRrHRJdPJprFt2N8qnNcjZbKlaLU-kQqEqjNSqzl8LLOg2xvvfU1y-hYQuN5BB2dwUB_cnKV4tdUqQYA; __stripe_sid=76346eba-8ea1-4bc0-bef5-621d4edc15437a7e56; intercom-session-ineyz1by=eDJXb1N6M2owblM2YmgrdG5aeWxnWTJvY1Vza2RRcEFBWTk3aWxsbS81end6S1VwUUZGNFZzWkpFR3p4b2huby0tOWdUa1JmL3VvQVpxN1B0MldxQXRPdz09--a73ea1e3e8dfff6839f8fce3ffc7fb77ab63cc72; _ga_VWQ0TSBSYY=GS1.1.1712840847.12.1.1712842860.60.0.0',
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
endCursor = None
json_data = [

    {
        'operationName': 'EventPeopleListViewConnectionQuery',
        'variables': {
            'viewId': 'RXZlbnRWaWV3XzY2OTQyNw==',
            'sort': None,
            'endCursor': endCursor,
        },
        'extensions': {
            'persistedQuery': {
                'version': 1,
                'sha256Hash': 'a4e69f9646845582e7665a1d5f91ace0c1e84ee58197fb4e6b91cb57c4c70367',
            },
        },
    },
]

response = requests.post(
    'https://attend.gdcevents.gdconf.com/api/graphql', headers=headers, json=json_data)


json_data = json.dumps(response.json(), indent=2)
# Предположим, что у вас есть JSON-строка json_data
# Преобразуем JSON-строку обратно в объект Python


print(json_data)
