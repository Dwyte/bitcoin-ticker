# bitcoin-ticker
A system tray app for linux that shows bitcoin's price live.  
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
