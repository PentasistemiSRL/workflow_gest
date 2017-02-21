#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('wf01_desregola')
        r.fieldcell('wf01_blocca')
        r.fieldcell('wf01_dipende')

    def th_order(self):
        return 'wf01_desregola'

    def th_query(self):
        return dict(column='wf01_desregola', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('wf01_desregola')
        fb.field('wf01_blocca')
        fb.field('wf01_dipende')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
