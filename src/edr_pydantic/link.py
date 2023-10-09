from typing import Optional
from typing import Union

from .my_base_model import EDRBaseModel
from .variables import CorridorVariables
from .variables import CubeVariables
from .variables import ItemVariables
from .variables import RadiusVariables
from .variables import Variables


class Link(EDRBaseModel):
    href: str
    hreflang: Optional[str] = None
    rel: str
    # TODO According to A.21 & A.23 all links shall include type
    type: Optional[str] = None
    title: Optional[str] = None
    length: Optional[int] = None
    templated: Optional[bool] = None
    variables: Optional[Union[Variables, CubeVariables, CorridorVariables, ItemVariables, RadiusVariables]] = None


# For EDRQueryLink the variables element is required compared to the Link object
class EDRQueryLink(Link, extra="allow"):
    variables: Union[Variables, CubeVariables, CorridorVariables, ItemVariables, RadiusVariables]
