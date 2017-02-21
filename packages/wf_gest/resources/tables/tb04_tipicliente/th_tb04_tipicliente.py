#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('tb04_destipo')

    def th_order(self):
        return 'tb04_destipo'

    def th_query(self):
        return dict(column='tb04_destipo', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('tb04_destipo')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
