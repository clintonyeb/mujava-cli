import click
import os
import sys
import subprocess
import wget


# Classpath settings
PROJECT_ROOT = "."


def run_cmd(cmd, cwd=False):
    cmd = 'mujava.' + cmd
    lib_path = os.path.join(PROJECT_ROOT, "lib")
    class_path = os.path.join(lib_path, "*")
    if cwd:
        subprocess.call(["java", '-cp', class_path, cmd], cwd=PROJECT_ROOT)
    else:
        subprocess.call(["java", '-cp', class_path, cmd])


def is_valid_directory():
    return os.path.exists("mujava.config")


def is_valid_command():
    if not is_valid_directory():
        click.echo("No project found in current folder")
        click.echo("Make sure you `cd` into your project folder before running this command")
        return False

    return True


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
def init(name):
    """Initializes new mujava project."""
    global PROJECT_ROOT

    # click.clear()

    # Check Java installation
    click.echo("Checking Java installation...")

    if os.system("java -version") != 0:
        click.echo("Java installation not found")
        sys.exit(-1)

    click.echo("Found Java Installation")

    # Find Java Version
    # version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
    # pattern = '\"(\d+\.\d+).*\"'
    # java_version = re.search(pattern, version.decode('ascii')).groups()[0]

    # Create directories
    path = os.path.join(name, "lib")
    os.makedirs(path)

    # Download files to lib
    click.echo("Downloading dependencies...")
    wget.download('https://cs.gmu.edu/~offutt/mujava/mujava.jar', path)
    wget.download('https://cs.gmu.edu/~offutt/mujava/openjava.jar', path)
    wget.download('https://www.dropbox.com/s/nj0veull02w3eq4/tools.jar?dl=1', path)
    wget.download('https://www.dropbox.com/s/vmxf23ej5xwaqil/junit-4.jar?dl=1', path)
    wget.download('https://www.dropbox.com/s/lyfilrmr2u6jgvs/hamcrest-core-1.3.jar?dl=1', path)

    # Create config file in project root
    dir_path = os.getcwd()
    project_root = os.path.join(dir_path, name)
    config = os.path.join(name, 'mujava.config')

    with open(config, 'w') as f:
        f.write('MuJava_HOME=' + project_root)

    PROJECT_ROOT = project_root

    # Make directory structure
    run_cmd('makeMuJavaStructure', True)

    click.echo("Project Initiation complete!")

    click.echo("\nRun: 'cd " + name + "' before running further commands")


@cli.command()
def generate():
    """Starts GUI to generate mutants"""

    if not is_valid_command():
        return

    click.echo("\nStarting GUI Interface")
    run_cmd('gui.GenMutantsMain')


@cli.command()
def test():
    """Starts GUI to generate mujava tests"""

    if not is_valid_command():
        return

    click.echo("\nStarting GUI Interface")
    run_cmd('gui.RunTestMain')


# @cli.command()
# def build():
#     click.echo("\nFeature not supported yet")


if __name__ == '__main__':
    cli()
