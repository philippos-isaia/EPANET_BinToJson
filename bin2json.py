#!/usr/bin/env python
from __future__ import print_function

from outbin import EpanetOutBin

# Create binary file
import epamodule as em
def out(s):
  print (s.decode())

net = "Water"
nomeinp = b'Water.inp'
nomeout = b'Water.txt'
nomebin = b'Water.bin'
em.ENepanet(nomeinp, nomeout, nomebin, vfunc=out)

#em.LoadInpFile(nomeinp, nomeout, nomebin)

sim_dur = '24:00' #em.getTimeSimulationDuration()
rep_step = '0:05' #em.getTimeHydraulicStep()
qual_step = '0:05' #em.getTimeQualityStep()
#print 'Pattern step: %s'%d.getTimePatternStep()
#print 'Pattern start: %s'%d.getTimePatternStart()
#print 'Report step: %s'%d.getTimeReportingStep()
#print 'Report start: %s'%d.getTimeReportingStart()
#print 'Rule step: %s'%d.getTimeRuleControlStep()
#print 'Number of reporting periods saved to the binary: %s'%d.getTimeReportingPeriods()
#print 'Statistic type code: %s'%d.getTimeStatisticsCode()
#print 'Statistic type: %s'%d.getTimeStatisticsType()

import readEpanetFile as d
d.LoadFile(net + '.inp')
d.BinUpdateClass()
nodeNameIDs = d.getBinNodeNameID()
linkNameIDs = d.getBinLinkNameID()

with EpanetOutBin(net + ".bin") as a:
   print(a._Nlinks)
   print(a._Nnodes)
   print(a._Nperiods)
   print(a._Npumps)
   print(a._Ntanks)
   print(a._Nvalves)
   print(a.bulk_rrate)
   print(a.chemicalname)
   print(a.chemicalunits)
   print(a.dynamic_start)
   print(a.dynamic_step)
   print(a.energy)
   print(a.energy_start)
   print(a.epilog_start)
   print(a.filename)
   print(a.flowunits)
   print(a.inputfilename)
   print(a.links) # 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
   print(a.nodes) #  'demand', 'head', 'nodetype', 'ordinal', 'outfile', 'pressure', 'quality'
   print(a.pressureunits)
   print(a.prolog_start)
   print(a.quality)
   print(a.source_inflowrate)
   print(a.tank_rrate)
   print(a.title)
   print(a.tracenode)
   print(a.wall_rrate)

   import json
   data = {}
   data['NodeID'] = {}
   data['NodeType'] = {}
   data['NodeDemand'] = {}
   data['NodeHead'] = {}
   data['NodePressure'] = {}
   data['NodeQuality'] = {}
   for i, id in enumerate(nodeNameIDs):
      data['NodeID'][i] = a.nodes[id].ID
      data['NodeType'][i] = a.nodes[id]._type
      data['NodeDemand'][i] = a.nodes[id].demand
      data['NodeHead'][i] = a.nodes[id].head
      data['NodePressure'][i] = a.nodes[id].pressure
      data['NodeQuality'][i] = a.nodes[id].quality

   data['LinkID'] = {}
   data['LinkType'] = {}
   data['LinkFriction'] = {}
   data['LinkHeadLoss'] = {}
   data['LinkQuality'] = {}
   data['LinkReactionRate'] = {}
   data['LinkSetting'] = {}
   data['LinkStatus'] = {}
   data['LinkVelocity'] = {}
   for i, id in enumerate(linkNameIDs):
      data['LinkID'][i] = a.links[id].ID
      data['LinkType'][i] = a.links[id].linktype
      data['LinkFriction'][i] = a.links[id].friction
      data['LinkHeadLoss'][i] = a.links[id].headloss
      data['LinkQuality'][i] = a.links[id].quality
      data['LinkReactionRate'][i] = a.links[id].reactionrate
      data['LinkSetting'][i] = a.links[id].setting
      data['LinkStatus'][i] = a.links[id].status
      data['LinkVelocity'][i] = a.links[id].velocity

   data['CountLinks'] = a._Nlinks
   data['CountNodes'] = a._Nnodes
   data['CountTanks'] = a._Ntanks
   data['CountPumps'] = a._Npumps
   data['CountValves'] = a._Nvalves
   data['BulkRate'] = a.bulk_rrate
   data['ChemicalName'] = a.chemicalname
   data['Periods'] = a._Nperiods
   data['ChemicalUnits'] = a.chemicalunits
   data['DynamicStart'] = a.dynamic_start
   data['DynamicStep'] = a.dynamic_step
   data['Energy'] = a.energy
   data['EnergyStart'] = a.energy_start
   data['EpilogStart'] = a.epilog_start
   data['Filename'] = a.filename
   data['FlowUnits'] = a.flowunits
   data['InputFilename'] = a.inputfilename
   data['PressureUnits'] = a.pressureunits
   data['PrologStart'] = a.prolog_start
   data['Quality'] = a.quality
   data['SourceFlowRate'] = a.source_inflowrate
   data['TankRate'] = a.tank_rrate
   data['Title'] = a.title
   data['TraceNode'] = a.tracenode
   data['WallRate'] = a.wall_rrate
   data['SimDuration'] = sim_dur
   data['RepStep'] = rep_step
   data['QualStep'] = qual_step
   json_data = json.dumps(data)
   #print(json_data)
   with open(net+"_bin.json", "w") as write_file:
      json.dump(data, write_file)

print('finish')