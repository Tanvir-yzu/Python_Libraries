import requests

response = requests.get("https://candid-licorice-66df5c.netlify.app")

# Now you can use the response object
print(response.status_code)  # Print the status code of the response
print(response.text)  # Print the content of the response