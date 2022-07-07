import requests

print ("hello world")
print ("Saya Widyasiwi")

response = requests.get ("https://google.com")

print (response.text)