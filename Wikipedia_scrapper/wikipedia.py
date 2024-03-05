def get_soup(url):
    from bs4 import BeautifulSoup as bs
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    #     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    with requests.get(url, headers=headers, stream=True) as res:
        soup = bs(res.text, 'html.parser')
    return soup


def get_data(slug="slugName"):
    import re
    from lxml import etree
    import time

    countries = ['Canada', 'Zimbabwe', 'The Republic of Korea', 'The Republic of Zambia', 'Lao', 'Andorra',
                 'United Arab Emirates', 'Afghanistan',
                 'Antigua And Barbuda', 'Syrian Arab Republic', 'Kazakhstan', 'Italy', 'South Africa', 'North Korea',
                 'Russia', 'Taiwan', 'Albania',
                 'Bosnia And Herzegovina', 'Azerbaijan', 'Argentina', 'Armenia', 'Bangladesh', 'Bulgaria', 'Angola',
                 'Anguilla', 'Antarctica', 'American Samoa',
                 'Austria', 'Aruba', 'Åland Islands', 'Barbados', 'Belgium', 'Burkina Faso', 'Bahrain', 'Burundi',
                 'Benin', 'Saint Barthélemy', 'Bermuda',
                 'Tanzania', 'Brunei Darussalam', 'Bolivia', '"Bonaire, Sint Eustatius And Saba"', 'Brazil', 'Bahamas',
                 'Bhutan', 'Bouvet Island', 'Botswana',
                 'Belize', 'Cocos (Keeling) Islands', 'Congo', 'Cook Islands', 'Chile', 'Cameroon', 'China', 'Colombia',
                 'Costa Rica', 'Cuba', 'Cape Verde',
                 'Curaçao', 'Christmas Island', 'Cyprus', 'Djibouti', 'Denmark', 'Dominica', 'Dominican Republic',
                 'Ecuador', 'Estonia', 'Western Sahara',
                 'Eritrea', 'Spain', 'Ethiopia', 'Finland', 'Germany', 'Belarus', 'Czech Republic', 'Egypt',
                 'Central African Republic',
                 'Democratic Republic Of The Congo', 'Switzerland', 'Algeria', 'Fiji', 'Falkland Islands (Malvinas)',
                 'Federated States of Micronesia',
                 'Faroe Islands', 'France', 'Gabon', 'Grenada', 'Georgia', 'French Guiana', 'Guernsey', 'Ghana',
                 'Gibraltar', 'Greenland', 'Gambia',
                 'Guadeloupe', 'Equatorial Guinea', 'Greece', 'South Georgia And The South Sandwich Islands',
                 'Guatemala', 'Guam', 'Guinea-Bissau',
                 'Guyana', 'Hong Kong', 'Heard Island And McDonald Islands', 'Croatia', 'Haiti', 'Hungary', 'Indonesia',
                 'Ireland', 'Israel', 'Isle Of Man',
                 'British Indian Ocean Territo', 'Iraq', 'Iran', 'Iceland', 'Jersey', 'Jamaica', 'Guinea', 'Honduras',
                 'United Kingdom', 'Jordan', 'Kenya',
                 'Cambodia', 'Kiribati', 'Comoros', 'Saint Kitts And Nevis', 'Liechtenstein', 'Liberia', 'Lesotho',
                 'Lithuania', 'Luxembourg', 'Latvia',
                 'Libya', 'Monaco', 'Moldova', 'Montenegro', 'Saint Martin (French Part)', 'Madagascar',
                 'Marshall Islands', 'Macedonia', 'Mali', 'Myanmar',
                 'Mongolia', 'Macao', 'Northern Mariana Islands', 'Martinique', 'Mauritania', 'Montserrat', 'Malta',
                 'Mauritius', 'Maldives', 'Malawi', 'Mexico',
                 'Mozambique', 'Namibia', 'Malaysia', 'Lebanon', 'Kyrgyzstan', 'Morocco', 'Sri Lanka', 'Japan',
                 'Saint Lucia', 'New Caledonia', 'Niger',
                 'Norfolk Island', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'Niue',
                 'New Zealand', 'Oman', 'Panama', 'Peru',
                 'French Polynesia', 'Papua New Guinea', 'Philippines', 'Pakistan', 'Saint Pierre And Miquelon',
                 'Pitcairn', 'Puerto Rico',
                 'Palestinian Territory', 'Portugal', 'Palau', 'Paraguay', 'Qatar', 'Réunion', 'Rwanda', 'Saudi Arabia',
                 'Solomon Islands', 'Seychelles',
                 'Sudan', 'Sweden', 'Singapore', 'Slovenia', 'Svalbard And Jan Mayen', 'Slovakia', 'Sierra Leone',
                 'Poland', 'Serbia', 'Romania', 'San Marino',
                 'Senegal', 'Somalia', 'South Sudan', 'Sao Tome And Principe', 'El Salvador',
                 'Sint Maarten (Dutch Part)', 'Turks And Caicos Islands',
                 'French Southern Territories', 'Togo', 'Thailand', 'Tokelau', 'Timor-Leste', 'Tunisia', 'Tonga',
                 'Tuvalu', 'Ukraine', 'Uganda',
                 'United States Minor Outlying Islands', 'Uruguay', 'Holy See (Vatican City State)',
                 'Saint Vincent And The Grenadines', 'British Virgin Islands',
                 'U.S. Virgin Islands', 'Vietnam', 'Vanuatu', 'Wallis And Futuna', 'Samoa', 'Yemen', 'Mayotte',
                 'Uzbekistan', 'Turkmenistan', 'Tajikistan',
                 'Venezuela', 'Swaziland', 'Chad', 'Kosovo', 'Turkey', 'Trinidad And Tobago', 'India', 'USSR',
                 'United States', 'Australia']

    data_list = []

    # tempSoup = get_soup(url)

    # hrefs = []
    # MainNames = []
    # table = tempSoup.find("table", class_="wikitable").find_all("tr")[1:]
    # aTags = [i.find_all("td",recursive = False)[1].find("a") for i in table]
    # carrTerms = [i.find_all("td",recursive = False)[2].text+" - "+i.find_all("td",recursive = False)[3].text for i in table]
    # polParty = [i.find_all("td",recursive = False)[5].text.strip() for i in table]
    # # hrefs_MainNames = tempSoup.find("div", class_="mw-parser-output").find_all("ul")[2:]
    # # for ent in hrefs_MainNames:
    # #     aTags = ent.find_all("a")
    # for a in aTags:
    #     hrefs.append("https://en.wikipedia.org" +a["href"])
    #     MainNames.append(a.text)


    from selenium import webdriver
    from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains

    # PATH = "C:\\Users\\91702\\Downloads\\chromedriver_win32\\chromedriver.exe"
    # from pyvirtualdisplay import Display
    # display = Display(visible = 0, size = (1366, 768))
    # display.start()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    hrefs = []
    MainNames = []
    try:
        driver.get("https://en.wikipedia.org/wiki/Cabinet_of_Iceland")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        links = driver.find_elements(By.XPATH, f'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[5]/a')
        links1 = [lnk.get_attribute('href') for lnk in links]
        linksNames1 = [lnk.text for lnk in links]
        hrefs.extend(links1)
        MainNames.extend(linksNames1)

    except:
        pass

    finally:
        try:
            driver.quit()

        except:
            pass


    # print("totalLinks: ", len(hrefs))
    for m, href in enumerate(hrefs):
        data_dict = {}
        familyInfo = ""
        desig = ""
        dob_pob = ""
        dob = ""
        pobCity = ""
        pobCountry = ""
        dod = ""
        category = ""
        name = ""
        image = ""
        education = ""
        nationality = ""
        occupation = ""
        yearsActive = ""
        knownFor = ""
        crimePenality = ""
        charges = ""
        maritalStatus = ""
        politicalParty = ""
        alias = ""
        height = ""
        weight = ""
        position = ""
        offense = ""
        description = ""
        careerInfo = ""
        achievements = ""
        crimeInfo = ""
        crimeDes = ""
        remarks = ""
        terms = ""
        summary = ""
        infoBox = ""
        name = ""
        address = ""
        website = ""
        soup = get_soup(href)
        name

        tempName = re.sub("\(.*?\)", "", MainNames[m])
        # print("tempName: "+tempName)

        b_tag = soup.find_all("b")
        b_tag = [i.text for i in b_tag]
        # print("b_tag: ",b_tag)

        for b in b_tag:
            try:
                if tempName.split(" ")[0] in b or tempName.split(" ")[1] in b:
                    name = b
                    break
            except:
                pass

        if not name:
            name = tempName

        # print("name: "+name)
        # print("****"*50)

        try:
            dom = etree.HTML(str(soup))
            isAlias = dom.xpath('//h1/span')[0].text
            if "None" in isAlias:
                isAlias = ''
            if isAlias and isAlias.split('(')[0].strip() not in name:
                alias = isAlias
        except:
            pass

        try:
            infoBox = soup.find("table", class_="infobox biography vcard")
            if infoBox:
                image = infoBox.find("img")
                if image:
                    image = "https:" + image["src"]

                infoBox = infoBox.find_all("tr")
                infoBox = [i.text for i in infoBox]


        except:
            pass

        if not infoBox:
            try:
                infoBox = soup.find("table", class_="infobox")
                if infoBox:
                    image = infoBox.find("img")
                    if image:
                        image = "https:" + image["src"]

                    temp = infoBox.find("th", class_="infobox-header")
                    try:
                        if temp:
                            temp = temp.text
                            if not re.match(
                                    ".*[Pp][Ee][Rr][Ss][Oo][Nn][Aa][Ll].*|[bB][Aa][Cc][Kk][Gg][Rr][Oo][Uu][Nn][Dd] [Ii][Nn][Ff][Oo][Rr][Mm][Aa][Tt][Ii][Oo][Nn]|.*Names.*",
                                    temp):
                                temp = re.sub("\[.*?\]", "", temp)
                                desig = temp.strip()
                                terms = soup.find("table", class_="infobox vcard").find("td", {
                                    "style": "border-bottom:none"}).text
                                terms = re.sub("[Ii][Nn]\s*[Oo][fF][Ff][Ii][Cc][Ee]|\[.*?\]", "", terms).strip()
                    except:
                        pass
                    infoBox = infoBox.find_all("tr")
                    infoBox = [i.text for i in infoBox]


            except:
                pass

        if not infoBox:
            try:
                infoBox = soup.find("table", class_="infobox vcard")
                if infoBox:
                    image = infoBox.find("img")
                    if image:
                        image = "https:" + image["src"]

                    temp = infoBox.find("th", class_="infobox-header")
                    if temp:
                        try:
                            temp = temp.text
                            if not re.match(".*[Pp][Ee][Rr][Ss][Oo][Nn][Aa][Ll].*|.*Names.*", temp):
                                desig = temp.strip()
                                terms = soup.find("table", class_="infobox vcard").find("td", {
                                    "style": "border-bottom:none"}).text
                                terms = re.sub("[Ii][Nn]\s*[Oo][fF][Ff][Ii][Cc][Ee]|\[.*?\]", "", terms).strip()
                        except:
                            pass
                    infoBox = infoBox.find_all("tr")
                    infoBox = [i.text for i in infoBox]


            except:
                pass

        if not infoBox:
            try:
                infoBox = soup.find("table", class_="infobox vcard plainlist")
                if infoBox:
                    image = infoBox.find("img")
                    if image:
                        image = "https:" + image["src"]

                    infoBox = infoBox.find_all("tr")
                    infoBox = [i.text for i in infoBox]

            except:
                pass

        if str(type(infoBox)) == "<class 'list'>":

            for info in infoBox:
                tempChildren = ""
                tempEducation = ""
                info = re.sub("\[.*?\]", " ", info)
                if re.match("^[Bb]orn", info):
                    dob_pob = info
                    dob = re.findall("\d{1,2}\s{0,1}[A-Z][a-z]+\s{0,1}\d{4}|[A-Z][a-z]+ \d{0,2}, \d{4}", dob_pob)
                    if dob:
                        dob = dob[0]
                    else:
                        dob = dob = re.findall("[A-Z][a-z]+, \d{4}|\d{1,2}/\d{1,2}/\d{4}|\d{4}", dob_pob)
                        if dob:
                            dob = dob[0]

                    dob_pob = re.sub(".*\d{0,2}\s{0,1}[A-Z][a-z]+\s{0,1}\d{4}|.*\d{4}", "", dob_pob)
                    pob = re.sub("[Bb]orn|\(.*?\)|\)|\(", "", dob_pob).strip()
                    pob = pob.split(",")
                    if len(pob) > 1:
                        pobCountry = pob[-1].strip()
                        pobCity = ",".join(pob[:-1]).strip()
                    else:
                        if pob[0].strip() in countries:
                            pobCountry = pob[0].strip()
                        else:
                            pobCity = pob[0].strip()

                elif re.match("^Date of birth", info):
                    dob = re.sub("Date of birth|\(.*?\)", "", info).strip()

                elif re.match("^Place of birth", info):
                    pob = re.sub("Place of birth", "", info).strip()
                elif "Branch" in info or "Allegiance" in info or "Rank" in info or "Battle" in info or "Years of service" in info:
                    if careerInfo:
                        careerInfo+="; "
                    careerInfo+=info

                elif "Reign" in info:
                    terms = info.replace("Reign", '').strip()
                    # print("terms: ",terms)
                elif "Predecessor" in info:
                    predecessor = re.sub("[pP]redecessor|position established|\(.*?\)|^.*?\)|\(.*?$|\n", "",
                                         info).strip()
                    # print(predecessor)
                    if predecessor:
                        careerInfo += "; Preceded By: " + predecessor
                elif "Heir " in info or "Successor" in info:
                    successor = re.sub("Heir presumptive|Successor|position established|\(.*?\)|^.*?\)|\(.*?$|\n", "",
                                       info).strip()
                    if successor:
                        careerInfo += "; Succeeded By: " + successor

                elif re.match("^Height|^Listed height", info):
                    height = re.sub("Height|\(.*?\)|Listed height", "", info).strip()

                elif re.match("^Weight|^Listed weight", info):
                    try:
                        weight = re.sub("Weight|Listed weight", "", info).strip()
                        weight = re.findall("\d{2,3}", weight)[-1] + " lbs"
                    except:
                        pass


                elif re.match("^Position", info):
                    position = re.sub("Position|(s)", "", info).strip()
                elif re.match("^[Dd]ied", info):
                    dod = re.findall("\d{0,2}\s{0,1}[A-Z][a-z]+\s{0,1}\d{4}|[A-Z][a-z]+ \d{0,2}, \d{4}|\d{4}", info)
                    if dod:
                        dod = dod[0].replace("Died", "").strip()

                elif re.match("^[Nn]ationality", info):
                    nationality = re.sub("[Nn]ationality", "", info).strip()
                elif re.match("^[Aa]lma|^[Ee][Dd][Uu][Cc][Aa][Tt][Ii][Oo][nN]", info):
                    education = re.sub("[aA]lma.*?mater|[Ee][Dd][Uu][Cc][Aa][Tt][Ii][Oo][nN]", "", info).strip()
                    education = re.sub("\n|(?<=\))(?=U)", "; ", education)
                    education = re.sub("(?<=[a-z])(?=[A-Z])",", ",education).strip()

                elif re.match("^College", info):
                    education += ";" + re.sub("College", "", info).strip()
                elif re.match("^High school", info):
                    education += ";" + re.sub("High school", "", info).strip()
                    # if re.match(".*[A-Z][a-z]+[A-Z][a-z]+.*", education):
                    #     tempEducation = re.findall("[A-Z][a-z]+(?: [A-Za-z]+ )*\s*[A-Z][a-z]+", education)
                    #     if tempEducation:
                    #         education = "; ".join(tempEducation)
                elif re.match("^[oO]ccupation", info):
                    desig += ";" + re.sub("[oO]ccupation[\(s\)]{0,3}", "", info).strip()
                elif re.match("^Profession", info):
                    desig +=";" + re.sub("Profession", "", info).strip()
                elif re.match("^Website", info):
                    website = re.sub("Website", "", info).strip()
                    if "." not in website:
                        website = ""
                elif re.match("^[Yy]ears.*?active", info):
                    yearsActive = re.sub("[Yy]ears.*active", "", info).strip()
                elif re.match("^[Kk]nown.*?for", info):
                    knownFor = re.sub("[Kk]nown.*?for", "", info).strip()
                elif re.match("^[Cc]riminal.*?penalty", info):
                    crimePenality = re.sub("[Cc]riminal.*?penalty", "", info).strip()
                elif re.match("^Residence", info):
                    address = re.sub("Residence", "", info).replace("\n", ', ').strip(';|,|" "')
                elif re.match("^Also known as", info):
                    alias += ";" + re.sub("Also known as", "", info).strip()
                elif re.match("^Birth name", info):
                    alias += ";" + re.sub("Birth name", "", info).strip()
                elif re.match("^[Ss]pouse", info):
                    maritalStatus = "Married"
                    spouse = re.sub("[sS]pouse[(sS)]{0,3}", "", info).strip()
                    if spouse and "See list" not in spouse:
                        if familyInfo:
                            familyInfo += "; Spouse Name: " + spouse
                        else:
                            familyInfo = "Spouse Name: " + spouse
                elif re.match("^[rR]elations",info):
                    relations = re.sub("Relations", "", info).strip()
                    if familyInfo:
                        familyInfo += "; Relations: " + relations
                    else:
                        familyInfo = "Relations: " + relations

                elif re.match("^[fF]ather", info):
                    father = re.sub("[Ff]ather", "", info).strip()
                    if father:
                        if familyInfo:
                            familyInfo += "; Father: " + father
                        else:
                            familyInfo = "Father: " + father

                elif re.match("^[Mm]other", info):
                    mother = re.sub("[Mm]other", "", info)
                    if mother:
                        if familyInfo:
                            familyInfo += "; Mother: " + mother
                        else:
                            familyInfo = "Mother: " + mother

                elif re.match("^[hH]ouse", info):
                    dynasty = re.sub("[hH]ouse", "", info)
                    if dynasty:
                        if familyInfo:
                            familyInfo += "; Dynasty: " + dynasty
                        else:
                            familyInfo = "Dynasty: " + dynasty

                elif re.match("[Ii]ssue", info):
                    issue = re.sub("[Ii]ssue", "", info)
                    issue = re.sub("(?<=[a-z\)])(?=[A-Z][a-z]+)", ", ", issue).strip(" ,")
                    issue = re.sub(",\s+,", ",", issue).strip(" ,")
                    if issue and "See list" not in issue:
                        if familyInfo:
                            familyInfo += "; Children: " + issue
                        else:
                            familyInfo = "Children: " + issue

                elif re.match("^[cC]hildren", info):
                    children = re.sub("[cC]hildren", "", info).strip()
                    if re.match(".*[A-Z][a-z]+[A-Z][a-z]+.*", children):
                        tempChildren = re.findall("[A-Z][a-z]+ (?:[a-z]+ )*[A-Z][a-z]+", children)
                    if tempChildren:
                        children = ", ".join(tempChildren)
                    if children:
                        if familyInfo:
                            familyInfo += "; Children: " + children
                        else:
                            familyInfo = "Children: " + children
                elif re.match("^[Pp]olitical party", info):
                    politicalParty = re.sub("[Pp]olitical party", "", info).strip()
                    politicalParty = re.sub("\)", "); ", politicalParty).strip("; ")
                    category = "PEP"
                elif re.match("^[oO]ther.*names", info):
                    alias = re.sub("[oO]ther.*?names", "", info)
                elif re.match(".*[Cc][Oo][Nn][Vv][Ii][Cc][Tt][Ii][Oo][Nn].*", info):
                    offense = re.sub("[Cc][Oo][Nn][Vv][Ii][Cc][Tt][Ii][Oo][Nn]|\(s\)", "", info).strip()
                elif re.match(".*Criminal charge(s).*", info):
                    charges = re.sub(".*Criminal charge(s).*", "", info)
                elif re.match("^Other political.*affiliations", info):
                    politicalAffilation = re.sub("[oO]ther|[Pp]olitical|[Aa]ffiliations|\n", "", info).strip()
                    category = "PEP"
                elif re.match("^Parent[\(sS\)]*", info):
                    parents = re.sub("Parent[\(sS\)]*", "", info)
                    if familyInfo:
                        familyInfo += "; Parents: " + parents
                    else:
                        familyInfo = "Parents: " + parents
                else:
                    # print(info)
                    pass

        details = soup.find("div", class_="mw-parser-output").find_all(["p", "h2", "li", "h3", "h4"])

        for tag in details:
            if "<p>" in str(tag):
                tempSummary = re.sub("\(.*?\(-\).*?\)|\(.*?\)|\[.*?\]|\n", "", tag.text)
                # print(tempSummary)
                if len(summary) < 300:

                    if summary:
                        summary += " " + re.sub("\s{2,}", " ", tempSummary)
                    else:
                        summary = re.sub("\s{2,}", " ", tempSummary)
                else:
                    description += " " + tempSummary
            elif "<h2" in str(tag):
                # print("break at h2")
                break

            # print("summary Len: ",len(summary))

        t = 0
        while t < len(details) - 1:

            if '<h2' in str(details[t]) or "<h3" in str(details[t]) or "<h4" in str(details[t]):
                if "<h3" in str(details[t + 1]) or "<h4" in str(details[t + 1]):
                    head = details[t + 1].text.strip()
                    head = re.sub("[Ee][Dd][Ii][Tt]", "", head).strip()
                    t += 2
                else:
                    head = details[t].text.strip()
                    head = re.sub("[Ee][Dd][Ii][Tt]", "", head).strip()
                    t += 1
                data = ""

                while True and t < len(details):
                    if "<li" in str(details[t]):
                        text = details[t].text.strip()
                        if "^" not in text:
                            if re.match("(?=.*[gG]raduated [Ff]rom)|(?=.*[dD]ropped [Oo]ut)", text):
                                if "taught" not in text.lower():
                                    if education:
                                        education += " " + text.strip(". ") + "."
                                    else:
                                        education = text.strip(". ") + "."
                                else:
                                    if data:
                                        data += ". " + text
                                    else:
                                        data = text
                            elif re.match(
                                    "(?=.*[eE]xecutive of)|(?=.*[gG]eneral of)|(?=.*[lL]eader of)|(?=.*[rR]esearcher at)|(?=.*[Cc]hairman of)|(?=.*[pP]resident of)|(?=.*[Mm]ember of )|(?=.*[Ee]lected)|(?=.*[Jj]oined)|(?=.*[Cc]ontested)",
                                    text):
                                if careerInfo:
                                    careerInfo += "; " + text.strip()
                                else:
                                    careerInfo = text.strip()
                            elif re.match("(?=.*[cC]onvicted)|(?=.*[tT]rial)|(?=.*[aA]rrested)",
                                    text):
                                # print(text.strip())
                                if crimeInfo:
                                    crimeInfo += "; " + text.strip()
                                else:
                                    crimeInfo = text.strip()

                    else:
                        if "You can help Wikipedia by expanding it" in details[t].text.strip() or "ReferencesEdit" in \
                                details[t].text.strip():
                            break
                        if not re.match(".*[a-z]Edit.*|.*Last Update.*", details[t].text.strip()):
                            data += ' ' + details[t].text.strip()

                    t += 1
                    if t >= len(details) or '<h2' in str(details[t]) or "<h3" in str(
                            details[t]) or "<h4" in str(details[t]):
                        break
                data = re.sub("\[.*?\]|\(.*?\)", "", data).strip()
                data = re.sub("\n", " ", data)

                if re.match(".*[a-z]Edit.*", data.strip()):
                    data = ""
                if re.match(
                        ".*Childhood.*|.*[lL]ife.*|.*[bB][Aa][Cc][Kk][Gg][Rr][Oo][Uu][Nn][Dd].*|.*[bB][Ii][Oo][Gg][Rr][Aa][Pp][hH][Yy].*|.*[Bb]iography.*",
                        head):
                    tempData = re.split("(?<=[a-z\d\)])\. (?=[A-Z])", data)
                    data = ""
                    for tex in tempData:

                        if re.match(
                                ".*[Gg]raduated.*|.*[Bb]achelor's [Dd]egree.*|.*High School.*|.*[Dd]octoral [Dd]egrees.*|.*[eE]lementary [sS]chool.*|(?=.*bachelor's)(?=.*University)|.*where he studied.*|.*Ph.D.*|(?=.*[mM]aster)(?=.*[dD]egree)",
                                tex):
                            if "taught" not in tex.lower():
                                if education:
                                    education += " " + tex.strip(". ") + "."
                                else:
                                    education = tex.strip(". ") + "."
                            else:
                                if data:
                                    data += ". " + tex
                                else:
                                    data = tex
                        else:
                            if data:
                                data += ". " + tex
                            else:
                                data = tex
                    if description:
                        description += " " + data
                    else:
                        description = data
                elif re.match(
                        ".*political involvement.*|.*[Cc][aA][rR][eE][Ee][rR].*|.*Lyngby.*|.*North America.*|.*[fF]irst [Rr]oles.*|.*[mM]ilitary [Ss]ervice.*|.*[cC]abinet [Mm]inister.*|.*Presidency \(.*|.*[aA]ssembly\s*[Ww]oman.*|.*[hH]ead of.*|.*[aA]ppointment.*|.* [Ww][Oo][Rr][Kk].*|.*[Gg]overner.*|.*[Bb]uisness.*",
                        head):
                    tempData = re.split("(?<=[a-z\d\)])\. (?=[A-Z])", data)
                    data = ""
                    for tex in tempData:
                        if re.match(
                                ".*[dD]istrict [cC]ourt [Ss]entenced.*|.*immediately jailed.*|.*was imprisoned.*|.*wrongdoing.*",
                                tex):
                            if crimeInfo:
                                crimeInfo += "; " + tex + "."
                            else:
                                crimeInfo = tex + "."
                        elif re.match(
                                ".*[Gg]raduated.*|.*[Bb]achelor's [Dd]egree.*|.*[Dd]octoral [Dd]egrees.*|(?=.*bachelor's)(?=.*University)|.*University.*|.*Ph.D.*|(?=.*[mM]aster)(?=.*[dD]egree)",
                                tex):

                            if "taught" not in tex.lower():
                                if education:
                                    education += " " + tex.strip(". ") + "."
                                else:
                                    education = tex.strip(". ") + "."
                            else:
                                if data:
                                    data += ". " + tex
                                else:
                                    data = tex
                        else:
                            if data:
                                data += ". " + tex
                            else:
                                data = tex
                    if careerInfo:
                        careerInfo += '; ' + data
                    else:
                        careerInfo = data
                elif re.match(".*[Pp][Ee][Rr][Ss][oO][nN][aA][lL] [Ll][iI][fF][Ee].*", head):
                    if description:
                        description += "; " + data
                    else:
                        description = data
                #         elif re.match(".*[aA][wW][aA][Rr][Dd].*", head):
                #             achievements = data
                elif re.match(".*[bB][iI][Cc][Hh][Ee][Ii][Rr][Oo].*", head):
                    if crimeInfo:
                        crimeInfo += '; ' + data
                    else:
                        crimeInfo = data
                elif re.match(
                        ".*[fF][Ii][Xx][Ii][Nn][Gg].*|.*[Cc][Oo][Nn][Vv][Ii][Cc][Tt][Ii][Oo][Nn].*|.*[Ss]exual [Aa]ssault.*",
                        head):
                    if crimeDes:
                        crimeDes += "; " + data
                    else:
                        crimeDes = data
                elif re.match(
                        ".*[Aa][rR][Rr][Ee][Ss][tT].*|.*[cC][Oo][Rr][Rr][Uu][Pp][Tt][Ii][Oo][Nn].*|.*Illicit business activities.*",
                        head):
                    if crimeDes:
                        crimeDes += "; " + data
                    else:
                        crimeDes = data
                elif desig in head and desig.strip():
                    if careerInfo:
                        careerInfo += '; ' + data
                    else:
                        careerInfo = data
                elif re.match(
                        ".*[pP][Rr][Oo][Ss][Ee][Cc][Uu][Tt][Ii][Oo][Nn].*|.*[tT][Rr][Ii][aA][Ll].*|.*[pP]rison [Ss]entence.*|.*[Cc]riticism.*|.*[Aa]ccusations.*|.*[dD]etention.*|.*[Cc]ontroversies.*",
                        head):
                    if remarks:
                        remarks += "; " + head + ": " + data
                    else:
                        remarks = head + ": " + data
                elif re.match(".* [eE]ducation.*|^Education", head):

                    tempData = re.split("(?<=[a-z\d\)])\. (?=[A-Z])", data)
                    data = ""
                    for tex in tempData:
                        if re.match(
                                "(?=.*[eE]xecutive of)|(?=.*[gG]eneral of)|(?=.*[lL]eader of)|(?=.*[rR]esearcher at)|(?=.*[Cc]hairman of)|(?=.*[pP]resident of)|(?=.*[Mm]ember of )|.*[Ee]xecutive [Mm]ember.*|.*[SshHEe]{2,3} became.*|.*the Central Committee.*!.(?=.*[Gg]overnor) ",
                                tex):
                            if careerInfo:
                                careerInfo += "; " + tex.strip()
                            else:
                                careerInfo = tex.strip()
                        else:
                            if data:
                                data += ". " + tex
                            else:
                                data = tex
                    if education:
                        education += "; " + data
                    else:
                        education = data


            else:
                t += 1

        # terms = carrTerms[m]
        # politicalParty = polParty[m]
        name = re.sub("\(.*?\)", "", name).strip()

        if name and name != "[2]":
            if "Sultan bin Muhammad Al Qasimi" in name:
                data_dict["alias"] = "Sultan bin Muhammad bin Al-Qasimi"
            if "Justice" in name:
                data_dict['prefix'] = "Justice"
                name = name.replace("Justice", '').strip()
            data_dict["fullName"] = name.replace("/", '').replace('"', '').replace('\u00ed','i').replace('\u00f3','o').replace('\u00f0','o').replace('\u00de','P').replace('\u00fa','u').replace('\u00f6','o').replace('\u00c1','A').strip()
            if image:
                if "flag" not in image.lower():
                    data_dict["image"] = image
            if desig:
                desig = re.sub("\[.*?\]|:.*?\d+", "", desig).strip()
                data_dict["careerInfoRoles"] = desig.strip(";")
            if terms:
                if re.match("[iI]ncumbent", terms):
                    terms = ""
                else:
                    terms = re.sub("\u00a0|\(.*?\)", "", terms).strip()
                    terms = re.sub("\u2013", "-", terms).strip()
                    data_dict["careerInfoTerms"] = terms
            if dob:
                data_dict["dob"] = dob
            if "Winter's Rush" in pobCity:
                pobCity = ""
            if pobCity:
                tempPobCity = pobCity.split(",")
                pobCity = ""
                for i in tempPobCity:
                    if i.strip() in countries:
                        pobCountry = i.strip()
                    else:
                        if pobCity:
                            pobCity += ", " + i.strip()
                        else:
                            pobCity = i.strip()
                if "England" in pobCity:
                    pobCity = re.sub("England", "", pobCity).strip(" ,")

                data_dict["placeOfBirthCity"] = pobCity.replace(",", "").replace(name, '')
            if "trucial states" in pobCountry.lower():
                pobCountry = "United Arab Emirates"
            elif "UAE" in pobCountry:
                pobCountry = "United Arab Emirates"
            elif "Transvaal" in pobCountry or "Kimberley" in pobCountry or "Johannesburg" in pobCountry:
                pobCountry = "South Africa"
            elif "Cape Colony" in pobCountry or "Northern Cape" in pobCountry or "North West" in pobCountry:
                pobCountry = "South Africa"
            elif "russia" in pobCountry.lower():
                pobCountry = "Russia"
            if pobCountry:
                pobCountry = re.sub("Union of", "", pobCountry).strip()
                if "british nigeria" in pobCountry:
                    pobCountry = "Nigeria"
                if pobCountry in countries:
                    data_dict["placeOfBirthCountry"] = pobCountry
                else:
                    if data_dict.get('placeOfBirthCity') != None:
                        data_dict['placeOfBirthCity'] += " " + pobCountry
                    else:
                        data_dict['placeOfBirthCity'] = pobCountry
            if dod:
                data_dict["deceased"] = True
                data_dict["importantDates"] = "Date of Death: " + dod
            if weight:
                data_dict['weight'] = weight
            if familyInfo:
                familyInfo = re.sub("\[.*?\]", "", familyInfo).strip()
                familyInfo = re.sub("\u200b \u200b\u200b", "", familyInfo).strip()
                familyInfo = re.sub("\u200b", "", familyInfo).strip()
                familyInfo = re.sub("\n", ", ", familyInfo).strip()
                data_dict["familyInfo"] = familyInfo
            if education.strip(';|" "') and len(education) > 6:
                data_dict["educationInfo"] = education.strip(';|" "')
            if address:
                data_dict['fullAddress'] = address
            if height:
                data_dict["height"] = height.replace('\u00a0','').strip()
            if nationality:
                if "Emirati" in nationality:
                    nationality = "United Arab Emirates"
                if "African" in nationality:
                    nationality = "South Africa"
                data_dict["nationality"] = nationality

            if summary:
                summary = re.sub("\[.*?\]|:.*?\d+", "", summary).strip()
                data_dict["summary"] = summary.replace("//", '').replace('\u00e8','').replace('\u00a3','').replace('\u2013','')
            if charges:
                data_dict["charges"] = charges
            if yearsActive:
                data_dict["additionalInfo"] = "Years Active: " + yearsActive.replace('\u00a0','').replace('\u2013','').strip()
            if knownFor:
                if yearsActive:
                    data_dict["additionalInfo"] += "; Known For: " + knownFor.replace('\u00a0','').replace('\u2013','').strip()
                else:
                    data_dict["additionalInfo"] = "Known For: " + knownFor.replace('\u00a0','').replace('\u2013','').strip()
            # if occupation:
            #     data_dict['careerInfoRoles'] = occupation
            if maritalStatus:
                data_dict["maritalStatus"] = maritalStatus
            if website:
                data_dict['website'] = website.replace(",", ';').strip(';|" "')
            if politicalParty:
                data_dict["politicalPartyName"] = politicalParty
            if alias:
                alias = re.sub("\(.*?\)|\n|Mo", "", alias).strip()
                data_dict["alias"] = alias
            if category:
                data_dict["category"] = category
            if offense:
                data_dict["offense"] = offense
            if description:
                data_dict["description"] = description.replace('\u2013','')
            if careerInfo:
                data_dict["careerInfo"] = careerInfo.replace('\u2013','').strip("; ")
            if achievements:
                data_dict['achievements'] = achievements
            if crimeInfo:
                crimeInfo = re.sub("\[.*?\]|:.*?\d+", "", crimeInfo).strip()
                data_dict["crimeInfo"] = crimeInfo
            if crimeDes:
                crimeDes = re.sub("\[.*?\]|:.*?\d+", "", crimeDes).strip()
                data_dict["crimeDescription"] = crimeDes
            # if remarks:
            #     data_dict["remarks"] = remarks
            if "Hope" in data_dict["fullName"]:
                data_dict["constituency"] = "Imo (West)"
            if "Ali Modu Sheriff" in data_dict["fullName"]:
                data_dict["placeOfBirthCity"] = "Ngala Town, Ngala LGA"

            data_list.append(data_dict)

    driver.quit()
    # display.stop()
    return data_list


def to_json(data):
    import json
    with open("extracted.json", "w") as outfile:
        json.dump(data, outfile, indent=4)
        outfile.close()


if __name__ == "__main__":
    data_list = get_data('slug_name')
    # print(data_list)
    to_json(get_data())

    
    
