def combinationArray(n):
    a = []
    p = 1
    nt = (n-1)
    dt = 1
    for i in range(n-1):
        a.append(p+(nt/dt))
        p = nt/dt
        nt *= (n - 2 - i)
        dt *= (i + 2)
    a.append(1.0)
    return a

principal = float(input("Principal Amt : "))
interest_rate = float(input("Interest rate (%): ")) / 100
tenure = int(float(input("Tenure (yrs): ")) * 12)

m1 = 1.0
m2 = 0.0
muls = combinationArray(tenure)
for i in range(len(muls)):
    m1 += ((interest_rate / 12) ** (i + 1)) * muls[i]
    m2 += ((interest_rate / 12) ** i) * muls[i]

emi = principal * m1  / m2
print("EMI :", emi)
