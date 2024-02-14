import logging

import click
import colorama

from lodocker.helpers import ClickHelpers, DevContainer, Helpers
from lodocker.run_container import RunContainer


@click.command()
@click.option(
    '--dir', 'dockerfile_dirname',
    callback=ClickHelpers.directory_callback,
    expose_value=True,
    is_eager=False,
    prompt=False,
    required=False,
    help='Directory name with Dockerfile inside the docker_files directory'
)
def start_container(dockerfile_dirname: str):
    """Start LibreOffice Docker container."""
    logging.basicConfig(level=logging.INFO)
    colorama.init(autoreset=True)
    image_name = Helpers.get_image_name(dockerfile_dirname)
    if image_name is None:
        logging.error("Aborting docker build.")
        return
    exec_name = Helpers.get_libreoffice_exec_name(dockerfile_dirname)
    lo_userdir = Helpers.get_libreoffice_userdir(dockerfile_dirname)
    RunContainer().start_container(image_name, exec_name, lo_userdir)


if __name__ == "__main__":
    start_container()
