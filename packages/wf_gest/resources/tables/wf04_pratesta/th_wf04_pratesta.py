#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('wf04_nota')
        r.fieldcell('wf04_cliente_an01')
        r.fieldcell('wf04_workflow_wf02')
        r.fieldcell('wf04_dataapertura')
        r.fieldcell('wf04_aperturaope')
        r.fieldcell('wf04_datachiusura')
        r.fieldcell('wf04_chiusuraope')

    def th_order(self):
        return 'wf04_nota'

    def th_query(self):
        return dict(column='wf04_nota', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('wf04_nota')
        fb.field('wf04_cliente_an01',hasDownArrow=True)
        fb.field('wf04_workflow_wf02',hasDownArrow=True)
        fb.field('wf04_dataapertura')
        fb.field('wf04_aperturaope')
        fb.field('wf04_datachiusura')
        fb.field('wf04_chiusuraope', condition="$tb03_firma = 'S'",colspan=2)

        fb.button('Genera Fasi',
                     action="""var risposta = confirm("Confermi la creazione delle fasi pratica?");
                               if (risposta == true){
							     alert("Risposta Positiva")
							   } else 
							   {
							     alert("Risposta Negativa")
							   };""",
                     style='color:red;font-size:20px;')
					  
        center = bc.contentPane(region='center')
        center.inlineTableHandler(relation='@fasi_pratica',viewResource='ViewFromPRA')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
