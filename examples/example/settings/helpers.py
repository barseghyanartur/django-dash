import os

__all__ = (
    'gettext',
    'project_dir',
    'PROJECT_DIR',
)


def project_dir(base):
    """Project dir."""
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), base).replace('\\', '/')
    )


PROJECT_DIR = project_dir


def gettext(val):
    """Fake gettext."""
    return val
