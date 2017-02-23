#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='wf_gest package',sqlschema='wf_gest',sqlprefix=True,
                    name_short='Wf_gest', name_long='WorkFlow_Gest', name_full='Wf_gest')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
    