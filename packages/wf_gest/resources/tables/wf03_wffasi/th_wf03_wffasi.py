#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class ViewFromWF(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('wf03_progressivo',edit=True)
        r.fieldcell('wf03_descrizione',edit=True)
        r.fieldcell('wf03_durata',edit=True)
        r.fieldcell('wf03_regola_wf01',edit=True)

    def th_order(self):
        return 'wf03_progressivo'
		
class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('wf03_workflow_wf02')
        r.fieldcell('wf03_progressivo')
        r.fieldcell('wf03_descrizione')
        r.fieldcell('wf03_durata')
        r.fieldcell('wf03_regola_wf01')

    def th_order(self):
        return 'wf03_workflow_wf02'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('wf03_workflow_wf02')
        fb.field('wf03_progressivo')
        fb.field('wf03_descrizione')
        fb.field('wf03_durata')
        fb.field('wf03_regola_wf01')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
