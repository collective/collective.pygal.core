from plone.theme.interfaces import IDefaultPloneLayer
from zope import interface

class ILayer(interface.Interface):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """
