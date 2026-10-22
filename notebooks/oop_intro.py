# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Object oriented programming

# %%
class Car:

    name: str

    def __init__(self, name):

        if not isinstance(name, str):
            raise ValueError('Attribute name should have type str')

        if not name:
            self.name = 'Mercedes'
        else:
            self.name = name

    def which_country(self):

        match self.name:
            case 'Peugeot':
                return 'France'
            case 'Volkswagen' | 'Mercedes':
                return 'Germany'
        


class MyCar:
    pass



# %%
car1 = Car('Peugeot')
car2 = Car('Volkswagen')

# %%
car1.which_country()

# %%
car2.which_country()


# %% [markdown]
# ## Complex numbers

# %%
class ComplexNumber:
    real: float
    imag: float

    def __init__(self, real, imag):

        # Correctness check
        for name, variable in zip(('real', 'imag'), (real, imag)):
            try:
                variable = float(variable)
                exec(f'{name} = {variable}')
            except ValueError:
                raise ValueError(f'Attribute {name} should be convertible to float')

        self.real = real
        self.imag = imag

    def __eq__(self, other):

        return (self.real, self.imag) == (other.real, other.imag)

    def __add__(self, other):

        real = self.real + other.real
        imag = self.imag + other.imag

        return ComplexNumber(real, imag)

    def __repr__(self):
        return f'ComplexNumber({self.real}, {self.imag})'

    def __str__(self):
        return f'{self.real} + i*{self.imag}'
    


# %%
z1 = ComplexNumber(2.0, 3.0)

# %%
z2 = ComplexNumber(2, 3)

# %%
z1 == z2

# %%
z1 + z2

# %%
print(z1+z2)

# %%
print(ComplexNumber(1, -1))

# %%

# %%
print(ComplexNumber(0, 1))

# %%

# %%

# %%
w = z1 + z2

# %%
w.real, w.imag

# %%
z1.real == z2.real, z2.imag == z2.imag

# %%

# %%
z1.calculate() == z2.calculate()

# %%
z1.calculate()

# %%

# %%

# %%
x1 = (2, 3)

# %%
x2 = (2, 3)

# %%
x1 == x2

# %%

# %%

# %%

# %%

# %%
