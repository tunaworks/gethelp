# gethelp

Writes module's help() as .txt files into the current directory:

By default, docs will be stored in ```sys.path[0]/readme``` 

Example:
```
from gethelp import helpdoc
import somemodule

helpdoc(somemodule)

```


Subfolders will be created if additional modules are present.
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
