from direct_query.DirectWikiQuery import DirectWikiQuery
from statements_query.StatementWikiQuery import StatementWikiQuery


def init_query(name, label, elements):
    type_ = elements["type"]
    if type_ == "DirectWikiQuery":
        return DirectWikiQuery(name, label)
    elif type_ == "StatementWikiQuery":
        return StatementWikiQuery(name, label)
        pass
