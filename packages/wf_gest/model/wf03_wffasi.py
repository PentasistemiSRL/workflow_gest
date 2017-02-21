# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('wf03_wffasi',pkey='id',name_long='fase',name_plural='fasi',caption_field='id')
        self.sysFields(tbl)
        tbl.column('wf03_workflow_wf02',size='22',name_long='codworkflow',name_short='codwf').relation('wf02_wftesta.id',relation_name='fasi_workflow', mode='foreignkey', onDelete='cascade')
        tbl.column('wf03_progressivo',dtype='I',name_long='progressivo',name_short='progr')
        tbl.column('wf03_descrizione',size='40',name_long='descfase',name_short='desfase')
        tbl.column('wf03_durata',dtype='I',name_long='duratagg',name_short='durata')
        tbl.column('wf03_regola_wf01',size='22',name_long='regolaworkflow',name_short='regolawf').relation('wf01_wfregole.id',relation_name='fasi_regole', mode='foreignkey', one_one=True)
