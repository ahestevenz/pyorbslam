import logging

from .__logger import setup
from .state import State
from .sensor import Sensor
from . import utils
from .slam import MonoSLAM, MonoIMUSLAM, StereoSLAM, StereoIMUSLAM, RgbdSLAM
from . import orbslam3

# Setup logging
setup()
logger = logging.getLogger("pyorbslam")

__all__ = [
    'State',
    'Sensor',
    'utils',
    'MonoSLAM',
    'MonoIMUSLAM',
    'StereoSLAM',
    'StereoIMUSLAM',
    'RgbdSLAM',
    'orbslam3',
]

# nano-explorer: trajectory_drawer/ and tools.py need the `viewer`/`tools`
# extras (PyQt5/pyqtgraph/trimesh/... and plyfile/pandas respectively — see
# pyproject.toml) that a bare `pip install .` no longer installs. Neither is
# needed for `from pyorbslam import orbslam3` (the only thing nano-explorer's
# own integration uses), so importing either here is now best-effort: log and
# move on rather than making `import pyorbslam` itself fail when those extras
# aren't installed.
try:
    from .trajectory_drawer import TrajectoryDrawer, TDApp

    __all__ += ['TrajectoryDrawer', 'TDApp']
except ImportError as e:
    logger.warning(f"trajectory_drawer unavailable (install the 'viewer' extra to use it): {e}")

try:
    from . import tools

    __all__ += ['tools']
except ImportError as e:
    logger.warning(f"tools unavailable (install the 'tools' extra to use it): {e}")
