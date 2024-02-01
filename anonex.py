from xeger import Xeger
import sys
import re
import random
from datetime import datetime,timedelta
import configparser

config = configparser.ConfigParser()
config.read('anonex.conf')


man = """
┌────────────────┐
│   anonex man   │
└────────────────┘
│
├─ special syntax outex :
│
│  ~ln  : last name
│  ~fn  : first name
│  ~ddb : date (db)
│  ~da : date (classic americain)
│  ~de : date (classic european)
│
├─ outex hint :
│
│  use group for 'repetition' :
│  r'([0-9])-\\1' -> 7-7, 2-2....
│       |_____|
"""
if '--help' in sys.argv or '-h' in sys.argv:
    print(man)
    sys.exit()

#### dictionnary
last_name  = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores","Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts","Gomez","Phillips","Evans","Turner","Diaz","Parker","Cruz","Edwards","Collins","Reyes","Stewart","Morris","Morales","Murphy","Cook","Rogers","Gutierre","Ortiz","Morgan","Cooper","Peterson","Bailey","Reed","Kelly","Howard","Ramos","Kim","Cox","Ward","Richards","Watson","Brooks","Chavez","Wood","James","Bennett","Gray","Mendoza","Ruiz","Hughes","Price","Alvarez","Castillo","Sanders","Patel","Myers","Long","Ross","Foster","Jimenez","Powell","Jenkins","Perry","Russell","Sullivan","Bell","Coleman","Butler","Henderso","Barnes","Gonzales","Fisher","Vasquez","Simmons","Romero","Jordan","Patterso","Alexande","Hamilton","Graham","Reynolds","Griffin","Wallace","Moreno","West","Cole","Hayes","Bryant","Herrera","Gibson","Ellis","Tran","Medina","Aguilar","Stevens","Murray","Ford","Castro","Marshall","Owens","Harrison","Fernande","McDonald","Woods","Washingt","Kennedy","Wells","Vargas","Henry","Chen","Freeman","Webb","Tucker","Guzman","Burns","Crawford","Olson","Simpson","Porter","Hunter","Gordon","Mendez","Silva","Shaw","Snyder","Mason","Dixon","Munoz","Hunt","Hicks","Holmes","Palmer","Wagner","Black","Robertson","Boyd","Rose","Stone","Salazar","Fox","Warren","Mills","Meyer","Rice","Schmidt","Garza","Daniels","Ferguson","Nichols","Stephens","Soto","Weaver","Ryan","Gardner","Payne","Grant","Dunn","Keller","Spencer","Hawkins"]
first_name = ["Jacob","Emily","Michael","Madison","Joshua","Emma","Matthew","Olivia","Daniel","Hannah","Christopher","Abigail","Andrew","Isabella","Ethan","Samantha","Joseph","Elizabeth","William","Ashley","Anthony","Alexis","David","Sarah","Alexander","Sophia","Nicholas","Alyssa","Ryan","Grace","Tyler","Ava","James","Taylor","John","Brianna","Jonathan","Lauren","Noah","Chloe","Brandon","Natalie","Christian","Kayla","Dylan","Jessica","Samuel","Anna","Benjamin","Victoria","Nathan","Mia","Zachary","Hailey","Logan","Sydney","Justin","Jasmine","Gabriel","Julia","Jose","Morgan","Austin","Destiny","Kevin","Rachel","Elijah","Ella","Caleb","Kaitlyn","Robert","Megan","Thomas","Katherine","Jordan","Savannah","Cameron","Jennifer","Jack","Alexandra","Hunter","Allison","Jackson","Haley","Angel","Maria","Isaiah","Kaylee","Evan","Lily","Isaac","Makayla","Luke","Brooke","Mason","Nicole","Jayden","Mackenzie","Jason","Addison","Gavin","Stephanie","Aaron","Lillian","Connor","Andrea","Aiden","Faith","Aidan","Zoe","Kyle","Kimberly","Juan","Madeline","Charles","Alexa","Luis","Katelyn","Adam","Gabriella","Lucas","Gabrielle","Brian","Trinity","Eric","Amanda","Adrian","Kylie","Nathaniel","Mary","Sean","Paige","Alex","Riley","Carlos","Leah","Bryan","Jenna","Ian","Sara","Owen","Rebecca","Jesus","Michelle","Landon","Sofia","Julian","Vanessa","Chase","Jordan","Cole","Angelina","Diego","Caroline","Jeremiah","Avery","Steven","Audrey","Sebastian","Evelyn","Xavier","Maya","Timothy","Claire","Carter","Autumn","Wyatt","Jocelyn","Brayden","Ariana","Blake","Nevaeh","Hayden","Arianna","Devin","Jada","Cody","Bailey","Richard","Brooklyn","Seth","Aaliyah","Dominic","Amber","Jaden","Isabel","Antonio","Mariah","Miguel","Danielle","Liam","Melanie","Patrick","Sierra","Carson","Erin","Jesse","Amelia","Tristan","Molly","Alejandro","Isabelle","Henry","Melissa","Victor","Madelyn","Trevor","Jacqueline","Bryce","Marissa","Jake","Angela","Riley","Shelby","Colin","Leslie","Jared","Katie","Jeremy","Jade","Mark","Catherine","Caden","Diana","Garrett","Aubrey","Parker","Mya","Marcus","Amy","Vincent","Briana","Kaleb","Sophie","Kaden","Gabriela","Brady","Breanna","Colton","Gianna","Kenneth","Kennedy","Joel","Gracie","Oscar","Peyton","Josiah","Adriana","Jorge","Christina","Ashton","Courtney","Cooper","Daniela","Tanner","Lydia","Eduardo","Kathryn","Paul","Valeria","Edward","Layla","Ivan","Alexandria","Preston","Natalia","Maxwell","Angel","Alan","Laura","Levi","Charlotte","Stephen","Margaret","Grant","Cheyenne","Nicolas","Naomi","Dakota","Miranda","Omar","Mikayla","Alexis","Kelsey","George","Payton","Eli","Ana","Collin","Alicia","Spencer","Jillian","Gage","Daisy","Max","Mckenzie","Ricardo","Ashlyn","Cristian","Sabrina","Derek","Caitlin","Micah","Summer","Brody","Ruby","Francisco","Valerie","Nolan","Rylee","Ayden","Skylar","Dalton","Lindsey","Shane","Kelly","Peter","Genesis","Damian","Zoey","Jeffrey","Eva","Brendan","Sadie","Travis","Alexia","Fernando","Cassidy","Peyton","Kylee","Conner","Kendall","Andres","Jordyn","Javier","Kate","Giovanni","Jayla","Shawn","Karen","Braden","Tiffany","Jonah","Cassandra","Bradley","Juliana","Cesar","Reagan","Emmanuel","Caitlyn","Manuel","Giselle","Edgar","Serenity","Mario","Alondra","Erik","Lucy","Edwin","Bianca","Johnathan","Kiara","Devon","Crystal","Erick","Erica","Wesley","Angelica","Oliver","Hope","Trenton","Chelsea","Hector","Alana","Malachi","Liliana","Jalen","Brittany","Raymond","Camila","Gregory","Makenzie","Abraham","Lilly","Elias","Veronica","Leonardo","Abby","Sergio","Jazmin","Donovan","Adrianna","Colby","Delaney","Marco","Karina","Bryson","Ellie","Martin","Jasmin"]
####


with open(config.get('DEFAULT', 'file'),'r') as file:
    raw = file.read()
clean = raw

matches = re.findall(config.get('DEFAULT', 'inex'), raw)

if len(matches) == 0:
    print("Oops, nothing match to your input regex (inex)")


xeger = Xeger(limit=10**6)
for match in matches:
    x = xeger.xeger(config.get('DEFAULT', 'outex'))
    clean = clean.replace(match,x)

    clean = clean.replace('~ln',last_name[random.randint(0, len(last_name))].lower())
    clean = clean.replace('~fn',first_name[random.randint(0, len(first_name))].lower())

    epoch = datetime(1970, 1, 1)
    random_date = epoch + timedelta(seconds=random.randint(0, int((datetime.now() - epoch).total_seconds())))

    clean = clean.replace('~ddb',random_date.strftime("%Y-%m-%d %H:%M:%S"))
    clean = clean.replace('~da',random_date.strftime("%m/%d/%Y"))
    clean = clean.replace('~de',random_date.strftime("%d/%m/%Y"))

print(clean)

