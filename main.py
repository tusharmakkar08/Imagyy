import json, urllib, webbrowser

def get_profile_id(username):
    """
    Input : Username
    Output : Profile Id 
    """
    url = "http://graph.facebook.com/" + username
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data['id']
    
def open_image_page(profile_id):
    """
    Input : Profile Id 
    Output : Opens a new tab with graph search results
    """
    new_url = "https://www.facebook.com/search/"+profile_id+"/photos-of"
    webbrowser.open_new_tab(new_url)

def main():
    username = raw_input("Enter the Username : ")
    user_id = get_profile_id(username)
    open_image_page(user_id)
    print ""
    return 0

if __name__ == '__main__':
    main()
