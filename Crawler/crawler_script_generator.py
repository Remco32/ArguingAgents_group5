#Generates commands for scraping

###Debatabase
URLs = ['https://idebate.org/debatabase/culture-media/should-airbrushing-womens-bodies-be-banned',
        'https://idebate.org/debatabase/education/house-believes-single-sex-schools-are-good-education',
        'https://idebate.org/debatabase/environment-animals-philosophy-ethics-science-science-general/house-would-ban-animal',
        'https://idebate.org/debatabase/law-crime-policing-punishment-philosophy-ethics-life/house-supports-death-penalty',
        'https://idebate.org/debatabase/culture-culture-general-media-modern-culture-television/house-believes-reality-television',
        'https://idebate.org/debatabase/education-university-government/house-believes-university-education-should-be-free',
        'https://idebate.org/debatabase/health-disease-healthcare-philosophy-ethics-life/house-believes-assisted-suicide-should',
        'https://idebate.org/debatabase/health-addiction-health-general-society/house-believes-cannabis-should-be-legalised',
        'https://idebate.org/debatabase/health-health-general-weight/house-would-ban-junk-food-schools',
        'https://idebate.org/debatabase/society-gender-family/house-believes-homosexuals-should-be-able-adopt']

topics = ['airbrushing', 'singleSexSchools', 'animalTesting', 'deathPenalty', 'realityTV', 'freeHigherEd', 'euthanesia', 'marijuana', 'junkfoodSchools', 'samesexAdoption']


if len(URLs) == len(topics):
    for index in range(0, len(URLs)):
        print("scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\\" + topics[index] + ".json -a domain=" + URLs[index])

###Procon short arguments
URLs = ['https://gun-control.procon.org/',
        'https://animal-testing.procon.org/',
        'https://marijuana.procon.org/',
        'https://school-uniforms.procon.org/',
        'https://drinkingage.procon.org/',
        'https://socialnetworking.procon.org/',
        'https://vaccines.procon.org/',
        'https://abortion.procon.org/',
        'https://vegetarian.procon.org/',
        'https://healthcare.procon.org/',
        'https://school-uniforms.procon.org/',
        'https://standardizedtests.procon.org/',
        'https://tablets-textbooks.procon.org/',
        'https://concealedguns.procon.org/',
        'https://drones.procon.org/',
        'https://gaymarriage.procon.org/']

topics = ['gunControl', 'animalTesting', 'marijuana', 'schoolUniforms', 'drinkingAge', 'socialNetworking', 'vaccinesRequiredChildren', 'abortion', 'vegetarian', 'rightToHealthcare', 'schoolUniforms', 'standarizedTests', 'textbooTablets', 'conceiledCarrying', 'droneStrikes', 'gayMarriage']

if len(URLs) == len(topics):
    for index in range(0, len(URLs)):
        print("scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\\" + topics[index] + ".json -a domain=" + URLs[index])

###Procon long arguments
URLs = ['https://medicalmarijuana.procon.org/view.answers.php?questionID=001325',
        'https://euthanasia.procon.org/view.answers.php?questionID=001320',
        'https://immigration.procon.org/view.answers.php?questionID=001362',
        'https://prostitution.procon.org/view.answers.php?questionID=001315']

topics = ['medicalMarijuana', 'euthanesia', 'illegalAliens', 'prostitution']

if len(URLs) == len(topics):
    for index in range(0, len(URLs)):
        print("scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\longArguments\\" + topics[index] + ".json -a domain=" + URLs[index])
