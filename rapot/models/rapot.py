from odoo import api, fields, models,_


class Mapel(models.Model):
    _name = 'mapel'
    _description = 'Data Nilai'
    _order = 'n_agama desc, n_ipa desc, n_ips desc'
    
    rank = fields.Char(string='Rangking')
    siswa = fields.Many2one(comodel_name='siswa', string='Nama')
    kelas_id = fields.Selection(string='Kelas', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], related='siswa.kelas')
    n_agama = fields.Integer(string='Agama')
    n_ipa = fields.Integer(string='IPA')
    n_ips = fields.Integer(string='IPS')
    total = fields.Integer(compute='_get_sum', store=True)
    rerata = fields.Float(compute='_get_avg', store=True)
    
    
    @api.model
    def create(self, vals):
        if vals.get('rank', ('-')) == ('-'):
            vals['rank'] = self.env['ir.sequence'].next_by_code('mapel') or ('-')
        res = super(Mapel, self).create(vals)
        return res
    
    @api.depends('n_agama', 'n_ipa', 'n_ips')

    def _get_sum(self):
        for rec in self:
           rec.update({
                'total': rec.n_agama+rec.n_ipa+rec.n_ips,

            })
    
    @api.depends('n_agama', 'n_ipa', 'n_ips')

    def _get_avg(self):
        for rec in self:
           rec.update({
                'rerata': rec.n_agama+rec.n_ipa+rec.n_ips/3,

            })
class Siswa(models.Model):
    _name = 'siswa'
    _description = 'Data Siswa'
    _rec_name = 'nama_siswa'

    nama_siswa = fields.Char(string='Nama')
    kelas = fields.Selection(string='Kelas', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')])
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    j_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),])
    nis = fields.Char(string='NIS')
    agama = fields.Selection(string='Agama', selection=[('islam', 'Islam'), ('kristen', 'Kristen'), ('budha', 'Budha'), ('konghucu', 'Konghucu')])