from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .Texture_autogen import Texture


class CubeTexture(Texture):
    """CubeTexture
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 17:17:08 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Textures/CubeTexture 
    """

    def __init__(self, **kwargs):
        super(Texture, self).__init__(**kwargs)

    _view_name = Unicode('CubeTextureView').tag(sync=True)
    _model_name = Unicode('CubeTextureModel').tag(sync=True)

