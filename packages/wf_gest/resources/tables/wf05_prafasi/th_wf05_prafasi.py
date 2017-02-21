#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class ViewFromPRA(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('wf05_progr',edit=True)
        r.fieldcell('wf05_regolafase_wf01',edit=True)
        r.fieldcell('wf05_operatore',edit=True)
        r.fieldcell('wf05_dataapertura',edit=True)
        r.fieldcell('wf05_datachiusura',edit=True)
        r.fieldcell('wf05_operatorechiu', condition="$tb03_firma = 'S'",edit=True)

    def th_order(self):
        return 'wf05_progr'
		
class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('wf05_pratica_wf04')
        r.fieldcell('wf05_progr')
        r.fieldcell('wf05_regolafase_wf01')
        r.fieldcell('wf05_operatore')
        r.fieldcell('wf05_dataapertura')
        r.fieldcell('wf05_datachiusura')
        r.fieldcell('wf05_operatorechiu')

    def th_order(self):
        return 'wf05_pratica_wf04'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('wf05_pratica_wf04')
        fb.field('wf05_progr')
        fb.field('wf05_regolafase_wf01')
        fb.field('wf05_operatore')
        fb.field('wf05_dataapertura')
        fb.field('wf05_datachiusura')
        fb.field('wf05_operatorechiu')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
