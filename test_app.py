from app import getabstract

def test_wiki():
   url = 'https://en.wikipedia.org/w/api.php'
   params = {
            'action': 'parse',
            'page': "Hello",
            'format': 'json',
            'prop':'text',
            'redirects':''
            }
 
   response = requests.get(url, params=params)
   data = response.json()
 
   raw_html = data['parse']['text']['*']
   soup = BeautifulSoup(raw_html,'html.parser')
   soup.find_all('p')
   text = ''
 
   for p in soup.find_all('p'):
      text += p.text
      pass
   
   assert getabstract("Hello")==text
