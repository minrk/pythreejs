from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class StereoCamera(ThreeWidget):
    """StereoCamera
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 17:17:07 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Cameras/StereoCamera 
    """

    def __init__(self, **kwargs):
        super(ThreeWidget, self).__init__(**kwargs)

    _view_name = Unicode('StereoCameraView').tag(sync=True)
    _model_name = Unicode('StereoCameraModel').tag(sync=True)

