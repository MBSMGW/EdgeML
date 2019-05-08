# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import Common

class Config:
	expBigLength = 6
	exp = "table" # "table" "math"
	codegen = "funcCall" # "funcCall" "inline"

def getAlgo():
	return Config.algo

def setAlgo(algo:str):
	Config.algo = algo

def getVersion():
	return Config.version

def setVersion(version:str):
	Config.version = version

def forFixed():
	return Config.version == Common.Version.Fixed

def forFloat():
	return Config.version == Common.Version.Float

def getTarget():
	return Config.target

def setTarget(target:str):
	Config.target = target

def forArduino():
	return Config.target == Common.Target.Arduino

def forHls():
	return Config.target == Common.Target.Hls

def forVerilog():
	return Config.target == Common.Target.Verilog

def forX86():
	return Config.target == Common.Target.X86

def getProfileLogFile():
	return Config.profileLogFile

def setProfileLogFile(file):
	Config.profileLogFile = file

def getExpBitLength():
	return Config.expBigLength

def getMaxScale():
	return Config.maxScale

def setMaxScale(x:int):
	Config.maxScale = x

def getShrType():
	# "shr" "shr+" "div" "negate"
	return "div"

def useMathExp():
	return Config.exp == "math"

def useTableExp():
	return Config.exp == "table"

def genFuncCalls():
	return Config.codegen == "funcCall"

def copy_dict(dict_src:dict, diff={}):
	dict_res = dict(dict_src)
	dict_res.update(diff)
	return dict_res

#set number of workers for FPGA sparseMUL
def setNumWorkers(WorkerThreads):
	Config.numWorkers = WorkerThreads

def getNumWorkers():
	return Config.numWorkers

# z = [y1,y2,..] = [[x1,..], [x2,..], ..] --> [x1,.., x2,.., ..]
def flatten(z:list): 
	return [x for y in z for x in y]