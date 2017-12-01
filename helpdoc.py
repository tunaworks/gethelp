#!/usr/bin/env python3

import sys, os, inspect, importlib
import pkgutil as pk


def helpdoc(module):
    modname = module.__name__
    ipath = "".join(module.__path__)
    opath = os.path.join(sys.path[0], "readme/{}".format(modname))

    classes = {}
    files = {}


    for finder,name,ispkg in pk.walk_packages(module.__path__, prefix="{}.".format(modname)):
        x = finder.find_spec(name)
        classes[x.origin] = name


    for i in range(len(classes.keys())):

        for x,y,z in os.walk(ipath):
            i = os.path.join(x[len(ipath):]).lstrip("/")

            if x == ipath:
                try:
                    os.makedirs(opath)
                    sys.stdout= open("{}/{}.txt".format(opath,modname), mode="w")
                    print(help(module))
                except FileExistsError:
                    continue


            for file in z:
                if file.endswith(".py"):
                    zpath = os.path.join(x+"/" + file)
                    if zpath in set(classes.keys()):
                        o = opath + os.path.split(zpath[len(ipath):])[0]
                        while True:
                            try:
                                sys.stdout= open("{}/{}.txt"\
                                .format(o, classes.get(zpath).replace(".", "_"))\
                                , mode="x")
                                print(help(classes.get(zpath)))
                                break
                            except FileNotFoundError:
                                os.makedirs(o)
                                continue
                            except FileExistsError:
                                break

    return(0)

#if __name__ == "__main__":
    #main()

