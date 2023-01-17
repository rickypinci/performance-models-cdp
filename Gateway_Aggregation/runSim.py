import os, sys
import itertools
import random
import xml.etree.ElementTree as et
from multiprocessing import Pool, Lock
import time
sys.path.insert(1, '../')
import varEnv



def genModel(idx, source, params, modelName):
	placeholderName = 'model.placeholder.jsimg'
	with open(placeholderName, 'r') as f:
		filedata = f.read()
	for s, p in zip(source, params):
		filedata = filedata.replace(s, str(p))
	filedata = filedata.replace(placeholderName, modelName)
	with open(modelName, 'w') as f:
		f.write(filedata)
			
			
def runSim(idx, source, params, outfile):
	modelName = 'model' + str(idx) + '.jsimg'
	resultName = modelName + '-result.jsim'
	genModel(idx, source, params, modelName)
	rnd = str(random.randint(0, sys.maxsize))
	cmd = 'java -cp ' + jmtpath + ' jmt.commandline.Jmt sim ' + modelName + ' -seed ' + rnd
	start_time = time.time()
	os.popen(cmd).read()
	end_time = time.time()
	collectResults(params, resultName, end_time - start_time, outfile)
	os.popen('rm ' + modelName + ' ' + resultName)
		
		
def collectResults(params, resultName, sim_time, outfile):
	tree = et.parse(resultName)
	root = tree.getroot()
	strAttrVals = ','.join([str(p) for p in params])
	for measure in root:
		dictAttrib = measure.attrib
		strAttrVals = strAttrVals + ',' + ','.join([dictAttrib['meanValue'], dictAttrib['lowerLimit'], dictAttrib['upperLimit']])
	strAttrVals = strAttrVals + ',' + str(sim_time)
	with lockWrite:
		with open(outfile, 'a') as f:
			f.write(strAttrVals + '\n')
	
		
def init(l):
    global lockWrite
    lockWrite = l		
	
	
def main():
	OUTFILE = 'multi_N25.csv'

	N_TOT = 25
	N_A = range(0, N_TOT+1, 1)
	Z_A = [100]
	Z_B = [100]
	S_A_GW = [10]
	S_B_GW = [10]
	S_A_S1 = [7]
	S_B_S1 = [18]
	S_A_S2 = [15]
	S_B_S2 = [12]
	S_A_S3 = [20]
	S_B_S3 = [5]
	
	ATTRIBUTE_NAMES = ['N_A', 'N_B', 'r_Z_A', 'r_Z_B', 'r_A_gw', 'r_B_gw', 'r_A_s1', 'r_B_s1', 'r_A_s2', 'r_B_s2', 'r_A_s3', 'r_B_s3']
	MEASURE_NAMES = ['R0', 'R0_low', 'R0_up', 'R0_A', 'R0_A_low', 'R0_A_up', 'R0_B', 'R0_B_low', 'R0_B_up', 'X0', 'X0_low', 'X0_up', 'X0_A', 'X0_A_low', 'X0_A_up', 'X0_B', 'X0_B_low', 'X0_B_up', 'Ugw', 'Ugw_low', 'Ugw_up', 'Us1', 'Us1_low', 'Us1_up', 'Us2', 'Us2_low', 'Us2_up', 'Us3', 'Us3_low', 'Us3_up', 'sim_time_sec']
	
	with open(OUTFILE, 'w') as f:
		f.write(','.join(ATTRIBUTE_NAMES) + ',' + ','.join(MEASURE_NAMES) + '\n')
	
	source = ['VAL{:03d}'.format(n) for n in range(len(ATTRIBUTE_NAMES))]
	paramsIterable = []
	for idx, vals in enumerate(list(itertools.product(N_A, Z_A, Z_B, S_A_GW, S_B_GW, S_A_S1, S_B_S1, S_A_S2, S_B_S2, S_A_S3, S_B_S3))):
		nA = vals[0]
		nB = N_TOT - nA
		rzA = 1/vals[1]
		rzB = 1/vals[2]
		rAgw = 1/vals[3]
		rBgw = 1/vals[4]
		rAs1 = 1/vals[5]
		rBs1 = 1/vals[6]
		rAs2 = 1/vals[7]
		rBs2 = 1/vals[8]
		rAs3 = 1/vals[9]
		rBs3 = 1/vals[10]
		params = [nA, nB, rzA, rzB, rAgw, rBgw, rAs1, rBs1, rAs2, rBs2, rAs3, rBs3]
		paramsIterable.append((idx, source, params, OUTFILE))
	
	l = Lock()	
	with Pool(NUM_SIM_THREADS, initializer=init, initargs=(l,)) as pool:
		pool.starmap(runSim, paramsIterable)	
	pool.close()
	pool.join()
		
		
if __name__ == '__main__':
	main()
