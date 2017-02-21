#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('tb03_nominativo')
        r.fieldcell('tb03_firma')
        r.fieldcell('tb03_pinfirma')

    def th_order(self):
        return 'tb03_nominativo'

    def th_query(self):
        return dict(column='tb03_nominativo', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('tb03_nominativo')
        fb.field('tb03_firma')
        fb.field('tb03_pinfirma')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
