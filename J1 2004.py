def cell_sell():

    day_mins = int(input())
    eve_mins = int(input())
    wkd_mins = int(input())

    day_cost_1 = (day_mins - 100) * 0.25
    day_cost_2 = (day_mins - 250) * 0.45

    eve_cost_1 = eve_mins * 0.15
    eve_cost_2 = eve_mins * 0.35

    wkd_cost_1 = wkd_mins * 0.20
    wkd_cost_2 = wkd_mins * 0.25

    if day_cost_1 < 0:

        day_cost_1 = 0

    if day_cost_2 < 0:

        day_cost_2 = 0

    total_cost_1 = round(day_cost_1 + eve_cost_1 + wkd_cost_1, 2)
    total_cost_2 = round(day_cost_2 + eve_cost_2 + wkd_cost_2, 2)

    best_cost = "Plan A and B are the same price."

    if total_cost_1 < total_cost_2:

        best_cost = "Plan A is cheapest."

    if total_cost_2 < total_cost_1:

        best_cost = "Plan B is cheapest."

    plan_a_cost = str("Plan A costs {costA}".format(costA=total_cost_1))
    plan_b_cost = str("Plan B costs {costB}".format(costB=total_cost_2))

    print("{cost1}\n{cost2}".format(cost1=plan_a_cost, cost2=plan_b_cost))

    return best_cost


print(cell_sell())