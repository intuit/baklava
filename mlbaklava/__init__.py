try:
    from mlbaklava.__version import __version__
except ImportError:  # pragma: no cover
    __version__ = 'dev'

from mlbaklava.api import (
    train,
    deploy,
    process,
)
