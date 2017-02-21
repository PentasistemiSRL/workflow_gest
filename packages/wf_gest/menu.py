#!/usr/bin/python
# -*- coding: UTF-8 -*-

def config(root,application=None):
    wf_gest = root.branch('WorkFlow_Gest')
    wf_gest.lookups('Tabelle di Base',lookup_manager='wf_gest')	
    wf_gest.thpage('Archivio regole WF',table='wf_gest.wf01_wfregole')
    wf_gest.thpage('Archivio Workflow',table='wf_gest.wf02_wftesta')
    wf_gest.thpage('Anagrafica Clienti',table='wf_gest.an01_clienti')	
    wf_gest.thpage('Archivio Pratiche',table='wf_gest.wf04_pratesta')

