# Instrument Controller
A script to initialize connection with instrument using SCPI through VISA connection. 

## Method included
1. get_resource_list() -> scan & list available resource
2. open_connection(resource_id) -> connect to an instrument using resource id (VISA address)
3. query(query_str) -> write & read operation based on query SCPI commands
4. write(cmd_str) -> write operation based on SCPI commands, expect to return response
5. read() -> read response from instrument (useful for polling response)
6. query_image(cmd_str) -> read image file from instrument and create BMP image file in current directory (binary block read)

## Package used
1. PyVISA (https://pyvisa.readthedocs.io/en/latest/)

## Get started
1. Clone the repo
2. Install required python library. (pip install -r requirements.txt)
3. Import and use InstrumentController class to init connection

## Examples 

### Get available resource list for Visa connection
controller = InstrumentController()
]print(controller.get_resource_list())

### Replace 'GPIB0::14::INSTR' with your instrument's address
instrument_address = 'GPIB0::14::INSTR'

### Open connection to instrument
controller.open_connection(instrument_address)

### Example usage:
#### Query the instrument's identity
print(controller.query('*IDN?'))

#### Write a command to the instrument (replace with an actual command for your instrument)
controller.write('OPERating:FREQuency?')

#### Read the response from the instrument
print(controller.read())

#### Read image screenshot from the instrument
controller.query_image('IMAGe:DOWNload?')
