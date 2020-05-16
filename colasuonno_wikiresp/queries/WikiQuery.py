from direct_query.DirectWikiQuery import DirectWikiQuery


def init_query(name, label, elements):
    type_ = elements["type"]
    if type_ == "DirectWikiQuery":
        return DirectWikiQuery(name, label)
    elif type_ == "StatementWikiQuery":
        pass
