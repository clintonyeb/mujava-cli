# MuJava Command Line Tool

This is a simple-wrapper for the mujava project [MuJava](https://cs.gmu.edu/~offutt/mujava/), which does all the necessary configurations for you.

(Video Here)


## Downloads

### Windows:
Download exe file: [MuJava Exe Download](https://www.dropbox.com/s/d266k0l4cmgqz97/mujava.exe?dl=1)

### Linux/Mac:


## Installation

### Requirements:
Java 8+: Make sure you have a valid installation of Java8 or a newer version.

### Windows:
Run the downloaded installer to install `mujava-cli on your system` You will require admin access since the `cli` modifies the system `Path` variable so that it can be used the the cmd.

After installation, you can access the cli from the `cmd` prompt as `mujava`.


For help with `mujava`:

```
mujava --help
```


## How To Use
Commands:
1. Create a new Project with name <project_name>:
  `mujava init <project_name>`:      Initializes new mujava project with given name.
  
2. Start GUI to generate mutants:
  `mujava generate`:  Starts GUI to generate mutants.
 
3. Start GUI to genertae mutant tests: 
  `mujava test`:      Starts GUI to generate mutant tests.
  

## How It Works
The CLI (Command Line Interface) is a simple wrapper for the MuJava Library that automates most of the configuration that must be done to be able to use the library. It is written in python.


## Future Work
Add a command to compile src files to corrresponding classes folder.
