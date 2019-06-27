# bitcoin-ticker
A system tray app for linux that shows bitcoin's price live. (Using Binance API)  

You can change the refresh interval inside the coin.py script.  
`REFRESH_TIME = 3`  
Change the value(seconds) on the left side whatever you want. 

You can change the pair as well other than BTCUSDT.  
`EXCHANGE_API = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"`  
Change the last part after `symbol=` to what ever pair you want that is currently on binance.

## Setup
You'll need git, pip, and some dependencies installed.  
`pip install pygobject`  

### Running from Terminal
**Clone the repo**  
`git clone https://github.com/Dwyte/bitcoin-ticker.git`  
**Go the Directory**  
`cd bitcoin-ticker`  
**Run**  
`python coin.py`  

### Compile to a standalone app
**Install pyinstalller**  
`pip install pyinstaller`  
**Go to the repo directory**  
`pyinstaller --onefile coin.py`  

copy the btc.png, and paste it in the dist folder
and run the standalone app.
