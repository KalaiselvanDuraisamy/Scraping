from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://www.wego.co.in/')
#soup = BeautifulSoup(source, 'html.parser')
text_file = open('abc.txt', 'w')
text_file.write(r)