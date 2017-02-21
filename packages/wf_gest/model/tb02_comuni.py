# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tb02_comuni',pkey='id',name_long='Tabella Comuni',name_plural='comuni',caption_field='tb02_descomune',lookup=True)
        self.sysFields(tbl)
        tbl.column('tb02_descomune',size='40',name_long='descomune',name_short='descom')
        tbl.column('tb02_provincia',size='2',name_long='provincia',name_short='prov')
