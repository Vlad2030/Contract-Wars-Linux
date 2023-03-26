import platform
import subprocess

import distro


class Detect:
    """
    class Detect:
        system() - Get a platform name ("Linux", "Windows", "Darvin" etc..)

        distr_id() - Get a distro id

        distr_name() - Get a distro name
    """

    def __init__(self) -> None:
        pass

    def system() -> str:
        """
        Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

        An empty string is returned if the value cannot be determined.
        """
        return platform.system()

    def distr_id() -> str:
        """
        Return the distro ID of the current distribution, as a machine-readable string.

        For a number of OS distributions, the returned distro ID value is *reliable*, in the sense that it is documented and that it does not change across releases of the distribution.
        """
        return distro.id()

    def distr_name() -> str:
        """
        Return the name of the current OS distribution, as a human-readable string.
        """
        return distro.name(pretty=False)


class Terminal:
    """
    class Terminal:
        send() - send command to terminal
    """
    def __init__(self, command: str, stdout: bool) -> None:
        self.command: str = command
        self.stdout: bool = stdout

    def send(command: str, stdout: None = None) -> str:
        """send command to terminal

        Args:
            command (str): your command
            stdout (bool): if given, return str answer from terminal

        Raises:
            TypeError
        """
        if not isinstance(command, str):
            raise TypeError("Only str type")

        if stdout is None:
            stdout: str = subprocess.PIPE

        return subprocess.run(
            args=command.split(" "),
            stdout=stdout,
        )


class Find:
    def __init__(self) -> None:
        pass

    def package(name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Only str type")

        command: str = Terminal.send(
            command=f"whereis {name}",
            stdout=True,
        ).stdout.decode()

        if f"/usr/bin/{name}" in command:
            return True

        return False
