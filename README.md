
# Auth0 Machine to Machine API

A simple FastAPI app with Auth0 Machine to Machine API implementation. 


Run the app:
```bash
python3 main.py
```

To fetch fresh Access Token:
```bash
curl --request POST \
  --url 'https://{yourDomain}/oauth/token' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data grant_type=client_credentials \
  --data client_id=YOUR_CLIENT_ID \
  --data client_secret=YOUR_CLIENT_SECRET \
  --data audience=YOUR_API_IDENTIFIER
```