import colander


class WikipediaSchema(colander.MappingSchema):
    url = colander.SchemaNode(
        colander.String(),
        validator=colander.Regex(
            r'(http)s?(://)(.*)(wikipedia.org/wiki/)(.*)',
            'The provided URL should be for the wikipedia.org domain,'
            ' eg. "https://en.wikipedia.org/wiki/Dog"'
        )
    )
