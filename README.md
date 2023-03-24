# MLWebAppPortfolio
MLWebAppPortfolio: Explore diverse ML-powered web apps, learn AI-driven features integration, and get inspired. Ideal for developers and data scientists.

## MarketPulseSP500
***

### Overview

This app called "MarketPulseSP500" displays the closing price and volume of the SPY (SPDR S&P 500 ETF) over the past 10 years. The app uses the yfinance library to get the data and streamlit library to display it in a user-friendly format. The closing price and volume are presented as line charts. Users can see how the closing price and volume of the SPY has changed over time and use this information to make informed decisions about their investments.


<div style="text-align:left;">
  <img src="MarketPulseSP500/images/pic1.png" alt="Market Pulse App - Closing Price" style="width: 75%; height: 75%;" />
</div>

Image of the applications showing closing price.


<div style="text-align:left;">
  <img src="MarketPulseSP500/images/pic2.png" alt="Market Pulse App - Volume" style="width: 75%; height: 75%;" />
</div>

Image of the applications showing trading volume.


### Installation and Usage

1. Make sure you have Python, yfinance, and Streamlit installed on your machine.
2. Clone or download the MarketPulseSP500 app from the GitHub repository.
3. Open your terminal or command prompt and navigate to the directory where you saved the MarketPulseSP500 app.
4. Type streamlit run MarketPulseSP500.py and press Enter.
5. Wait for the app to load, and then explore the different features by interacting with the widgets and visualizations.

To stop the app, press Ctrl + C in the terminal or command prompt.

Enjoy using MarketPulseSP500!

## NucleoTally
***
<div style="text-align:left;">
  <img src="NucleoTally/images/dna.png" alt="dna" style="width: 75%; height: 75%;" />
</div>

### Overview
This is a web app called "NucleoTally" that helps count the number of different DNA nucleotides in a given sequence. The app is written in Python and uses libraries such as pandas, streamlit, altair, and PIL.

When the app is opened, it displays an image of a DNA molecule and asks the user to enter a DNA sequence. The user can type in the sequence or paste it in from somewhere else.

After the user enters the sequence, the app counts the number of each type of nucleotide (A, T, G, and C) and displays the results in a bar chart using the Altair library. The user can see the count of each nucleotide and the percentage of the total sequence that it represents.

Overall, this app is useful for anyone who needs to quickly and easily count the number of nucleotides in a DNA sequence.


### Installation
1. Ensure that you have Python 3 installed on your computer. You can check this by opening a terminal or command prompt and typing python3 --version. If Python 3 is not installed, download it from the official Python website: https://www.python.org/downloads/.

2/ Install the required libraries using the following command in your terminal or command prompt:
```bash
pis3 install pandas streamlit altair Pillow

```
3. Download the app code and image files from a code repository or create a new file in your preferred code editor and copy-paste the code provided.

### Usage

1. Open a terminal or command prompt and navigate to the directory where the app code is saved.

2. Start the app by running the following command:
```bash
streamlit run app.py
```

3. The app will open in your default web browser and display an image of a DNA molecule with a text box below it.

4. Enter the DNA sequence you want to analyze in the text box. You can type or paste in the sequence.

5. The app will automatically count the number of each nucleotide in the sequence and display the results in a bar chart below the input box.

6. To analyze a different sequence, simply clear the text box and enter the new sequence.

7. To stop the app, close the web browser tab or press Ctrl + C in the terminal or command prompt where the app is running.

That's it! With these steps, you can install and use the NucleoTally app to count nucleotides in any DNA sequence.





