import json, requests, os, time

API_TOKEN = os.getenv("CF_API_TOKEN")
ACCOUNT_ID = os.getenv("CF_ACCOUNT_ID")
PROJECT_NAME = os.getenv("CF_PROJECT_NAME")
API_URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT_NAME}/domains"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

with open("all_domains.txt") as f:
    domains = [line.strip() for line in f if line.strip()]

batch_size = 20
for i in range(0, len(domains), batch_size):
    batch = domains[i:i+batch_size]
    print(f"Adding batch {i//batch_size + 1}: {batch}")
    response = requests.post(API_URL, headers=headers, json={"domains": batch})
    print(response.status_code, response.text)
    time.sleep(1)
