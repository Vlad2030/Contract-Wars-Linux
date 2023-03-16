import platform

import distro


class Detect:
    """
    class Detect:
        system() - Get a platform name ("Linux", "Windows", "Darvin" etc..)

        distr() - Get a distro
    """

    def __init__(self) -> None:
        pass

    def system() -> str:
        """
        Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

        An empty string is returned if the value cannot be determined.
        """
        return platform.system()

    def distr(id: bool = True, name: bool = False) -> str:
        if not isinstance(id and name, bool):
            raise TypeError("Only bool type")

        if id and name:
            raise ValueError("Only id or name argument")

        if id:
            return distro.id()

        if name:
            return distro.name(pretty=False)
