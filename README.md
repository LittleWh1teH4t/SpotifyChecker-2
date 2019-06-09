# SpotifyChecker
Credential stuffing program for Spotify. This program was made for educational purposes only. I am not responsible for what you use this for.

## Installation
1. Install the latest version of Python from [here](https://www.python.org/downloads/)
2. Use the `pip` command to install the requirements
```bash
pip install requests
pip install colorama
pip install beautifulsoup4
```
## Usage
1. Visit [this url](https://accounts.spotify.com/en/login/) and look for a cookie called `__bon`
![](https://a.cozy.cat/igxzx.png)
2. Replace `putyourownbonhere` in the `cookie` payload with the `__bon` cookie you got earlier
3. Make a new file called `accounts.txt` and put your account list in there, formatted as `user:pass`
4. Open terminal in the directory with your program files, then type `py app.py` to start it
5. Wait for the program to finish, everything will be saved to `hits.txt`
