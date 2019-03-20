import decimal
print(decimal.Decimal(0.1))
print(decimal.Decimal(0.1)+decimal.Decimal(0.2))
print(decimal.Decimal('0.1')+decimal.Decimal('0.2'))

import fractions
print(fractions.Fraction(1.5))
print(fractions.Fraction(1,3))
print(fractions.Fraction(1.1))
print(fractions.Fraction('1.1'))