#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('an01_ragsoc')
        r.fieldcell('an01_indirizzo')
        r.fieldcell('an01_comune')
        r.fieldcell('an01_tipologia')

    def th_order(self):
        return 'an01_ragsoc'

    def th_query(self):
        return dict(column='an01_ragsoc', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('an01_ragsoc')
        fb.field('an01_indirizzo')
        fb.field('an01_comune')
        fb.field('an01_tipologia',colspan=2,width='100%',tag='checkboxtext',table='wf_gest.tb04_tipicliente',popup=True)


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
