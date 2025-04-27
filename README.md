# Solana Wallet Scraper for X (previously known as a Twitter)

Extract unique Solana wallet addresses from tweet replies — perfect for token airdrops, whitelist building, and Solana community giveaways.

# Features:

Clean extraction of valid Solana addresses (32-44 characters)

Automatically skips duplicates

Handles pagination (fetches more than 100 replies if needed)

Outputs clean .csv file ready for airdrops

Minimal setup (only Python 3 + requests library)

# Requirements:

Python 3 installed

Twitter/X Developer account

Twitter API Bearer Token

# Installation & Setup:

1. Clone the repository

`git clone https://github.com/yourusername/your-repo-name.git`

cd your-repo-name

2. Install required Python libraries

`pip install requests`

3. Edit the script with your credentials

Open twitter_scraper.py and set:

```
bearer_token = 'YOUR_TWITTER_BEARER_TOKEN'
tweet_id = 'TARGET_TWEET_ID'
```

Bearer Token: Found in your Twitter Developer Portal
Tweet ID: It's the number in the tweet URL (https://twitter.com/user/status/TWEET_ID)

# How to Run

In the project folder, simply run:

`python twitter_scraper.py`

After running, a file named wallet_addresses.csv will be created containing:

- One unique Solana wallet address per line

# Example Use Cases

Build token airdrop whitelists from your Twitter audience

Collect wallet addresses from engagement giveaways

Prepare lists for Solana SPL token distribution

# Notes

- Duplicate Checking: Automatically skips duplicate wallet addresses using Python set()

- Pagination Handling: Fetches more than 100 tweet replies automatically

- This script is focused on Solana wallet patterns only (32 to 44 character alphanumeric strings).
