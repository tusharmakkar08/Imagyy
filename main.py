import json, re, requests, sys, urllib, webbrowser

def get_profile_id_fbv1(username):
    """
    Input : Username
    Output : Profile Id 
    """
    url = "http://graph.facebook.com/" + username
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data['id']
    
def get_profile_id_fbv2(username):
    """
    Input : Username
    Output : Profile Id 
    """
    requestData = requests.post("http://findmyfbid.com/", data={'url':username})
    print requestData.text

def open_image_page(profile_id):
    """
    Input : Profile Id 
    Output : Opens a new tab with graph search results
    """
    new_url = "https://www.facebook.com/search/"+profile_id+"/photos-of"
    webbrowser.open_new_tab(new_url)

def main():
    username = raw_input("Enter the Username : ")
    user_html = get_profile_id_fbv2(username)
    user_id = get_user_id(user_html)
    sys.exit(0)
    open_image_page(user_id)
    print ""
    return 0

if __name__ == '__main__':
    main()
