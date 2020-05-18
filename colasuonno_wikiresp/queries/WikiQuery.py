import sys
from SPARQLWrapper import SPARQLWrapper, JSON
from .SPARQLBuilder import SPARQLBuilder
import json

endpoint_url = "https://query.wikidata.org/sparql"


class WikiQuery:
    """
    This class uses the default endpoint (wikidata) as a source
    <link>https://query.wikidata.org/sparql</link>
    The Query structure is SPARQL
    The response is in JSON
    """

    def __init__(self, name="WikiResp", label="Dante Alighieri", language_ind="en"):
        self.sparql = SPARQLWrapper(endpoint_url, agent=(name + "/%s.%s" % (sys.version_info[0], sys.version_info[1])))
        self.sparql.setReturnFormat(JSON)
        self.result_lang = "[AUTO_LANGUAGE],it,en"
        self.builder = SPARQLBuilder(label, self.result_lang, language_ind)
        self.query_txt = ""

    def query(self, query):
        self.sparql.setQuery(query)
        self.query_txt = query
        return self.sparql.query().convert()["results"]["bindings"]

    def init(self, elements):
        self.builder.select_labels(elements["labels"])
        self.builder.where_struct(elements)
        return self.build()

    def build(self):
        self.builder.last_result = self.query(self.builder.build())
        return self.builder.last_result

    def pretty_print(self):
        """
        Pretty the result
        :return: the cooler JSON ever
        """
        result = {

        }
        bindings = self.builder.last_result
        if len(bindings) == 0:
            return result
        a = 0

        for bind in bindings:
            for label in self.builder.labels:
                if a not in result:
                    result[a] = {}
                if label in bind:
                    result[a][label] = bind[label]["value"]
                    if "id" not in result[a]:
                        result[a]["id"] = bind["idLabel"]["value"]
            a += 1

        return json.dumps(result)
