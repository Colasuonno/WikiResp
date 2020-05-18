class SPARQLBuilder:
    """
    SPARLBuilder for wikiData service
    IT USES THE LABEL SERVICE (bd:serviceParam wikibase:language "it".)
    BUT IT SEARCHES IN ENGLISH FORMAT (?id ?label "_name"@en)
    """

    def __init__(self, name, result_lang, language_ind):
        self.query_select = "SELECT DISTINCT ?id ?idLabel "  # "...."
        self.query_where = "WHERE {"  # "....}"
        self.labels = []
        self.name = name
        self.language_ind = language_ind
        self.result_lang = result_lang
        self.qs = ""
        self.qw = ""
        self.last_result = []

    def select_labels(self, labels):
        self.labels = labels
        self.qs = self.query_select
        for label in labels:
            self.qs += "?" + label + " "
        return self

    def where_struct(self, elements):
        """
        Assuming conditions and optionals are a dict
        WARNING: in this section we are only focussing ?id Label which is involved
        :param elements:
        :param self:
        """
        self.qw = self.query_where + "\n"
        conditions = elements["conditions"]
        optionals = elements["optional_conditions"]
        limit = elements["limit"]
        last = elements["last"]
        for num in conditions:
            cond = conditions[num]
            self.qw += cond["startVar"] + " " + cond["conditions"] + " " + cond["endVar"] + " . \n"
        self.qw += "OPTIONAL { \n"
        for num in optionals:
            cond = optionals[num]
            self.qw += cond["startVar"] + " " + cond["conditions"] + " " + cond["endVar"] + " . \n"
        self.qw += "} \n"
        self.qw += """SERVICE wikibase:label { bd:serviceParam wikibase:language 
               \"""" + self.result_lang + """\".}""" \
            + """?id ?label \"""" + self.name + """\"@""" + self.language_ind  + """. }"""

        self.qw += last + "\n"
        self.qw += "LIMIT " + str(limit) + " \n"

        self.qw = self.qw.replace("{lang_ind}", str(self.language_ind))
        return self

    def build(self):
        q = self.qs + self.qw
        print(q)
        return q

