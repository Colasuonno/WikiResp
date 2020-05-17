import sys
from SPARQLWrapper import SPARQLWrapper, JSON
from .SPARQLSimpleBuilder import SPARQLBuilder

endpoint_url = "https://query.wikidata.org/sparql"


class DirectWikiQuery:
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

    def init(self, elements, limit=None):
        self.builder.select_labels(elements["labels"])
        self.builder.where_struct(elements["conditions"], elements["assignments"], elements["optional_conditions"],
                                  elements["optional_assignments"])
        last = None
        if "last" in elements:
            last = elements["last"]
        return self.build(limit, last)

    @DeprecationWarning
    def lazy_init(self, labels, conditions, vars_assuming, optionals_conditions, optionals_vars_assuming, limit=None):
        self.builder.select_labels(labels)
        self.builder.where_struct(conditions, vars_assuming, optionals_conditions, optionals_vars_assuming)
        return self.build(limit)

    def build(self, limit=None, last=""):
        self.builder.last_result = self.query(self.builder.build(self.result_lang, last, limit))
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
                if label + "Label" in bind:
                    if label in result:
                        result[label] = result[label] + ", " + bind[label + "Label"]["value"]
                    else:
                        result[label] = bind[label + "Label"]["value"]
        return result
