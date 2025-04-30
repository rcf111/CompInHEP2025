#!/usr/bin/env python

import sys
import os,re
import datetime

import hist
import dask
import awkward as ak
import hist.dask as hda
import dask_awkward as dak

from coffea import nanoevents
from coffea.nanoevents import NanoEventsFactory, NanoAODSchema
from coffea import processor
from coffea.nanoevents.methods import candidate, vector


import uproot
import matplotlib.pyplot as plt

class Analysis(processor.ProcessorABC):
    def __init__(self):
        self.histograms = {}
        self.histograms["pileup"] = (
            hda.Hist.new
            .Reg(50, 0 , 50, name="x", label="x-axis")
            .Double()
        ) 

    def process(self, events):

        muons = ak.zip(
            {
                "pt": events.Muon.pt,
                "eta": events.Muon.eta,
                "phi": events.Muon.phi,
                "mass": events.Muon.mass,
                "charge": events.Muon.charge,
            },
            with_name="PtEtaPhiMCandidate",
            behavior=candidate.behavior,
        )

        cut = (ak.num(muons) == 2) & (ak.sum(muons.charge, axis=1) == 0)
        # add first and second muon in every event together
        dimuon = muons[cut][:, 0] + muons[cut][:, 1]
        selected_events = events[events.HLT.IsoMu24 == True]

        self.histograms["pileup"].fill(x=selected_events.PV.npvs)

        out = {}
        out.update(self.histograms)
        return out

    def postprocess(self, accumulator):
        pass

def main():
    filename = "file://DYJetsToLL.root"
    events = NanoEventsFactory.from_root(
        {filename: "Events"},
        metadata={"dataset": "Pileup"},
        schemaclass=NanoAODSchema,
    ).events()
    p = Analysis()
    out = p.process(events)
    (result,) = dask.compute(out)

    with uproot.recreate("output2.root") as fOUT:
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        now = datetime.datetime.now()
        m = "produced: %s %s"%(days[now.weekday()],now)
        fOUT[f"{m}"] = ""

        for key in result.keys():
            fOUT[f"{key}"] = result[key]
    
    h = result["pileup"]
    fig, ax = plt.subplots()
    h.plot(ax=ax)
    ax.set_xlim(0, 50)
    ax.set_xlabel("Number of primary vertices")
    ax.set_ylabel("Number of events")

    plt.savefig("pileup_histogram.png")


if __name__ == "__main__":
    main()
