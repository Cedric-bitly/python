gross_salary = 45000

if gross_salary >= 0:
    if gross_salary < 20000:
        contribution = 500
    else:
        if gross_salary < 40000:
            contribution = 1000
        else:
            contribution = 1500
else:
    print("invalid salary")

print("Gross Salary:", gross_salary)
print("Monthly Contribution:", contribution)