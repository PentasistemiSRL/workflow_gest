#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
		
class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('wf02_codworkflow')
        r.fieldcell('wf02_desworkflow')
        r.fieldcell('wf02_durata')

    def th_order(self):
        return 'wf02_codworkflow'

    def th_query(self):
        return dict(column='wf02_codworkflow', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('wf02_codworkflow')
        fb.field('wf02_desworkflow')
        fb.field('wf02_durata')
        center = bc.contentPane(region='center')
        center.inlineTableHandler(relation='@fasi_workflow',viewResource='ViewFromWF')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
