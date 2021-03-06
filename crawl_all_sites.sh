#!/bin/bash
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\airbrushing.json -a domain=https://idebate.org/debatabase/culture-media/should-airbrushing-womens-bodies-be-banned
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\singleSexSchools.json -a domain=https://idebate.org/debatabase/education/house-believes-single-sex-schools-are-good-education
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\animalTesting.json -a domain=https://idebate.org/debatabase/environment-animals-philosophy-ethics-science-science-general/house-would-ban-animal
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\deathPenalty.json -a domain=https://idebate.org/debatabase/law-crime-policing-punishment-philosophy-ethics-life/house-supports-death-penalty
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\realityTV.json -a domain=https://idebate.org/debatabase/culture-culture-general-media-modern-culture-television/house-believes-reality-television
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\freeHigherEd.json -a domain=https://idebate.org/debatabase/education-university-government/house-believes-university-education-should-be-free
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\euthanesia.json -a domain=https://idebate.org/debatabase/health-disease-healthcare-philosophy-ethics-life/house-believes-assisted-suicide-should
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\marijuana.json -a domain=https://idebate.org/debatabase/health-addiction-health-general-society/house-believes-cannabis-should-be-legalised
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\junkfoodSchools.json -a domain=https://idebate.org/debatabase/health-health-general-weight/house-would-ban-junk-food-schools
scrapy runspider crawler_debatabase.py -o Crawled\Debatabase\samesexAdoption.json -a domain=https://idebate.org/debatabase/society-gender-family/house-believes-homosexuals-should-be-able-adopt
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\gunControl.json -a domain=https://gun-control.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\animalTesting.json -a domain=https://animal-testing.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\marijuana.json -a domain=https://marijuana.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\schoolUniforms.json -a domain=https://school-uniforms.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\drinkingAge.json -a domain=https://drinkingage.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\socialNetworking.json -a domain=https://socialnetworking.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\vaccinesRequiredChildren.json -a domain=https://vaccines.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\abortion.json -a domain=https://abortion.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\vegetarian.json -a domain=https://vegetarian.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\rightToHealthcare.json -a domain=https://healthcare.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\schoolUniforms.json -a domain=https://school-uniforms.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\standarizedTests.json -a domain=https://standardizedtests.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\textbooTablets.json -a domain=https://tablets-textbooks.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\conceiledCarrying.json -a domain=https://concealedguns.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\droneStrikes.json -a domain=https://drones.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\shortArguments\gayMarriage.json -a domain=https://gaymarriage.procon.org/
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\longArguments\medicalMarijuana.json -a domain=https://medicalmarijuana.procon.org/view.answers.php?questionID=001325
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\longArguments\euthanesia.json -a domain=https://euthanasia.procon.org/view.answers.php?questionID=001320
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\longArguments\illegalAliens.json -a domain=https://immigration.procon.org/view.answers.php?questionID=001362
scrapy runspider crawler_debatabase.py -o Crawled\ProconOrg\longArguments\prostitution.json -a domain=https://prostitution.procon.org/view.answers.php?questionID=001315