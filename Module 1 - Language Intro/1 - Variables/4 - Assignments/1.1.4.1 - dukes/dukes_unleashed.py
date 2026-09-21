"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

JMU 2022-2023 Annual:
In-state total cost: 30792 USD
Out-of-state total cost: 47882 USD

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
import math

#create a function to calculate the amount of money needed to generate the tuition costs 
# at a 5% return from in state and out-of-state tuition costs
def calculate_gift(in_state_tuition, out_state_tuition):
    in_state_gift1 = in_state_tuition / 0.05
    out_state_gift2 = out_state_tuition / 0.05
    return in_state_gift1, out_state_gift2
in_state_gift1, out_state_gift2 = calculate_gift(30792, 47882)
print("In-state gift needed: $", in_state_gift1)
print("Out-of-state gift needed: $", out_state_gift2)

#define the tuition costs for in-state and out-of-state students
in_state_tuition = 30792
out_state_tuition = 47882
#calculate the amount of money needed to generate the tuition costs at a 5% return
in_state_gift = in_state_tuition / 0.05
out_state_gift = out_state_tuition / 0.05
#output the results
print("In-state gift needed: $", in_state_gift)
print("Out-of-state gift needed: $", out_state_gift)

in_state_gift_final = in_state_gift

out_state_gift_final = out_state_gift
