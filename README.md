# mzXMLConverter
This repository contains a script for converting mzXML files to a CSV file
with only the m/z values and intensity values.

## Installation
Create a virtual environment:
```shell
python -m venv venv
```

Install packages:

On Linux / MacOS:
```shell
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

On Windows:
```shell
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```


## Generating an packaged executable
We generate a console executable version of the script using pyinstaller.
Run this command on the type of OS you want to support:
```shell
source venv/bin/activate
pyinstaller --console mzxmlconverter.py
```
or
```shell
source venv/bin/activate
pyinstaller --console --onefile mzxmlconverter.py
```


Then distribute the content from the dist directory.


## Usage of the script
Start by downloading the release package for your operating system
from [Releases](https://github.com/NHMDenmark/mzXMLConverter/releases).
Then unpack it somewhere appropriate on your computer.

For Windows there are two release zip archives: mzxmlconverter.zip 
the program in a folder together with a lot of necessary extra files.
mzxmlconverter_onefile.zip contains one file called mzxmlconverter.exe 
with everything needed pack into a single file. Both works.

WARNING: On Windows running either package is super slow because
of a antimalware scan everytime the program starts.

### MacOS
Open a terminal window and start by executing the command
```shell
export PATH=$PATH:/your_path_to/mzxmlconverter/
```
Now you can execute the program in the same terminal window by
```shell
mzxmlconverter -i path_to_file.mzXML -o path_to_output_directory
```

### Windows
Open a terminal window and change into the directory where you 
installed the program
```shell
cd your_path_to\mzxmlconverter.exe
```
Now you can execute the program in the same terminal window by
```shell
mzxmlconverter -i path_to_file.mzXML -o path_to_output_directory
```


