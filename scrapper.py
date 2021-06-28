from bs4 import BeautifulSoup
import requests
import art
art.tprint("Cricket")
url = "https://www.espncricinfo.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text,'html.parser')
featured = soup.find('div', class_ = "featured-scoreboard slick-slider-container")
matchlinks = []
currentMatches = featured.find_all('div', class_ = "match-info match-info-HSB card scorecard")
print("Latest Matches \n")
for i in currentMatches:
    nameDetail = i.find_all('div', class_ = "name-detail")
    teams = []
    for j in nameDetail:
        teamName = j.find('p', class_ = "name")
        teams.append(teamName.text)
    statusdiv = i.find('div', class_='status-text')
    status = statusdiv.find('span').text
    if (status == 'null'):
        teams.append("Match delayed")
    else:
        teams.append(status)
    print(f"{teams[0]} vs {teams[1]}  -  {teams[2]}")
    for a in i.find_all('a', href=True):
        print ("Found the URL:", a['href'])
    print("\n")