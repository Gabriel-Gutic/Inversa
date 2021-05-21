from django import forms
from sympy import *


def modify(string: str):
    string = string.replace("**", "^")
    string = string.replace("*", "∙")
    string = string.replace("sqrt", "root")
    string = string.replace("pi", "𝜋")
    print(string)
    return string


class MatrixForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.n = kwargs.pop('n')
        super(MatrixForm, self).__init__(*args, **kwargs)
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                if j == self.n:
                    self.fields['elements_' + str(i) + '_' + str(j)] = forms.CharField(label="", max_length=30,
                                                                                       help_text=" ", initial="0")
                else:
                    self.fields['elements_' + str(i) + '_' + str(j)] = forms.CharField(label="", max_length=30,
                                                                                       initial="0")
                self.fields['elements_' + str(i) + '_' + str(j)].widget.attrs['style'] = "width:100px;"

    def GetMatrix(self):
        M = zeros(self.n, self.n)
        for i in range(self.n):
            for j in range(self.n):
                try:
                    M[i, j] = self.cleaned_data['elements_' + str(i + 1) + '_' + str(j + 1)]
                    M[i, j] = simplify(M[i, j])
                except:
                    return None
        l = list()
        for i in range(self.n):
            r = list()
            for j in range(self.n):
                s = modify(str(M[i, j]))
                r.append(s)
            l.append([r, i])
        return l

    def GetDet(self):
        M = zeros(self.n, self.n)
        for i in range(self.n):
            for j in range(self.n):
                M[i, j] = self.cleaned_data['elements_' + str(i + 1) + '_' + str(j + 1)]
                M[i, j] = simplify(M[i, j])
        return modify(str(simplify(M.det())))

    def GetInversa(self):
        M = zeros(self.n, self.n)
        for i in range(self.n):
            for j in range(self.n):
                M[i, j] = self.cleaned_data['elements_' + str(i + 1) + '_' + str(j + 1)]
                M[i, j] = simplify(M[i, j])
        if M.det() == 0:
            return None

        M = M.inv()

        l = list()
        for i in range(self.n):
            r = list()
            for j in range(self.n):
                s = modify(str(simplify(M[i, j])))
                r.append(s)
            l.append([r, i])
        return l

