# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tb04_tipicliente',pkey='id',name_long='Tabella Tipi Cliente',name_plural='tipicliente',caption_field='tb04_destipo',lookup=True)
        self.sysFields(tbl)
        tbl.column('tb04_destipo',size='40',name_long='tipocliente',name_short='tipocli')
