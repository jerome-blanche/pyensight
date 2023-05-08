"""launch_ensight module

The launch_ensight module provides pyensight with the ability to launch an
EnSight session using PyPIM.  This leverages the DockerLauncherEnShell module.

Examples:
    ::

        from ansys.pyensight import launch_ensight
        session = launch_ensight()
        # do pyensight stuff with the session
        session.close()
"""

from typing import Optional

from ansys.pyensight.locallauncher import LocalLauncher
from ansys.pyensight.session import Session

pim_is_available = False
try:
    import ansys.platform.instancemanagement as pypim

    pim_is_available = True
except Exception:
    pass
# print(f"pim_is_available: {pim_is_available}\n")

docker_is_available = False
try:
    from ansys.pyensight.dockerlauncherenshell import DockerLauncherEnShell

    docker_is_available = True
except Exception:
    pass
# print(f"docker_is_available: {docker_is_available}\n")


if pim_is_available:

    def _launch_ensight_with_pim(
        product_version: str = None,
        use_egl: Optional[bool] = False,
        use_sos: Optional[int] = None,
    ) -> "Session":
        """Internal function.
        Start via PyPIM the EnSight Docker container with EnShell as the ENTRYPOINT.
        Create and bind a Session instance to the created gRPC session.  Return that session.

        Args:
          product_version : str, optional
            Version of the product. For example, "232". The default is "None", in which case
          use_egl:
            If True, EGL hardware accelerated graphics will be used. The platform
            must be able to support it.
          use_sos:
            If None, don't use SOS. Otherwise, it's the number of EnSight Servers to use (int).

        Returns:
          pyensight Session object instance
        """

        pim = pypim.connect()
        instance = pim.create_instance(
            product_name="ensight",
            product_version=product_version,
        )
        instance.wait_for_ready()
        # use defaults as specified by PIM
        channel = instance.build_grpc_channel(
            options=[
                ("grpc.max_receive_message_length", -1),
                ("grpc.max_send_message_length", -1),
                ("grpc.testing.fixed_reconnect_backoff_ms", 1100),
            ]
        )

        launcher = DockerLauncherEnShell(
            use_egl=use_egl,
            use_sos=use_sos,
            channel=channel,
            pim_instance=instance,
        )
        return launcher.connect()


def launch_ensight(
    product_version: Optional[str] = None,
    use_pim: Optional[bool] = True,
    use_docker: Optional[bool] = True,
    data_directory: Optional[str] = None,
    docker_image_name: Optional[str] = None,
    use_dev: Optional[bool] = False,
    ansys_installation: Optional[str] = None,
    application: Optional[str] = "ensight",
    batch: Optional[bool] = True,
    use_egl: Optional[bool] = False,
    use_sos: Optional[int] = None,
    timeout: Optional[float] = 120.0,
) -> "Session":
    """Start an EnSight session via EnShell using the Docker EnSight Image.
    Return that session.

    Args:
      product_version : str, optional
        Select an installed version of ANSYS. The string must be in a format like
        "232" (for 2023 R2). The default is "None", in which case the newest installed
        version is used.
      use_pim : bool, optional
        If True, then PyPIM is used to launch EnSight.
      use_docker : bool, optional
        If True, use DockerLaucherEnShell. If use_pim is True, this option is ignored.
      data_directory:
        Host directory to make into the Docker container at /data
        Only used if use_docker is True.
      docker_image_name:
        Optional Docker Image name to use
      use_dev:
        Option to use the latest ensight_dev Docker Image; overridden by docker_image_name if specified.
      ansys_installation:
        Location of the ANSYS installation, including the version
        directory Default: None (causes common locations to be scanned).
        If use_pim is True, this option is ignored.  If use_docker is True, this option is ignored.
      application:
        The application to be launched. By default, "ensight", but
        "envision" is also available.
      batch:
        By default, the EnSight/EnVision instance will run in batch mode.
        If batch is set to False, the full GUI will be presented.
        Only used if use_pim and use_docker are False.
      use_egl:
        If True, EGL hardware accelerated graphics will be used. The platform
        must be able to support it.
      use_sos:
        If None, don't use SOS. Otherwise, it's the number of EnSight Servers to use (int).
      timeout:
        In some cases where the EnSight session can take a significant amount of
        time to start up, this is the number of seconds to wait before failing
        the connection.  The default is 120.0.

    Returns:
      pyensight Session object instance

    Raises:
      RuntimeError:
          variety of error conditions.
    """

    # print(f"pim_is_available: {pim_is_available}  use_pim: {use_pim}\n")
    if pim_is_available and use_pim:
        if pypim.is_configured():
            return _launch_ensight_with_pim(
                product_version=product_version, use_egl=use_egl, use_sos=use_sos
            )

    # not using PIM, but use Docker
    # print(f"docker_is_available: {docker_is_available}  use_docker: {use_docker}\n")
    if docker_is_available and use_docker:
        launcher = DockerLauncherEnShell(
            data_directory=data_directory,
            docker_image_name=docker_image_name,
            use_dev=use_dev,
            timeout=timeout,
            use_egl=use_egl,
            use_sos=use_sos,
        )
        return launcher.start()

    # use local installation of EnSight
    launcher = LocalLauncher(
        ansys_installation=ansys_installation,
        application=application,
        batch=batch,
        timeout=timeout,
        use_egl=use_egl,
        use_sos=use_sos,
    )
    return launcher.start()
