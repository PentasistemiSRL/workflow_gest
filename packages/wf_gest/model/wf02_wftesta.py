# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('wf02_wftesta',pkey='id',name_long='workflow',name_plural='workflows',caption_field='wf02_desworkflow')
        self.sysFields(tbl)
        tbl.column('wf02_codworkflow',size='5',name_long='codworkflow',name_short='codwf')
        tbl.column('wf02_desworkflow',size='40',name_long='desworkflow',name_short='deswf')
        tbl.column('wf02_durata',dtype='I',name_long='duratagg',name_short='durata')
