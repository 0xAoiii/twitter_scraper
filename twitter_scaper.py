import csv
import re
import time

import requests

# Config
bearer_token = 'YOUR_TWITTER_BEARER_TOKEN'
tweet_id = 'YOUR_TWEET_ID'
output_file = 'wallet_addresses.csv'
solana_address_regex = r'\b[1-9A-HJ-NP-Za-km-z]{32,44}\b'

# Twitter API headers
def create_headers(bearer_token):
    return {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "v2ReplyLookupPython"
    }

# Fetch replies with pagination
def get_all_replies(tweet_id, bearer_token):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    headers = create_headers(bearer_token)
    params = {
        'query': f'conversation_id:{tweet_id}',
        'tweet.fields': 'author_id,conversation_id',
        'max_results': 100
    }
    all_replies = []
    next_token = None

    while True:
        if next_token:
            params['next_token'] = next_token

        response = requests.get(search_url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Request error: {response.status_code} {response.text}")

        json_response = response.json()
        if "data" in json_response:
            all_replies.extend(json_response["data"])

        next_token = json_response.get("meta", {}).get("next_token", None)
        if not next_token:
            break
        
        time.sleep(1)  # Be nice to the API, add small delay between calls

    return all_replies

# Extract wallets
def extract_wallets(replies):
    wallets = set()
    for tweet in replies:
        matches = re.findall(solana_address_regex, tweet["text"])
        for match in matches:
            wallets.add(match)
    return list(wallets)

# Save to CSV
def save_wallets(wallets, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["wallet_address"])
        for wallet in wallets:
            writer.writerow([wallet])
    print(f"Saved {len(wallets)} unique wallet addresses to {filename}")

# MAIN
if __name__ == "__main__":
    all_replies = get_all_replies(tweet_id, bearer_token)
    wallets = extract_wallets(all_replies)
    save_wallets(wallets, output_file)
