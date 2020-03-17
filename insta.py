
class upload:
  def __init__(self, fname, caption):
    from InstagramAPI import InstagramAPI
    path = 'source/'+fname
    InstagramAPI = InstagramAPI('Username', 'Password')
    InstagramAPI.login() 
    InstagramAPI.uploadPhoto(path, caption=caption)
