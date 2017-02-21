#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('tb02_descomune')
        r.fieldcell('tb02_provincia')

    def th_order(self):
        return 'tb02_descomune'

    def th_query(self):
        return dict(column='tb02_descomune', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('tb02_descomune')
        fb.field('tb02_provincia')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
