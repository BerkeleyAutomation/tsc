import numpy as np
np.seterr(divide='ignore') # these warnings are usually harmless for this code
from matplotlib import pyplot as plt
import copy, os
from generate.TrajectoryDataGenerator import *
from tsc.tsc import TransitionStateClustering
from alternates.clustering import TimeVaryingGaussianMixtureModel, HMMGaussianMixtureModel, CoresetSegmentation
from alternates.bayes import HiddenSemiMarkovModel, AutoregressiveMarkovModel
from alternates.em import EMForwardBackward
from evaluation.Evaluator import *
from evaluation.Metrics import *

#creates a system whose regimes are uniformly sampled from the stochastic params

"""
sys = createNewDemonstrationSystem(k=3,dims=2, observation=[0.1,0.1], resonance=[0.0,0.0], drift=[0.0,0.0])
t = sampleDemonstrationFromSystem(sys,np.ones((2,1)),lm=0.0, dp=0.0)
t2 = sampleDemonstrationFromSystem(sys,np.ones((2,1)),lm=0.0, dp=0.0)
t3 = sampleDemonstrationFromSystem(sys,np.ones((2,1)),lm=0.0, dp=0.0)


a.addDemonstration(t[0])
a.addDemonstration(t2[0])
a.addDemonstration(t3[0])
a.fit()
print a.segmentation
"""

sys_params = {'k':3,'dims':2, 'observation':[0.0,0.1], 'resonance':[0.0,0.0], 'drift':[0,0.0]}

a = TransitionStateClustering(window_size=3, normalize=False, pruning=0.3,delta=-1)
#b = TimeVaryingGaussianMixtureModel(hard_param=3)
#c = HMMGaussianMixtureModel(n_components=3)
#d = CoresetSegmentation(n_components=4)
b = EMForwardBackward(n_components=3)
#f = AutoregressiveMarkovModel()


"""
plotY1Y2(run_sweep_experiment(sys_params, 'observation', [0.1, 0.25, 0.5, 0.75, 1], [a, b], np.ones((2,1)), lambda x,y: evaluate(x,y,'jaccard', thresh=0.75), N=10, k=10),
             "(A) HF Observation Noise",
             "HF Noise",
             "Segment Accuracy",
             legend=["GMM-TSC", "EM-TSC"],
             loc = 'lower left',
             filename="output1.png",
             ylim=0.0,
             xlim=0.1)
"""


plotY1Y2(run_sweep_experiment(sys_params, 'resonance', [0.1, 0.5, 1.0, 1.5, 2], [a, b], np.ones((2,1)), lambda x,y: evaluate(x,y,'jaccard', thresh=0.75), N=10, k=10),
             "(B) LF Observation Noise",
             "LF Noise",
             "Segment Accuracy",
             legend=["GMM-TSC", "EM-TSC"],
             loc = 'lower left',
             filename="output2.png",
             ylim=0.0,
             xlim=0.1)

"""
plotY1Y2(run_sweep_experiment(sys_params, 'resonance', [0.1, 0.25, 0.5, 0.75, 1], [a,b,c,d,e,f], np.ones((2,1)), lambda x,y: evaluate(x,y,'seg_acc', thresh=0.75), N=2, k=10),
             "(B) LF Process Noise",
             "LF Noise",
             "Segment Accuracy",
             legend=["TSC", "GMM", "GMM+HMM", "Coreset", "HSMM", "ARHMM"],
             loc = 'lower left',
             filename="output2.png",
             ylim=0.0,
             xlim=0.1)
"""


"""
plotY1Y2(run_sweep_experiment(sys_params, 'observation', [0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1], [a,b,c,d,e,f], np.ones((2,1)), lambda x,y: evaluate(x,y,'frame_acc'), N=2, k=10),
             "(B) HF Observation Noise",
             "HF Noise",
             "Frame Accuracy",
             legend=["TSC", "GMM", "GMM+HMM", "Coreset", "HSMM", "ARHMM"],
             loc = 'lower left',
             filename="output1b.png",
             ylim=0.0,
             xlim=0.1)
"""

"""
plotY1Y2(run_sweep_experiment(sys_params, 'resonance', [0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1], [a,b,c,d,e,f], np.ones((2,1)), lambda x,y: evaluate(x,y,'frame_acc'), N=2, k=10),
             "(D) LF Process Noise",
             "LF Noise",
             "Frame Accuracy",
             legend=["TSC", "GMM", "GMM+HMM", "Coreset", "HSMM", "ARHMM"],
             loc = 'lower left',
             filename="output2b.png",
             ylim=0.0,
             xlim=0.1)
"""

#plotData(t[0])

#
#lm is the mean number of loops, dp is the probability of "missing"
#t = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)
#u = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)
#v = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)
#w = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)
#x = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)


#0.3 o,  0.3, 3 r
"""
a = TransitionStateClustering(window_size=3, normalize=False, pruning=0.3,delta=-1)
b = TimeVaryingGaussianMixtureModel(hard_param=3)
c = HMMGaussianMixtureModel(n_components=3)
d = CoresetSegmentation(n_components=4)
e = HiddenSemiMarkovModel()
f = AutoregressiveMarkovModel()

plotY1Y2(run_sweep_experiment(sys_params, 'resonance', [0.01, 0.25, 0.5, 1, 2], [a,b,c,d,e,f], np.ones((2,1)), jaccard, N=5, k=5),
             "LF Noise vs. Jaccard",
             "LF Noise",
             "Jaccard",
             legend=["TSC", "GMM", "GMM+HMM", "Coreset", "HSMM", "ARHMM"],
             loc = 'title',
             filename="output2.png",
             ylim=0.0,
             xlim=0.1)
"""

"""
a = TransitionStateClustering(window_size=2, normalize=False, pruning=0.2,delta=-1)
b = TransitionStateClustering(window_size=2, normalize=False, pruning=0.4,delta=-1)
c = TransitionStateClustering(window_size=2, normalize=False, pruning=0.6,delta=-1)
d = TransitionStateClustering(window_size=2, normalize=False, pruning=0.8,delta=-1)
e = TransitionStateClustering(window_size=2, normalize=False, pruning=1.0,delta=-1)

plotY1Y2(run_sweep_experiment(sys_params, 'observation', [0.1, 0.2, 0.5, 0.75, 1, 1.5], [a,b,c,d,e], np.ones((2,1)), jaccard, N=5, k=20),
             "LF Noise vs. Jaccard",
             "LF Noise",
             "Jaccard",
             legend=["TSC (p=0.2)", "TSC (p=0.4)", "TSC (p=0.6)", "TSC (p=0.8)", "TSC (p=1.0)"],
             loc = 'title',
             filename="output5.png",
             ylim=0.0,
             xlim=0.1)
"""




"""
a = TimeVaryingGaussianMixtureModel()
#t = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)
#plotData(t)
for i in range(0,20):
	t = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)
	a.addDemonstration(np.squeeze(t))

a.fit(hard_param = 3)
print a.segmentation
"""


"""
a = HMMGaussianMixtureModel()
#t = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)
#plotData(t)
for i in range(0,20):
	t = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)
	a.addDemonstration(np.squeeze(t))

a.fit(n_components = 4)
print a.segmentation
"""

"""
a = CoresetSegmentation()
for i in range(0,20):
	t = sampleDemonstrationFromSystem(sys,np.ones((2,1)), lm=0, dp=0)
	a.addDemonstration(np.squeeze(t))
a.fit(n_components = 2)
print a.segmentation
"""

#from alternates.coreset import *
#print coreset.get_coreset(np.squeeze(t),3,3)


