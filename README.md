# About

A set of python scripts to work with SAE J1708 protocol over serial port communication.

# SAE J1708

SAE J1708 protocol is used in various heavy-duty equipment (e.g., lorries, loaders, diggers, etc.) and is a simple communication protocol supporting CRC shechsum. 
Detailed description of the protocol is provided [here](https://www.kvaser.com/about-can/can-standards/j1708/).


# Protocol structure

## Message

A J1708 message example:

<table>
    <thead>
    <tr>
    <th width="12%">MID</th>
    <th width="12%">Data 1</th>
    <th width="12%">Data 2</th>
    <th width="13%">Data 3</th>
    <th width="13%">Data 4</th>
    <th width="13%">Checksum</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td width="12%">44</td>
    <td width="12%">23</td>
    <td width="12%">61</td>
    <td width="13%">114</td>
    <td width="13%">62</td>
    <td width="13%">208</td>
    </tr>
    </tbody>
</table>

## MID

The first byte in every message must always be a MID. Valid values of the MID is 0-255.


* MIDs 0-68 belong to predefined devices to ensure consistency.
* MIDs 69-86 are set aside for J1922 protocol.
* MIDs 87-110 are reserved for future applications. Manufactures may apply to SAE Truck and Bus Electrical Committee to define a MID.
MID 111 is designated for factory tests of electronic control units and shall not be used by any on-board unit.
* MIDs 112-127 are not reserved and can be used as wanted.
MIDs 128-255 are reserved for the SAE J1587 protocol, where they are defined.

## CRC

The checksum is calculated as following:

As an example (using the sample message in the figure above),

* 44+23+61+114+62+208 = 512
* (512 AND 0xFF) = 0, so the message is correct.


# Use of the scripts
## Installing Dependencies
The scripts have a number of dependencies that can be installed using 

To use the scripts the following packages are required:

* pyserial
* time
* csv
* sys
* signal
* os

To install the above-mentioned packages use the following commands:

    python -m pip install --upgrade pip
    python -m pip install pyserial

OR

Use use virtual environment instead

```
python -m venv venv #must be called only once
 .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip

```
AND
```
pip install pyserial
```
OR
```
pip install -r requirements.txt
```


## Run

To read the serial bus COM-port number has to be updated in line 46 in _j1708_com_receive.py_. It is also advisible to check *_com.baudrate_* and *_com.timeout_*

Running of the script from CLI by:

    python j1708_com_receive.py

NOTE:

Don't forget to activate the environment prior to execution by:

```
 .\venv\Scripts\Activate.ps1
 python j1708_com_receive.py
```
will result in a log file to be created in _logs/_ folder.

