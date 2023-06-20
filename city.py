travel_log=[
    {"country":"Frnace","Counrty_Code":13,"no_of_vistited":10},
    {"country":"Germany","Country_Code":30,"no_of_vistited":12}
]
def add_country(country_name,country_code,visited):
    new_country={}
    new_country["country"]=country_name
    new_country["code"]=country_code
    new_country["visit"]=visited
    print(new_country)    
    travel_log.append(new_country)
    print(travel_log)
add_country("North America",7,16)    