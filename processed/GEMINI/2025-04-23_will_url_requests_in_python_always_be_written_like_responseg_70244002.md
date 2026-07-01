---
category: coding
date: 2025-04-23
id: 506255
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking whether HTTP requests in Python are always made using response.get()
  syntax.
tags:
- python-requests
- http-methods
- api-calls
- beginner-question
---
# will url requests in python always be written like response.get 

### USER
will url requests in python always be written like response.get 

### GEMINI
You're on the right track, but let's clarify the terminology a bit. When you're using the requests library in Python to make an HTTP request (like fetching data from a URL), the method you use corresponds to the HTTP method you want to employ. For making a GET request (which is what you're doing to fetch the Solana price), you indeed use requests.get(). This is the most common type of request and is used to retrieve data from a server. However, HTTP has other methods besides GET, and the requests library provides corresponding functions for them as well: POST: Used to send data to a server to create or update a resource. In requests, you would use requests.post(). PUT: Used to send data to a server to update or replace a resource. The corresponding requests function is requests.put(). DELETE: Used to request that the server delete a resource. You would use requests.delete(). HEAD: Similar to GET, but it only retrieves the headers of the response, without the body. The requests function is requests.head(). OPTIONS: Used to ask the server about the HTTP methods it supports for a given URL. The requests function is requests.options(). So, while you use response = requests.get(url) specifically for making a GET request to a URL, the requests library offers a suite of functions (post, put, delete, head, options) that mirror the different HTTP methods you might need to use when interacting with web services and APIs. In summary, requests.get() is the specific way to perform a GET request using the requests library. The requests library provides other functions for different types of HTTP requests.
