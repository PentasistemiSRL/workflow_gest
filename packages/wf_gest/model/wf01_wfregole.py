# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('wf01_wfregole',pkey='id',name_long='regola',name_plural='regole',caption_field='wf01_desregola')
        self.sysFields(tbl)
        tbl.column('wf01_desregola',size='40',name_long='desregola',name_short='desreg')
        tbl.column('wf01_blocca',size='1',name_long='bloccascad (S/N)',name_short='bloccascad')
        tbl.column('wf01_dipende',size='1',name_long='dipende (S/N)',name_short='dipende')
