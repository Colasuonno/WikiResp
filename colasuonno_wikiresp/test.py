from direct_query.DirectWikiQuery import DirectWikiQuery
from statements_query.StatementWikiQuery import StatementWikiQuery
from datetime import datetime
from models import PlanetModels as pm
from models import HumansModels as hm
from models import GeographicModels as gm


#query = DirectWikiQuery("Aster", "Dante Alighieri")
#elements = hm.languages_spoken()
#query.lazy_init(elements[0], elements[1], elements[2], elements[3], elements[4])
#print(query.pretty_print())

query = DirectWikiQuery("Aster", "Great Britain")

while(True):
    name = input("Block: ")
    starting = datetime.now()
    elements = gm.flag_image()
    query.lazy_init(elements[0], elements[1], elements[2], elements[3], elements[4])
    print(query.pretty_print())
    end = datetime.now()
    tot = end - starting
    print({"Request elapsed time": str(tot.total_seconds()) + "s"})

