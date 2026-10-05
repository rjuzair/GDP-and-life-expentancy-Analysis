"""Medical insurance records - core Python data structures.

Builds and queries patient insurance records using dictionaries,
dictionary comprehensions and nested dictionaries (no external libraries).
"""


def main():
    medical_costs = {"Marina": 6607.0, "Vinay": 3225.0}
    medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
    medical_costs["Vinay"] = 3325.0  # corrected record
    print(medical_costs)

    average_cost = sum(medical_costs.values()) / len(medical_costs)
    print(f"Average insurance cost: ${average_cost:,.2f}")

    names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
    ages = [27, 24, 43, 35, 52]
    names_to_ages = dict(zip(names, ages))
    print(f"Marina's age is {names_to_ages.get('Marina')}")

    medical_records = {
        "Marina": {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0},
        "Vinay": {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0},
        "Connie": {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0},
        "Isaac": {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0},
        "Valentina": {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0},
    }
    print(f"Connie's insurance cost is ${medical_records['Connie']['Insurance_cost']:,.2f}")

    medical_records.pop("Vinay")

    for name, record in medical_records.items():
        print(f"{name} is a {record['Age']} year old {record['Sex']} {record['Smoker'].lower()} "
              f"with a BMI of {record['BMI']} and an insurance cost of ${record['Insurance_cost']:,.2f}")

    smokers = [n for n, r in medical_records.items() if r["Smoker"] == "Smoker"]
    print(f"Smokers: {smokers}")


if __name__ == "__main__":
    main()
