# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('wf05_prafasi',pkey='id',name_long='Pratiche Fasi',name_plural='Fasi',caption_field='id')
        self.sysFields(tbl)
        tbl.column('wf05_pratica_wf04',size='22',name_long='praticarif',name_short='pratrif').relation('wf04_pratesta.id',relation_name='fasi_pratica', mode='foreignkey', onDelete='cascade')
        tbl.column('wf05_progr',dtype='I',name_long='nrriga',name_short='riga')
        tbl.column('wf05_regolafase_wf01',size='22',name_long='regolafase',name_short='regfas').relation('wf01_wfregole.id',relation_name='regfase_regolawf', mode='foreignkey', one_one=True)
        tbl.column('wf05_operatore',size='22',name_long='operatorefase',name_short='operfase').relation('tb03_operatori.id',relation_name='apepra_operatori', mode='foreignkey', one_one=True)
        tbl.column('wf05_dataapertura',dtype='D',name_long='dataapertura',name_short='dataape')
        tbl.column('wf05_datachiusura',dtype='D',name_long='datachiusura',name_short='datachiu')
        tbl.column('wf05_operatorechiu',size='22',name_long='operatorechiusura',name_short='operchiu').relation('tb03_operatori.id',relation_name='chiupra_operatori', mode='foreignkey', one_one=True)
