# mzXMLConverter
This repository contains a script for converting mzXML files to a CSV file
with only the m/z values and intensity values.

## Installation
Create a virtual environment:
```shell
python -m venv venv
```

Install packages:
```shell
source venv/bin/activate
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
Then distribute the content from the dist directory.


## Usage of the script
Start by downloading the release package for your operating system
and unpack it somewhere appropriate on your computer.

### MacOS
Open a terminal window and start by executing the command
```shell
export PATH=$PATH:/your_path_to/mzxmlconverter
```
Now you can execute the program in the same terminal window by
```shell
mzxmlconverter -i path_to_file.mzXML -o path_to_output_directory
```

