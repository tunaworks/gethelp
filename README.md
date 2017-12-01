# gethelp

Writes module's help() as .txt files into the current directory (or wherever you want).

By default, docs will be stored in ```sys.path[0]/readme``` .

**Example:**
```
from gethelp import Helpdoc
import somemodule

Helpdoc(somemodule)

```


subfolders will be created if additional modules are present.
```
~/workspace/$ ls -R -1 readme

readme:
somemodule/

readme/somemodule:
api/
somemodule.txt
somemodule_helpers.txt

readme/somemodule/api:
somemodule_api.txt

```


## Usage
**As module**:
```
from gethelp import Helpdoc as h
import somemodule

h(somemodule)
```

**As standalone**
```
$cd ~/path
$from gethelp import Helpdoc as h 
$import somemodule
$h.(somemodule)
```
