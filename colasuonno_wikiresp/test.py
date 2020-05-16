from queries import WikiQuery
from datetime import datetime
from models import PlanetModels as pm
from models import HumansModels as hm
from models import GeographicModels as gm
from queries.WikiQuery import init_query


#query = DirectWikiQuery("Aster", "Dante Alighieri")
#elements = hm.languages_spoken()
#query.lazy_init(elements[0], elements[1], elements[2], elements[3], elements[4])
#print(query.pretty_print())

elements = hm.birth_death()
query = init_query("Aster", "", elements)

while(True):
    name = input("Block: ")
    query.builder.name = name
    starting = datetime.now()
    query.init(elements)
    print(query.pretty_print())
    print(query.query_txt)
    end = datetime.now()
    tot = end - starting
    print({"Request elapsed time": str(tot.total_seconds()) + "s"})

