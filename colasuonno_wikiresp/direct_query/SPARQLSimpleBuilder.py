class SPARQLBuilder:
    """
    SPARLBuilder for wikiData service
    WARNING: THIS CLASS IS MADE ONLY FOR DIRECT QUESTION, IT CANNOT BE GENERALIZED
    IT USES THE LABEL SERVICE (bd:serviceParam wikibase:language "it".)
    BUT IT SEARCHES IN ENGLISH FORMAT (?id ?label "_name"@en)
    """

    def __init__(self, name):
        self.query_select = "SELECT DISTINCT ?id ?idLabel "  # "...."
        self.query_where = "WHERE {"  # "....}"
        self.labels = []
        self.name = name
        self.qs = ""
        self.qw = ""
        self.last_result = []

    def select_labels(self, labels):
        self.labels = labels
        self.qs = self.query_select
        for label in labels:
            self.qs += "?" + label + " "
            self.qs += "?" + label + "Label" + " "  # We are using the Label Service
        return self

    def where_struct(self, conditions, vars_assuming, optionals_conditions, optionals_vars_assuming):
        """
        Assuming conditions and optionals are a dict
        EXAMPLE (we want the birthPlace):
            {"P19": "?birth"} WHERE ?birth is declared  in the select_labels
        WARNING: in this section we are only focussing ?id Label which is involved
        :param self:
        :param conditions: dict
        :param optionals: dict
        :return: self
        """
        self.qw = self.query_where
        for key in conditions:
            self.qw += "?id wdt:" + key + " wd:" + conditions[key] + ". \n"
        for key in vars_assuming:
            self.qw += "?id wdt:" + key + vars_assuming[key] + ". \n"
        self.qw += "OPTIONAL { "
        for key in optionals_conditions:
            self.qw += "?id wdt:" + key + " wd:" + optionals_conditions[key] + ". \n"
        for key in optionals_vars_assuming:
            self.qw += "?id wdt:" + key + optionals_vars_assuming[key] + ". \n"
        self.qw += "} "
        return self

    def build(self, result_lang, last="", limit=None):
        q = self.qs + self.qw + """SERVICE wikibase:label { bd:serviceParam wikibase:language 
        \"""" + result_lang + """\".}""" \
               + """?id ?label \"""" + self.name + """\"@en. }"""
        if limit is not None:
            q += " LIMIT " + str(limit)
        if last != "":
            q += " " + str(last)
        return q
