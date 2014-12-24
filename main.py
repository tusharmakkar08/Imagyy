import urllib, json , webbrowser
url = "http://graph.facebook.com/tanya.jain.129"
response = urllib.urlopen(url);
data = json.loads(response.read())
print data['id']
new_url = "https://www.facebook.com/search/"+data['id']+"/photos-of"
webbrowser.open_new_tab(new_url)
