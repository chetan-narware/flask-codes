import requests

class Post:
    def __init__(self,num) -> None:
        self.num = int(num)  # Ensure the num is an integer

    def blog(self):
        url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(url=url)
        data = response.json()
        for d in data:
            if d["id"] == self.num:
                print(d)
                return d
        return None  # Handle case where no post is found
    def titles(self):
        url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(url=url)
        data = response.json()
        return data
            
