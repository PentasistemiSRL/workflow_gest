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
                    ask=dict(title='Quante Fasi?',
                                fields=[dict(name='numero_fasi',lbl='Numero',wdg='numberTextBox'),
                                        dict(name='data_apertura',lbl='Data',wdg='dateTextBox')]),
                     action='FIRE #FORM.genera_fasi = numero_fasi',
                     style='color:red;font-size:20px;',
                     disabled='^#FORM.controller.is_newrecord',
                     hidden='^#vista_fasi.view.store?=#v && #v.len()>0')
        fb.dataRpc(None,self.creaWorkflow,pratica_id='=#FORM.pkey',n_fasi='^#FORM.genera_fasi')
					  
        center = bc.contentPane(region='center')
        center.inlineTableHandler(relation='@fasi_pratica',grid_selfDragRows=True,
                                    viewResource='ViewFromPRA',nodeId='vista_fasi')

    @public_method
    def creaWorkflow(self,pratica_id=None,n_fasi=None):
        fasi = self.db.table('wf_gest.wf05_prafasi')
        n_fasi = n_fasi or 4
        for i in range(n_fasi):
            record = dict(wf05_pratica_wf04=pratica_id,wf05_progr=i,wf05_dataapertura=self.workdate)
            fasi.insert(record)
        self.db.commit()


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
