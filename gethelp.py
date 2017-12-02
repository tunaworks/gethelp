#!/usr/bin/env python3

import sys, os, io, inspect, importlib, pydoc, shutil
import pkgutil as pk


def main():
    Helpdoc(twython)

def Helpdoc(module, path=sys.path[0]):


    if isinstance(module, str):
        module = __import__(module)
    for file in os.scandir(module.__path__[0]):
        if file.is_file():
            print(file.name)
    modname = module.__name__
    ipath = "".join(module.__path__)
    opath = os.path.join(path, "readme/{}".format(modname))

    classes = {}
    files = {}


    for finder,name,ispkg in pk.walk_packages(module.__path__, prefix="{}.".format(modname)):
        x = finder.find_spec(name)
        classfunc = list()
        try:
            # x.loader points to a loader object
            # loader.load_module(name) returns module <object>
            # use module as usual
            xmod = x.loader.load_module(x.name)
            for funcname,address in (inspect.getmembers(xmod, inspect.isroutine)):
               func = getattr(xmod,funcname)
               classfunc.append(func)
        except ModuleNotFoundError:
            pass

        classes[x.origin] = [x.name,classfunc]
        del classfunc


    for i in range(len(classes.keys())):

        for x,y,z in os.walk(ipath):
            i = os.path.join(x[len(ipath):]).lstrip("/")

            if x == ipath:
                try:
                    os.makedirs(opath)
                    f= open("{}/{}.txt".format(opath,modname), mode="w")
                    pydoc.doc(module, output=f)
                except FileExistsError:
                    continue
                f.close()


            for file in z:
                if file.endswith(".py"):
                    zpath = os.path.join(x + os.path.sep + file)
                    if zpath in set(classes.keys()):
                        o = opath + os.path.split(zpath[len(ipath):])[0]
                        while True:
                            try:
                                filemod = classes.get(zpath)[0]
                                filemodname = classes.get(zpath)[0].rpartition(".")[2]
                                o_mpath = o + os.path.sep + filemodname
                                os.makedirs(o_mpath)
                                    # pydoc.doc returns errors as print() not error
                                    # (Line 1617) https://github.com/python/cpython/blob/3.6/Lib/pydoc.py
                                for func in classes.get(zpath)[1]:
                                    o_fpath = o_mpath + os.path.sep + func.__name__
                                    text = inspect.getdoc(func)
                                    if text:
                                        f = open("{}.txt".format(o_fpath), "x")
                                        pydoc.doc(func, output = f)
                                        f.close()
                                        #f.write(text)

                                text = inspect.getdoc(filemod)
                                if text:
                                    f = open("{}{}{}.txt".format(\
                                    o_mpath,os.path.sep,filemodname), "x")
                                    pydoc.doc(filemod, output = f)
                                    #f.write(text)
                                    f.close()
                                break
                            except FileNotFoundError:
                                #os.makedirs(o)
                                continue
                            except FileExistsError:
                                break



    print("saved to \"{}\"".format(opath))
    sys.exit(0)

if __name__ == "__main__":
    main()

