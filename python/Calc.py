class calculator:
    def calc_add(self,a,b):
        if type(a)==str or type(b)==str:
            raise TypeError("can't add str")
        else:
            return a+b

    def calc_sub(self,a,b):
        return a-b

    def calc_div(self,a,b):
        return round(a/b,3)

    def calc_mul(self, a, b):
        if type(a)==str or type(b)==str:
            raise TypeError("can't mul str")
        else:
            return a*b



# c=calculator()
# c.calc_div(1,0)
