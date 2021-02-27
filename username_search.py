import requests
import json

def username_search(username):
        instagram = 'https://api.instantusername.com/check/instagram/' + username
        tiktok = 'https://api.instantusername.com/check/tiktok/' + username
        twitter = 'https://api.instantusername.com/check/twitter/' + username
        facebook = 'https://api.instantusername.com/check/facebook/' + username
        youtube = 'https://api.instantusername.com/check/youtube/' + username
        medium = 'https://api.instantusername.com/check/medium/' + username
        reddit = 'https://api.instantusername.com/check/reddit/' + username
        github = 'https://api.instantusername.com/check/github/' + username
        qoura = 'https://api.instantusername.com/check/quora/' + username
        crunchyroll = 'https://api.instantusername.com/check/crunchyroll/' + username
        ebay = 'https://api.instantusername.com/check/ebay/' + username
        giphy = 'https://api.instantusername.com/check/giphy/' + username
        imgur = 'https://api.instantusername.com/check/imgur/' + username
        itchio = 'https://api.instantusername.com/check/itch.io/' + username
        myanimelist = 'https://api.instantusername.com/check/myanimelist/' + username
        pastebin = 'https://api.instantusername.com/check/pastebin/' + username
        replit = 'https://api.instantusername.com/check/repl.it/' + username
        spotify = 'https://api.instantusername.com/check/spotify/' + username
        steam = 'https://api.instantusername.com/check/steam/' + username
        tinder = 'https://api.instantusername.com/check/tinder/' + username
        twitch = 'https://api.instantusername.com/check/twitch/' + username
        virustotal = 'https://api.instantusername.com/check/virustotal/' + username

        username_search.users = []

        instagram_check = requests.get(instagram)
        ins = instagram_check.text
        instagram_check_json = json.loads(ins)
        instagram_check_json_true = instagram_check_json["available"]
        if instagram_check_json_true:
                username_search.insta = instagram_check_json["url"]
                username_search.users.append(username_search.insta)

        twitter_check = requests.get(twitter)
        twi = twitter_check.text
        twitter_check_json = json.loads(twi)
        twitter_check_json_true = twitter_check_json["available"]
        if twitter_check_json_true:
                username_search.tweet = twitter_check_json["url"]
                username_search.users.append(username_search.tweet)

        tiktok_check = requests.get(tiktok)
        tik = tiktok_check.text
        tiktok_check_json = json.loads(tik)
        tiktok_check_json_true = tiktok_check_json["available"]
        if tiktok_check_json_true:
                username_search.tiktok = tiktok_check_json["url"]
                username_search.users.append(username_search.tiktok)

        facebook_check = requests.get(facebook)
        fac = facebook_check.text
        facebook_check_json = json.loads(fac)
        facebook_check_json_true = facebook_check_json["available"]
        if facebook_check_json_true:
                username_search.face = facebook_check_json["url"]
                username_search.users.append(username_search.face)

        youtube_check = requests.get(youtube)
        you = youtube_check.text
        youtube_check_json = json.loads(you)
        youtube_check_json_true = youtube_check_json["available"]
        if youtube_check_json_true:
                username_search.youtube = youtube_check_json["url"]
                username_search.users.append(username_search.youtube)

        medium_check = requests.get(medium)
        med = medium_check.text
        medium_check_json = json.loads(med)
        medium_check_json_true = medium_check_json["available"]
        if medium_check_json_true:
                username_search.medium = medium_check_json["url"]
                username_search.users.append(username_search.medium)

        reddit_check = requests.get(reddit)
        red = reddit_check.text
        reddit_check_json = json.loads(red)
        reddit_check_json_true = reddit_check_json["available"]
        if reddit_check_json_true:
                username_search.reddit = reddit_check_json["url"]
                username_search.users.append(username_search.reddit)

        github_check = requests.get(github)
        git = github_check.text
        github_check_json = json.loads(git)
        github_check_json_true = github_check_json["available"]
        if github_check_json_true:
                username_search.github = github_check_json["url"]
                username_search.users.append(username_search.github)

        qoura_check = requests.get(qoura)
        qour = qoura_check.text
        qoura_check_json = json.loads(qour)
        qoura_check_json_true = qoura_check_json["available"]
        if qoura_check_json_true:
                username_search.qoura = qoura_check_json["url"]
                username_search.users.append(username_search.qoura)

        crunchyroll_check = requests.get(crunchyroll)
        cru = crunchyroll_check.text
        crunchyroll_check_json = json.loads(cru)
        crunchyroll_check_json_true = crunchyroll_check_json["available"]
        if crunchyroll_check_json_true:
                username_search.crunchyroll = crunchyroll_check_json["url"]
                username_search.users.append(username_search.crunchyroll)

        ebay_check = requests.get(ebay)
        eba = ebay_check.text
        ebay_check_json = json.loads(eba)
        ebay_check_json_true = ebay_check_json["available"]
        if ebay_check_json_true:
                username_search.ebay = ebay_check_json["url"]
                username_search.users.append(username_search.ebay)

        giphy_check = requests.get(giphy)
        gip = giphy_check.text
        giphy_check_json = json.loads(gip)
        giphy_check_json_true = giphy_check_json["available"]
        if giphy_check_json_true:
                username_search.giphy = giphy_check_json["url"]
                username_search.users.append(username_search.giphy)

        imgur_check = requests.get(imgur)
        img = imgur_check.text
        imgur_check_json = json.loads(img)
        imgur_check_json_true = imgur_check_json["available"]
        if imgur_check_json_true:
                username_search.imgur = imgur_check_json["url"]
                username_search.users.append(username_search.imgur)

        itchio_check = requests.get(itchio)
        itc = itchio_check.text
        itchio_check_json = json.loads(itc)
        itchio_check_json_true = itchio_check_json["available"]
        if itchio_check_json_true:
                username_search.itchio = itchio_check_json["url"]
                username_search.users.append(username_search.itchio)

        myanimelist_check = requests.get(myanimelist)
        mya = myanimelist_check.text
        myanimelist_check_json = json.loads(mya)
        myanimelist_check_json_true = myanimelist_check_json["available"]
        if myanimelist_check_json_true:
                username_search.myanimelist = myanimelist_check_json["url"]
                username_search.users.append(username_search.myanimelist)

        pastebin_check = requests.get(pastebin)
        pas = pastebin_check.text
        pastebin_check_json = json.loads(pas)
        pastebin_check_json_true = pastebin_check_json["available"]
        if pastebin_check_json_true:
                username_search.pastebin = pastebin_check_json["url"]
                username_search.users.append(username_search.pastebin)

        replit_check = requests.get(replit)
        rep = replit_check.text
        replit_check_json = json.loads(rep)
        replit_check_json_true = replit_check_json["available"]
        if replit_check_json_true:
                username_search.replit = replit_check_json["url"]
                username_search.users.append(username_search.replit)

        spotify_check = requests.get(spotify)
        spo = spotify_check.text
        spotify_check_json = json.loads(spo)
        spotify_check_json_true = spotify_check_json["available"]
        if spotify_check_json_true:
                username_search.spotify = spotify_check_json["url"]
                username_search.users.append(username_search.spotify)

        steam_check = requests.get(steam)
        ste = steam_check.text
        steam_check_json = json.loads(ste)
        steam_check_json_true = steam_check_json["available"]
        if steam_check_json_true:
                username_search.steam = steam_check_json["url"]
                username_search.users.append(username_search.steam)

        tinder_check = requests.get(tinder)
        tin = tinder_check.text
        tinder_check_json = json.loads(tin)
        tinder_check_json_true = tinder_check_json["available"]
        if tinder_check_json_true:
                username_search.tinder = tinder_check_json["url"]
                username_search.users.append(username_search.tinder)

        twitch_check = requests.get(twitch)
        twi = twitch_check.text
        twitch_check_json = json.loads(twi)
        twitch_check_json_true = twitch_check_json["available"]
        if twitch_check_json_true:
                username_search.twitch = twitch_check_json["url"]
                username_search.users.append(username_search.twitch)

        virustotal_check = requests.get(virustotal)
        vir = virustotal_check.text
        virustotal_check_json = json.loads(vir)
        virustotal_check_json_true = virustotal_check_json["available"]
        if virustotal_check_json_true:
                username_search.virustotal = virustotal_check_json["url"]
                username_search.users.append(username_search.virustotal)



        username_search.Str = ' '.join([str(elem) for elem in username_search.users])
