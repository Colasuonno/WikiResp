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

    def where_struct(self, conditions, quantity_labels):
        """
        Assuming conditions and optionals are a dict
        WARNING: in this section we are only focussing ?id Label which is involved
        :param quantity_labels:
        :param self:
        :param conditions: dict
        :return: self
        """
        self.qw = self.query_where
        cond = "?id "
        for key in conditions:
            cond += key + ":" + conditions[key] + "/"
        cond = cond[:-1]
        cond += " [ "
        for i in range(0, len(quantity_labels)):
            key = list(quantity_labels.keys())[i]
            if i == len(quantity_labels)-1:
                cond += key + " " + quantity_labels[key] + "].\n"
            else:
                cond += key + " " + quantity_labels[key] + "; \n"
        self.qw += cond + " \n"
        return self

    def build(self, result_lang, limit=None):
        q = self.qs + self.qw + """SERVICE wikibase:label { bd:serviceParam wikibase:language 
        \"""" + result_lang + """\".}""" \
               + """?id ?label \"""" + self.name + """\"@en. }"""
        if limit is not None:
            q += " LIMIT " + str(limit)
        return q
