from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .Light_autogen import Light


class HemisphereLight(Light):
    """HemisphereLight
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 17:17:07 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Lights/HemisphereLight 
    """

    def __init__(self, color="#ffffff", groundColor="#000000", intensity=1, **kwargs):
        kwargs['color'] = color
        kwargs['groundColor'] = groundColor
        kwargs['intensity'] = intensity
        super(Light, self).__init__(**kwargs)

    _view_name = Unicode('HemisphereLightView').tag(sync=True)
    _model_name = Unicode('HemisphereLightModel').tag(sync=True)

    groundColor = Unicode("#000000").tag(sync=True)
