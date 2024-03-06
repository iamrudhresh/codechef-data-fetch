import requests
import re
from bs4 import BeautifulSoup as bs

def codechef():
    r = requests.get("https://www.codechef.com/users/rudhresh")
    soup = bs(r.content,"html.parser")
    div_number = soup.find("div", {"class":"rating-header text-center"})

    rankings = soup.find("div", {"class":"rating-ranks"})

    ul_element = rankings.find('ul')

    contestcount = soup.find("div", {"class":"contest-participated-count"})

    # for global ranking
    if ul_element:
        globalrank = ul_element.find('li').text.split()[0]
    else:
      globalrank = "NA"

   # for country ranking
    if ul_element:
      countryrank = ul_element.find_all('li')[1].text.split()[0]
    else:
      countryrank = "NA"

    div_number1 = div_number.find_all("div")

    highestRating = div_number.find('small').text.strip(')').split()[-1]
    L = []
    for tag in div_number1:
        L.append(tag.get_text())

    count = contestcount.find('b').text

    problemscount = []
    prob = soup.find("section", {"class":"rating-data-section problems-solved"})
    a = prob.find_all("h3")
    for i in a:
      problemscount.append(i.get_text())

    ans1 = problemscount[0]
    ans2 = problemscount[1]
    ans3 = problemscount[2]
    ans4 = problemscount[3]


    if not ans1.strip():
      return None
    number1 = re.sub(r"[^\d]", "", ans1)
    if not number1.isdigit():
      return None

    if not ans2.strip():
      return None
    number2 = re.sub(r"[^\d]", "", ans2)
    if not number2.isdigit():
      return None

    if not ans3.strip():
      return None
    number3 = re.sub(r"[^\d]", "", ans3)
    if not number3.isdigit():
      return None

    if not ans4.strip():
      return None
    number4 = re.sub(r"[^\d]", "", ans4)
    if not number4.isdigit():
      return None

    rating = L[0]
    div = L[1]
    star = L[2]
    print("Current Rating:",rating)
    print("Highest Rating:",highestRating)
    print("Division:",div)
    print("Star Rating:",star)
    print("Global Ranking:",globalrank)
    print("Country Ranking:",countryrank)
    print("No. of Contests Participated:",count)
    print(ans1, ans2, ans3, ans4)
    print("Total Problems Solved:",int(number1) + int(number2) + int(number3) + int(number4))

codechef()
