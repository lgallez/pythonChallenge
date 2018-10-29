{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# First we'll import the os module\n",
    "import os\n",
    "# Module for reading CSV files\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "csvpath = os.path.join('..', '..', 'gitlab-data-analytics', '02-Homework', '03-Python', 'Instructions','PyBank','Resources', 'budget_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Method 1: Plain Reading of CSV files\n",
    "with open(csvpath, newline=\"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    next(csvreader)\n",
    "    Data = list (csvreader)\n",
    "    rowlength = (len(Data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-9-c1e8d246b161>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-9-c1e8d246b161>\"\u001b[0;36m, line \u001b[0;32m3\u001b[0m\n\u001b[0;31m    newCol = csv.writer(csvfile)\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    " csvreader[\"New Col\"] = csvreader[\"Profit/Losses\"]\n",
    "\n",
    "    newCol = csv.writer(csvfile)\n",
    "    month = 0\n",
    "    pnl = 0\n",
    "    change = 0.0\n",
    "    greatI = 0\n",
    "    greatD = 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pnl' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-10-768c38da05ee>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mData\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m       \u001b[0mpnl\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpnl\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mfloat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m       \u001b[0mmonth\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mData\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m       \u001b[0mnewCol\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mData\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Change'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'pnl' is not defined"
     ]
    }
   ],
   "source": [
    "  for row in Data:\n",
    "        pnl = pnl + float(row[1])\n",
    "        month = len(Data)\n",
    "\n",
    "        newCol.Data(row+['Change'])\n",
    "        next(csvreader)\n",
    "        change = (row[2] - row[1])\n",
    "        \n",
    "        #greatI = max(greatI, value)\n",
    "        #greatD = min(greatD, value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              PyBank Summary\n",
      "-------------------------------------------\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'month' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-11-0db50428c9b9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"              PyBank Summary\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"-------------------------------------------\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Total Months:                \"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmonth\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Profit / Loss:               \"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpnl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Avg Change in Profit:        \"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mchange\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'month' is not defined"
     ]
    }
   ],
   "source": [
    "#Print summary\n",
    "print(\"              PyBank Summary\")\n",
    "print(\"-------------------------------------------\")\n",
    "print(\"Total Months:                \" + str(month))\n",
    "print(\"Profit / Loss:               \" + str(pnl))\n",
    "print(\"Avg Change in Profit:        \" + str(change))\n",
    "#print(\"Greatest Increase:           \" + str(greatI))\n",
    "#print(\"Greatest Decrease:           \" + str(greatD))\n",
    "print(\"-------------------------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
