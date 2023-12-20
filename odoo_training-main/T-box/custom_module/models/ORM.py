    @api.model_create_multi

    def create(self, vals):

        res = super(FirstTest,self).create(vals)

        #for v in vals:  
        #   v['amount'] = 50

        return res

    def write(self,vals):
        res = super(FirstTest,self).write(vals)
        self.amount = 30

        return res

    get_name()

    name_search()

    unlink()