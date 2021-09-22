import requests
from bs4 import BeautifulSoup
import xlsxwriter
from tqdm import tqdm


def themeteams(in_url, in_team):

    URL = in_url
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("div", class_="player-list-item")
    position_list = []
    name_list = []
    ovr_list = []
    program_list = []
    xbox_price_list = []
    play_price_list = []
    pc_price_list = []
    for job_element in job_elements:
        first_name = job_element.find("div", class_="player-list-item__name-first")
        last_name = job_element.find("div", class_="player-list-item__name-last")
        ovr = job_element.find("div", class_="player-list-item__score-value")
        position = job_element.find("div", class_="player-list-item__archetype")
        program = job_element.find("div", class_="player-list-item__program")
        name_list.append(str(first_name.text.strip()) + ' ' + str(last_name.text.strip()))
        ovr_list.append(str(ovr.text.strip()))
        position_list.append(str(position.text.strip()).split(" ",1)[0])
        program_list.append(str(program.text.strip()))
        link ='https://www.muthead.com/22/players/' + str(job_element.find('a', href=True)['href'])[-9:]
        page1 = requests.get(link)
        if page1.status_code == 200:
            soup1 = BeautifulSoup(page1.content, "html.parser")
            price_elements = soup1.find_all('span', class_='mut-player-price__price')
            xbox_price_list.append(str(price_elements[0].text.strip()))
            play_price_list.append(str(price_elements[1].text.strip()))
            pc_price_list.append(str(price_elements[2].text.strip()))
            
        else:
            xbox_price_list.append("-")
            play_price_list.append("-")
            pc_price_list.append("-")
            
        
        
    workbook = xlsxwriter.Workbook('ThemeTeams/' + in_team + '.xlsx')
    worksheet = workbook.add_worksheet()
    
    worksheet.write(0, 0, "Position")
    worksheet.write(0, 1, "Name")
    worksheet.write(0, 2, "OVR")
    worksheet.write(0, 3, "Program")
    worksheet.write(0, 4, "Price - Xbox")
    worksheet.write(0, 5, "Price - PlayStation")
    worksheet.write(0, 6, "Price - PC")
    
    
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 1
    column = 0
    
    
    # iterating through content list
    for item in position_list :
     
        # write operation perform
        worksheet.write(row, column, item)
        
        # incrementing the value of row by one
        # with each iterations.
        row += 1
    
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 1
    column = 1
    
    
    # iterating through content list
    for item in name_list :
     
        # write operation perform
        worksheet.write(row, column, item)
        
        # incrementing the value of row by one
        # with each iterations.
        row += 1
    
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 1
    column = 2
    
    
    # iterating through content list
    for item in ovr_list :
     
        # write operation perform
        worksheet.write(row, column, item)
        
        # incrementing the value of row by one
        # with each iterations.
        row += 1
    
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 1
    column = 3
    
    
    # iterating through content list
    for item in program_list :
     
        # write operation perform
        worksheet.write(row, column, item)
        
        # incrementing the value of row by one
        # with each iterations.
        row += 1
    
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 1
    column = 4
    
    
    # iterating through content list
    for item in xbox_price_list:
     
        # write operation perform
        worksheet.write(row, column, item)
        
        # incrementing the value of row by one
        # with each iterations.
        row += 1
        
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 1
    column = 5
    
    
    # iterating through content list
    for item in play_price_list:
     
        # write operation perform
        worksheet.write(row, column, item)
        
        # incrementing the value of row by one
        # with each iterations.
        row += 1
        
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 1
    column = 6
    
    
    # iterating through content list
    for item in pc_price_list:
     
        # write operation perform
        worksheet.write(row, column, item)
        
        # incrementing the value of row by one
        # with each iterations.
        row += 1
    
    workbook.close()
    
url_list = [
    'https://www.mut.gg/theme-teams/16/san-francisco-49ers/',
    'https://www.mut.gg/theme-teams/2/chicago-bears/',
    'https://www.mut.gg/theme-teams/3/cincinnati-bengals/',
    'https://www.mut.gg/theme-teams/4/buffalo-bills/',
    'https://www.mut.gg/theme-teams/5/denver-broncos/',  
    'https://www.mut.gg/theme-teams/6/cleveland-browns/',
    'https://www.mut.gg/theme-teams/7/tampa-bay-buccaneers/',
    'https://www.mut.gg/theme-teams/8/arizona-cardinals/',
    'https://www.mut.gg/theme-teams/9/los-angeles-chargers/',
    'https://www.mut.gg/theme-teams/10/kansas-city-chiefs/',
    'https://www.mut.gg/theme-teams/11/indianapolis-colts/',
    'https://www.mut.gg/theme-teams/12/dallas-cowboys/',
    'https://www.mut.gg/theme-teams/13/miami-dolphins/',
    'https://www.mut.gg/theme-teams/14/philadelphia-eagles/',
    'https://www.mut.gg/theme-teams/15/atlanta-falcons/',
    'https://www.mut.gg/theme-teams/27/washington-football-team/',
    'https://www.mut.gg/theme-teams/17/new-york-giants/',
    'https://www.mut.gg/theme-teams/18/jacksonville-jaguars/',
    'https://www.mut.gg/theme-teams/19/new-york-jets/',
    'https://www.mut.gg/theme-teams/20/detroit-lions/',
    'https://www.mut.gg/theme-teams/21/green-bay-packers/',
    'https://www.mut.gg/theme-teams/22/carolina-panthers/',
    'https://www.mut.gg/theme-teams/23/new-england-patriots/',
    'https://www.mut.gg/theme-teams/24/las-vegas-raiders/',
    'https://www.mut.gg/theme-teams/25/los-angeles-rams/',
    'https://www.mut.gg/theme-teams/26/baltimore-ravens/',
    'https://www.mut.gg/theme-teams/28/new-orleans-saints/',
    'https://www.mut.gg/theme-teams/29/seattle-seahawks/',
    'https://www.mut.gg/theme-teams/30/pittsburgh-steelers/',
    'https://www.mut.gg/theme-teams/33/houston-texans/',
    'https://www.mut.gg/theme-teams/31/tennessee-titans/',
    'https://www.mut.gg/theme-teams/32/minnesota-vikings/'
    ]


print("                                                                                                  ")
print(" _____ ___ ___    _____ _                    _____                  _____             _           ")
print("|     |_  |_  |  |_   _| |_ ___ _____ ___   |_   _|___ ___ _____   |_   _|___ ___ ___| |_ ___ ___ ")
print("| | | |  _|  _|    | | |   | -_|     | -_|    | | | -_| .'|     |    | | |  _| .'|  _| '_| -_|  _|")
print("|_|_|_|___|___|    |_| |_|_|___|_|_|_|___|    |_| |___|__,|_|_|_|    |_| |_| |__,|___|_,_|___|_|  ")
print("                                                                                                  ")
print("by Santiago Ariza - September 2021")

for x in tqdm(range(len(url_list)), desc="Loading..."):
    themeteams(url_list[x], url_list[x].split('/')[5])
