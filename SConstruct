import excons
from excons.tools import python
import os
import sys
import shutil
import re


major = 2
minor = 0
patch = 0


env = excons.MakeBaseEnv()


defs = []
if sys.platform == "win32":
    cppflags = " /wd4100 /wd4505 /wd4701 /wd4127 /wd4189 /wd4005 /wd4510 /wd4512 /wd4610 /wd4211 /wd4702 /wd4706 /wd4310"
else:
    cppflags = " -Wno-unused-parameter"
prjs = []
customs = []


out_incdir = excons.OutputBaseDirectory() + "/include"
out_libdir = excons.OutputBaseDirectory() + "/lib/"
out_pydir = excons.OutputBaseDirectory() + "/py/"


## build
headers = excons.glob("include/medic/*")


prjs.append({"name": "medic",
             "type": "sharedlib",
             "alias": "medic-lib",
             "defs": defs,
             "cppflags": cppflags,
             "incdirs": [out_incdir],
             "srcs": excons.glob("src/medic/*.cpp"),
             "symvis": "default",
             "install": {out_incdir + "/medic": headers},
             "custom": [python.SoftRequire]})

for test in excons.glob("test/*.cpp"):
    test_base = os.path.splitext(os.path.basename(test))[0]

    prjs.append({"name": test_base,
                 "type": "testprograms",
                 "defs": defs,
                 "cppflags": cppflags,
                 "incdirs": [out_incdir],
                 "srcs": [test],
                 "libdirs": [out_libdir],
                 "libs": ["medic"],
                 "rpath": out_libdir,
                 "custom": [python.Require]})

for test_plugin in excons.glob("testPlugin/*.cpp"):
    plug_base = os.path.splitext(os.path.basename(test_plugin))[0]

    prjs.append({"name": plug_base,
                 "type": "dynamicmodule",
                 "defs": defs,
                 "cppflags": cppflags,
                 "incdirs": [out_incdir],
                 "srcs": [test_plugin],
                 "libs": ["medic"],
                 "libdirs": [out_libdir],
                 "prefix": "tester",
                 "symvis": "default",
                 "rpath": out_libdir,
                 "custom": [python.SoftRequire]})


excons.DeclareTargets(env, prjs)
