from odoo import api, fields, models


class Agama(models.Model):
    _name = 'agama'
    _description = 'Data Nilai Agama'

    peserta = fields.Many2one(comodel_name="siswa", string='Nama')
    kelas = fields.Selection(string='', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], related='peserta.kelas', store=True)
    j_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),] ,related='peserta.j_kel' ,store=True)
    total = fields.Integer(compute='_get_sum', store=True)
    rerata = fields.Float(compute='_get_avg', store=True)
    state = fields.Selection(string='State', selection=[('lulus', 'Lulus'), ('remidi', 'Remidi'),])
    
    # field ujian
    uh1 = fields.Integer(string='UH 1')
    uh2 = fields.Integer(string='UH 2')
    uh3 = fields.Integer(string='UH 3')
    uts = fields.Integer(string='UTS')
    uas = fields.Integer(string='UAS')
    
    @api.depends('uh1', 'uh2', 'uh3', 'uts', 'uas')
    def _get_sum(self):
        for rec in self:
           rec.update({
                'total': rec.uh1+rec.uh2+rec.uh3+rec.uts+rec.uas,

            })
               
    @api.depends('uh1', 'uh2', 'uh3', 'uts', 'uas')
    def _get_avg(self):
        for rec in self:
           rec.update({
                'rerata': rec.uh1+rec.uh2+rec.uh3+rec.uts+rec.uas/5,

            })         
                    
class Ipa(models.Model):
    _name = 'ipa'
    _description = 'Data Nilai IPA'

    peserta = fields.Many2one(comodel_name='siswa', string='Nama')
    kelas = fields.Selection(string='', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], related='peserta.kelas', store=True)
    j_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),] ,related='peserta.j_kel' ,store=True)
    total = fields.Integer(compute='_get_sum', store=True)
    rerata = fields.Float(compute='_get_avg', store=True)
    state = fields.Selection(string='State', selection=[('lulus', 'Lulus'), ('remidi', 'Remidi'),] , compute='htg_ujian')
    
    # field ujian
    uh1 = fields.Integer(string='UH 1')
    uh2 = fields.Integer(string='UH 2')
    uh3 = fields.Integer(string='UH 3')
    uts = fields.Integer(string='UTS')
    uas = fields.Integer(string='UAS')
    
    @api.depends('uh1', 'uh2', 'uh3', 'uts', 'uas')
    def _get_sum(self):
        for rec in self:
           rec.update({
                'total': rec.uh1+rec.uh2+rec.uh3+rec.uts+rec.uas,

            })
           
    @api.depends('uh1', 'uh2', 'uh3', 'uts', 'uas')
    def _get_avg(self):
        for rec in self:
           rec.update({
                'rerata': rec.uh1+rec.uh2+rec.uh3+rec.uts+rec.uas/5,

            })
                     
class Ips(models.Model):
    _name = 'ips'
    _description = 'Data Nilai IPS'

    peserta = fields.Many2one(comodel_name='siswa', string='Nama')
    kelas = fields.Selection(string='', selection=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], related='peserta.kelas', store=True)
    j_kel = fields.Selection(string='Jenis Kelamin', selection=[('L', 'Laki-laki'), ('P', 'Perempuan'),] ,related='peserta.j_kel' ,store=True)
    total = fields.Integer(compute='_get_sum', store=True)
    rerata = fields.Float(compute='_get_avg', store=True)
    state = fields.Selection(string='State', selection=[('lulus', 'Lulus'), ('remidi', 'Remidi'),] , compute='htg_ujian')
    
    # field ujian
    uh1 = fields.Integer(string='UH 1')
    uh2 = fields.Integer(string='UH 2')
    uh3 = fields.Integer(string='UH 3')
    uts = fields.Integer(string='UTS')
    uas = fields.Integer(string='UAS')
    
    @api.depends('uh1', 'uh2', 'uh3', 'uts', 'uas')
    def _get_sum(self):
        for rec in self:
           rec.update({
                'total': rec.uh1+rec.uh2+rec.uh3+rec.uts+rec.uas,

            })
           
    @api.depends('uh1', 'uh2', 'uh3', 'uts', 'uas')
    def _get_avg(self):
        for rec in self:
           rec.update({
                'rerata': rec.uh1+rec.uh2+rec.uh3+rec.uts+rec.uas/5,

            })

    @api.depends('state','uh1', 'uh2', 'uh3', 'uts', 'uas')
    def htg_ujian(self):
        for rec in self:
            if rec.rerata >= 300.00:
                return self.write({'state': 'lulus'}) 
            if rec.rerata <= 300.00:
                return self.write({'state': 'remidi'}) 
    
    # @api.depends('state')
    # def htg_ujian(self):
    #     for rec in self:
    #         if self.rerata > 300.00:
    #             return self.write({'state': 'lulus'})   
    
    # @api.depends('state')
    # def htg_ujian(self):
    #     if self.rerata > 300.00:
    #         return self.write({'state': 'remidi'})      
    
                     
    # @api.depends('state','uh1', 'uh2', 'uh3', 'uts', 'uas')
    # def htg_ujian(self):  
    #     for rec in self:
    #         if rec.rerata > 300.00:
    #             return self.write({'state': 'lulus'}) 
    #         if rec.rerata < 300.00:
    #             return self.write({'state': 'remidi'}) 