import sys
from SPARQLWrapper import SPARQLWrapper, JSON
from .SPARQLStatementBuilder import SPARQLBuilder

endpoint_url = "https://query.wikidata.org/sparql"


class StatementWikiQuery:
    """
    This class uses the default endpoint (wikidata) as a source
    <link>https://query.wikidata.org/sparql</link>
    The Query structure is SPARQL
    The response is in JSON
    """

    def __init__(self, name="WikiResp", label="Dante Alighieri"):
        self.sparql = SPARQLWrapper(endpoint_url, agent=(name + "/%s.%s" % (sys.version_info[0], sys.version_info[1])))
        self.sparql.setReturnFormat(JSON)
        self.builder = SPARQLBuilder(label)
        self.result_lang = "[AUTO_LANGUAGE],en,it"
        self.query_txt = ""

    def query(self, query):
        self.sparql.setQuery(query)
        self.query_txt = query
        return self.sparql.query().convert()["results"]["bindings"]

    def lazy_init(self, labels, conditions, quantity_labels, limit=None):
        self.builder.select_labels(labels)
        self.builder.where_struct(conditions, quantity_labels)
        return self.build(limit)

    def build(self, limit=None):
        self.builder.last_result = self.query(self.builder.build(self.result_lang, limit))
        return self.builder.last_result

    def pretty_print(self):
        """
        Pretty the result
        :return: the cooler JSON ever
        """
        result = {}
        bindings = self.builder.last_result
        if len(bindings) == 0:
            return result
        result["id"] = bindings[0]["idLabel"]["value"]
        for bind in bindings:
            for label in self.builder.labels:
                if label in bind:
                    if label in result:
                        result[label] = result[label] + ", " + bind[label]["value"]
                    else:
                        result[label] = bind[label]["value"]
        return result
