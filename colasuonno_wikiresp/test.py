from DirectWikiQuery import DirectWikiQuery
from datetime import datetime

starting = datetime.now()
query = DirectWikiQuery("Aster", "Dante Alighieri")
query.result_lang = "it"
query.father_mather()
#print(query.query_txt)
print(query.pretty_print())
end = datetime.now()
tot = end - starting
print({"Request elapsed time": str(tot.total_seconds()) + "s"})

