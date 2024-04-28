import requests
import time
import json
print("welcome to the news app".title().center(150))
underline=("*" * 150)
def headlines(category):
    """THIS FUNCTION IS USED FOR TAKING TOP HEADLINES FROM THE API WHICH IS NEWS API"""
    try:
        website_api = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=21d530392e9a4227b7b083e93ecbe0b4")#URL WITH API KEY
        #"""BY USING STATUS I AM CHECKING IS THE WEBSITE ALLOWING OR NOT IF THE STATUS IS 200"""
        status = website_api.status_code
        website_api.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        if status == 200:
            parser_api = json.loads(website_api.text)   # IT IS USED TO PARSE API USING.TEXT AND JSON.LOADS BY USING THIS IT GIVE GIVE RESULTS IN READABLE FORM
            print(underline)
            results=(parser_api["totalResults"])  # IT IS PRESENT IN THE API AND GIVES TOTAL RESULTS
            print(f"The total Headlines in this {category} category are:{results}")
            if results==0:
                print("There is no Top headline in this category ")
            print(underline)
            for news in parser_api["articles"]:   # IT IS THE DICTIONARY PRESENT IN THE API
                print(news["title"])   # IT IS THE ANOTHER DICTIONARY PRESENT IN THE ARTICLE DICTIONARY
                print(news["description"])   # IT IS ALSO THE ANOTHER PRESENT IN THE ARTICLE DICTIONARY
                print(news["url"])   # THIS URL IS ALSO ANOTHER DICTIONARY PRESENT IN THE ARTICLE DICTIONARY
                print(underline)
        else:
            print(f"The website is not allowing to get its information {status}")
    except requests.exceptions.MissingSchema:  # raise error if there is no http or https
        print("THERE IS NO [HTTP] OR [HTTPS] IN GIVEN URL")
    except Exception as e:
        print(f"There is problem in this.The problem is this {e}")
def everything(topic):
    """THIS FUNCTION IS USED FOR TAKING ALL THE NEWS ON GIVEN TOPIC FROM THE WORLD FROM THE API WHICH IS NEWS API"""

    try:
        time_from=input("From when you want the news [give time in this format:YYYY-MM-DD]:")   # THIS WILL TAKE TIME FROM USER AND ASK USER FROM WHAT TIME THE USER REQUIRES NEWS
        time_to=time.strftime("%Y-%m-%d")    # IT WILL GIVE LATEST DATE
        website_api=requests.get(f"https://newsapi.org/v2/everything?q={topic}&from={time_from}&to={time_to}&sortBy=publishedAt&apiKey=21d530392e9a4227b7b083e93ecbe0b4")
        # """BY USING STATUS I AM CHECKING IS THE WEBSITE ALLOWING OR NOT IF THE STATUS IS 200"""
        status = website_api.status_code
        website_api.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        if status == 200:
            parser_api=json.loads(website_api.text)   # IT IS USED TO PARSE API USING.TEXT AND JSON.LOADS BY USING THIAS IT GIVE GIVE RESULTS IN READABLE FORM
            print(underline)
            results = (parser_api["totalResults"])
            print(f"The total Headlines in this {topic} category are:{results}")
            if results == 0:
                print("There is no Top headline in this category ")
            print(underline)
            for news in parser_api["articles"]:
                sources=news["source"]  # THIS IS THE DICTIONARY PRESENT IN THE ARTICLES DICTIONARY WHICH TELLS ABOUT THE NEWS PROVIDER
                sources_details=(sources["name"])   # THIS IS THE VALUE PRESENT IN THE SOURCE DICTIONARY
                print(f"\nNews given by this source: {sources_details}")
                print(news["title"])   # IT IS THE DICTIONARY PRESENT IN THE API
                print(news["description"])  # IT IS ALSO THE ANOTHER PRESENT IN THE ARTICLE DICTIONARY
                print(news["url"])   # THIS URL IS ALSO ANOTHER DICTIONARY PRESENT IN THE ARTICLE DICTIONARY
                print(news["publishedAt"])   # THIS IS THE DICTIONARY PRESENT IN THE ARTICLE DICTIONARY WHICH WILL TELL ABOUT THE TIME OF PUBLISHMENT
                print(underline)
        else:
            print(f"The website is not allowing to get its information {status}")
    except requests.exceptions.MissingSchema:  # raise error if there is no http or https
        print("THERE IS NO [HTTP] OR [HTTPS] IN GIVEN URL")
    except Exception as e:
        print(f"The problem occurring is this {e}")
def menu():
    """THIS IS THE FUNCTION WHICH WILL APPEAR TO THE USER AS A MENU"""
    try:
        while True:
            url=input("1.Top headlines\n2.Everything\nGive the value according to your interest-:")
            if url=="1":
                topic = input("Category of the news are:\nbusiness\nentertainment\ngeneral\nhealth\nscience\nsports\ntechnology\nIn which category do you want the news:".title())
                headlines(topic)
                break
            elif url=="2":
                topics ="Category of the news are:\nbusiness\nentertainment\ngeneral\nhealth\nscience\nsports\ntechnology\nIn which category do you want the news:".title()
                topic=input(f"{topics}\nIn which topic you want the news:")
                everything(topic)
                break
            else:
                print("GIVE VALUE ONLY IN 1 AND 2")
    except Exception as e:
        print(f"The problem occurred is this {e}\nSorry for the inconvenience")
menu()
while True:
    ask=(input("Do you want to continue[c] to get news or to quit it[q]:").title())
    if ask=="C":
        menu()
    elif ask=="Q":
        print("You have successfully exited from the news app")
        break
    else:
        print("Give your answer only in C or E")
