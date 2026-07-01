---
category: crypto-web3
date: 2025-05-10
id: 233816
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to find the correct coin ID for use with the CoinGecko
  API.
tags:
- coingecko-api
- coin-id
- api-explorer
- crypto-data
---
# how do you check correct id on coingecko api explorer?

### USER
how do you check correct id on coingecko api explorer?

### GEMINI
To check the correct ID on the CoinGecko API Explorer, you have a few reliable methods: Refer to the Coin's Dedicated Page on CoinGecko: Go to the official CoinGecko website (https://www.coingecko.com/). Search for the specific cryptocurrency you are interested in. On the coin's page, look for an "Info" section or similar. Within this section, you will typically find the "API ID". This is the most direct way to get the correct ID. Use the /coins/list Endpoint: The CoinGecko API provides an endpoint specifically to list all supported coins along with their IDs, names, and symbols. You can access this endpoint in the API Explorer. The URL is usually: https://api.coingecko.com/api/v3/coins/list The response will be a JSON array containing objects. Each object will have fields like "id", "symbol", and "name". The value of the "id" field is what you need for other API calls that require the coin ID. Consult the CoinGecko API Documentation: The official CoinGecko API documentation is a comprehensive resource. You can find it here: https://docs.coingecko.com/ or https://docs.coingecko.com/v3.0.1/reference/endpoint-overview for the public API. Within the documentation, especially in the sections describing the /coins/{id} or /simple/price endpoints, it will explicitly mention how to obtain the correct id and often link to the /coins/list endpoint or other methods. Utilize the Provided Google Sheet: CoinGecko sometimes provides a Google Sheet that lists all coins with their API IDs, symbols, and names. The API documentation often links to this sheet. This can be a convenient way to search and find the correct ID. In summary, the best ways to check the correct ID on the CoinGecko API Explorer are to either find it on the specific coin's page on the CoinGecko website or by using the /coins/list API endpoint to get a comprehensive list of all supported coins and their IDs.
