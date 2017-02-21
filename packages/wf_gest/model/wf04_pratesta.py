# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('wf04_pratesta',pkey='id',name_long='Archivio Pratiche',name_plural='pratiche',caption_field='wf04_nota')
        self.sysFields(tbl)
        tbl.column('wf04_nota',size='40',name_long='NotaPratica',name_short='nota')
        tbl.column('wf04_cliente_an01',size='22',name_long='ClientePratica',name_short='cliprat').relation('an01_clienti.id',relation_name='pratica_clienti', mode='foreignkey', one_one=True)
        tbl.column('wf04_workflow_wf02',size='22',name_long='WorkFlowPratica',name_short='wfprat').relation('wf02_wftesta.id',relation_name='pratica_workflow', mode='foreignkey', one_one=True)
        tbl.column('wf04_dataapertura',dtype='D',name_long='DataApertura',name_short='dataape')
        tbl.column('wf04_aperturaope',size='22',name_long='OperatoreApertura',name_short='operape').relation('tb03_operatori.id',relation_name='apertura_operatori', mode='foreignkey', one_one=True)
        tbl.column('wf04_datachiusura',dtype='D',name_long='DataChiusura',name_short='datachiu')
        tbl.column('wf04_chiusuraope',size='22',name_long='OperatoreChiusura',name_short='operachiu').relation('tb03_operatori.id',relation_name='chiusura_operatori', mode='foreignkey', one_one=True)
