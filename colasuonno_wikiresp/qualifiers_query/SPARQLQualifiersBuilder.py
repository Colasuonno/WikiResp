class SPARQLBuilder:
    """
    SPARLBuilder for wikiData service
    WARNING: THIS CLASS IS MADE ONLY FOR STATEMENTS QUESTION, IT CANNOT BE GENERALIZED
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
        return self

    def where_struct(self, assignments, optionals_assignments):
        """
        Assuming conditions and optionals are a dict
        WARNING: in this section we are only focussing ?id Label which is involved
        :param optionals_assignments:
        :param assignments:
        :param self:
        :return: self
        """
        self.qw = self.query_where
        for key in assignments:
            self.qw += key + " " + assignments[key] + ". \n"
        self.qw += "OPTIONAL { \n"
        for key in optionals_assignments:
            self.qw += key + " " + optionals_assignments[key] + ". \n"
        self.qw += "}"

        return self

    def build(self, result_lang, last="", limit=None):
        q = self.qs + self.qw + """SERVICE wikibase:label { bd:serviceParam wikibase:language 
        \"""" + result_lang + """\".}""" \
               + """?id ?label \"""" + self.name + """\"@it. }"""
        if limit is not None and limit != "":
            q += " LIMIT " + str(limit)
        if last is set:
            q += " " + str(last)

        return q
