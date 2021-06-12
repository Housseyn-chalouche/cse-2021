{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def dream_house():\n",
    "    \n",
    "    # necessary inputs\n",
    "    annual_salary = float(input('Enter your starting annual salary:\\n'))\n",
    "    portion_percentage = float(input('Enter the percent of your salary to save, as a decimal:\\n'))\n",
    "    total_cost = float(input('Enter the cost of your dream home:\\n'))\n",
    "    semi_annual_raise = float(input('Enter the semi annual raise, as a decimal:\\n'))\n",
    "    \n",
    "    portion_down_payment = 0.25*total_cost # 25% of the dream home cost\n",
    "    portion_saved = annual_salary*portion_percentage/12 #monthly saved money -it is fixed, doesn't change with time-\n",
    "    current_savings = 0 # months and asavings start from 0\n",
    "    months = 0\n",
    "    \n",
    "    while current_savings < portion_down_payment :\n",
    "        r = current_savings*0.04/12 # increamentation of profits from investements each month\n",
    "        current_savings += portion_saved + r # incrementation of savings\n",
    "        \n",
    "        months +=1 # manual incrementation of time, months\n",
    "        if months%6 == 0:\n",
    "            portion_saved += semi_annual_raise\n",
    "        \n",
    "    print('number of months: ', months)\n",
    "    \n",
    "dream_house()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
