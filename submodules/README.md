# DataConda Submodules

Using DataConda submodules reduces dependencies, making it much easier to use parts of DataConda

## Submodules

* [DataConda charts](dataconda_charts.py)
  * Dependencies
    * matplotlib
    * tkinter
* [DataConda WebServers](dataconda_web.py)
  * Dependencies
    * flask
    * bs4 (BeautifulSoup)
    * requests
* [DataConda Mutables](dataconda_mutable.py)
  * No dependencies
* [DataConda Sqlite](dataconda_sqlite.py)
  * Dependencies
    * sqlite3
    
## Usage

### Make module usable
Put the downloaded dataconda submodule in the project folder

### Import
Use `import something` or `import something as something` syntax, do not use `from something import something` syntax

#### Example
```python
import dataconda_web as dcw
```
or
```python
import dataconda_sqlite as dcs
```
or
```python
import dataconda_mutable as dcm
```
or
```python
import dataconda_charts as dcc
```
