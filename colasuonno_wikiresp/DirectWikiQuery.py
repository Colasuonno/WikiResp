import sys
from SPARQLWrapper import SPARQLWrapper, JSON
from SPARQLSimpleBuilder import SPARQLBuilder

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
        self.result_lang = "it"
        self.query_txt = ""

    def query(self, query):
        self.sparql.setQuery(query)
        self.query_txt = query
        return self.sparql.query().convert()["results"]["bindings"]

    def birth_death(self):
        """
        CONDITIONS:
        INSTANCE OF HUMAN
        ASSUMING
        BIRTH
        OPTIONAL ASSUMING
        DEATH
        :return:
        """
        self.builder.select_labels(["birth", "death"])
        self.builder.where_struct({"P31": "Q5"}, {"P19": "?birth"}, {}, {"P20": "?death"})
        return self.build()

    def languages_spoken(self):
        """
        CONDITIONS:
        INSTANCE OF HUMAN
        ASSUMING
        LANGUAGES SPOKEN
        :return:
        """
        self.builder.select_labels(["languages_spoken"])
        self.builder.where_struct({"P31": "Q5"}, {"P1412": "?languages_spoken"}, {}, {})
        return self.build()

    def father_mather(self):
        """
        CONDITIONS:
        INSTANCE OF HUMAN
        ASSUMING
        MATHER
        FATHER
        :return:
        """
        self.builder.select_labels(["father", "mother"])
        self.builder.where_struct({"P31": "Q5"}, {}, {}, {"P22": "?father", "P25": "?mother"})
        return self.build()

    def build(self):
        self.builder.last_result = self.query(self.builder.build(self.result_lang))
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
