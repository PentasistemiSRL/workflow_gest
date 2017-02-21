# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('tb01_settori',pkey='id',name_long='Tabella Settori',name_plural='settori',caption_field='descsettore',lookup=True)
        self.sysFields(tbl)
        tbl.column('tb01_descsettore',size='40',name_long='descsettore',name_short='descset')
