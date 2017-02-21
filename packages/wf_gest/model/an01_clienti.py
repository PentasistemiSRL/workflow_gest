# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('an01_clienti',pkey='id',name_long='cliente',name_plural='clienti',caption_field='an01_ragsoc')
        self.sysFields(tbl)
        tbl.column('an01_ragsoc',size='40',name_long='ragionesociale',name_short='ragsoc')
        tbl.column('an01_indirizzo',size='40',name_long='indirizzo',name_short='indir')
        tbl.column('an01_comune',size='22',name_long='comune',name_short='com').relation('tb02_comuni.id',relation_name='clienti_comuni', mode='foreignkey', one_one=True)
        tbl.column('an01_tipologia',size='22',name_long='tipocliente',name_short='tipocli').relation('tb04_tipicliente.id',relation_name='clienti_tipoclienti', mode='foreignkey')
