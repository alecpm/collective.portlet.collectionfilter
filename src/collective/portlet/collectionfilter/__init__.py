from zope.i18nmessageid import MessageFactory

msgFact = MessageFactory('collective.portlet.collectionfilter')

# Add request filtering to collection query for AT plone.app.collection
try:
    from plone.app.collection.collection import Collection
except ImportError:
    Collection = None

if Collection is not None:
    def custom_results(self, *args, **kw):
        if kw.get('custom_query') is None:
            request = getattr(self, 'REQUEST', None)
            if request and request.form:
                kw['custom_query'] = request.form.copy()
        return self._orig_results(*args, **kw)

    Collection._orig_results = Collection.results
    Collection.results = custom_results
