import click
import os
import sys
import subprocess
import re
from git.repo.base import Repo


# Classpath settings
PROJECT_ROOT = "."


def run_cmd(cmd):
    cmd = 'mujava.' + cmd
    lib_path = os.path.join(PROJECT_ROOT, "lib")
    class_path = os.path.join(lib_path, "*")
    subprocess.call(["java", '-cp', class_path, cmd], cwd=PROJECT_ROOT)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
def init(name):
    """Initializes new mujava project."""
    global PROJECT_ROOT

    click.clear()

    # Check Java installation
    click.echo("Checking Java installation...")

    if os.system("java -version") is not 0:
        click.echo("Java installation not found")
        sys.exit(-1)

    # Find Java Version
    version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
    pattern = '\"(\d+\.\d+).*\"'
    java_version = re.search(pattern, version.decode('ascii')).groups()[0]

    needs_tools = False

    if java_version is '1.8':
        needs_tools = True

    # Clone starter project
    Repo.clone_from("https://github.com/clintonyeb/mujava-starter", name)

    # Create config file in project root
    dir_path = os.getcwd()
    project_root = os.path.join(dir_path, name)
    config = os.path.join(name, 'mujava.config')

    with open(config, 'w') as f:
        f.write('MuJava_HOME=' + project_root)

    PROJECT_ROOT = project_root

    # Make directory structure
    run_cmd('makeMuJavaStructure')

    click.echo("\nProject Initiation complete.")


@cli.command()
def generate():
    """Starts GUI to generate mutants"""
    click.echo("\nStarting GUI Interface")
    run_cmd('gui.GenMutantsMain')


@cli.command()
def test():
    """Starts GUI to generate mujava tests"""
    click.echo("\nStarting GUI Interface")
    run_cmd('gui.RunTestMain')


# @cli.command()
# def build():
#     click.echo("\nFeature not supported yet")


if __name__ == '__main__':
    cli()
