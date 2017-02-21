# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tb03_operatori',pkey='id',name_long='Tabella Operatori',name_plural='operatori',caption_field='tb03_nominativo',lookup=True)
        self.sysFields(tbl)
        tbl.column('tb03_nominativo',size='40',name_long='nominativo',name_short='nome')
        tbl.column('tb03_firma',size='1',name_long='confirma',name_short='firma')
        tbl.column('tb03_pinfirma',size='4',name_long='pinfirma',name_short='pin')
