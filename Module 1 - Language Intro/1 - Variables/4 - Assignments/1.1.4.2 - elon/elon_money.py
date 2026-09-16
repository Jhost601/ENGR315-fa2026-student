"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###
import math
#define variables for the investment
K = 33_000_000_000  # Elon's capital in USD
R_10 = 3.96  # 10-year bond rate
R_20 = 4.32  # 20-year bond rate
N_10 = 10  # 10-year period
N_20 = 20  # 20-year period
grwth_factor_10 = 1 + (R_10 / 100)  # growth factor for 10-year bond
grwth_factor_20 = 1 + (R_20 / 100)  # growth factor for 20-year bond
#taking the growth factor to the power of the number of years and multiplying by the initial capital
ten_year_final = K * (grwth_factor_10 ** N_10)
twenty_year_final = K * (grwth_factor_20 ** N_20)
#printing the final results
print(f"${ten_year_final}")
print(f"${twenty_year_final}")
# final answer for 10-year
ten_year_final = 48660509081.78675
# final answer for 20-year
twenty_year_final =76889229275.98897