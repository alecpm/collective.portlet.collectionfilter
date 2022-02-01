from Products.CMFPlone.utils import safe_unicode
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory


def safe_decode(val):
    """Safely create unicode values.
    """
    ret = None
    if isinstance(val, dict):
        ret = dict([(safe_decode(k), safe_decode(v)) for k, v in val.items()])
    elif isinstance(val, list):
        ret = [safe_decode(it) for it in val]
    elif isinstance(val, tuple):
        ret = (safe_decode(it) for it in val)
    else:
        ret = safe_unicode(val)
    return ret


def safe_encode(val):
    """Safely encode a value to utf-8.
    """
    ret = None
    if isinstance(val, dict):
        ret = dict([(safe_encode(k), safe_encode(v)) for k, v in val.items()])
    elif isinstance(val, list):
        ret = [safe_encode(it) for it in val]
    elif isinstance(val, tuple):
        ret = (safe_encode(it) for it in val)
    else:
        ret = safe_unicode(val).encode('utf-8')
    return ret


def title_for_type(type_name):
    types_vocab = queryUtility(
        IVocabularyFactory,
        name='plone.app.vocabularies.ReallyUserFriendlyTypes'
    )
    if types_vocab is None:
        return type_name
    types_vocab = types_vocab(None)
    try:
        term = types_vocab.getTerm(type_name)
    except LookupError:
        return None
    return term.title
