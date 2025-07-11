~~DUCKYSCRIPT~~ DONE!
~~- Open cmd in the background~~
~~- Curl python to temp appdata directory ~~
~~- Install python quietly via cmdline~~
  ~~- Args:~~
    ~~- /quiet~~
    ~~- TargetDir=%LocalAppData%\python1~~
    ~~- AssociateFiles=0~~
    ~~- CompileAll=1~~
    ~~- Include_doc=0~~
    ~~- Include_launcher=0~~
    ~~- Include_tcltk=0~~
    ~~- Include_test=0~~
~~- Curl the main payload.py as an innocuous "py-manager.py" into python1 folder~~
~~- Curl the autostart.bat as "explorer.bat" into autostart folder~~
~~- Exit~~

PYTHON
- Persistence: Copies itself into a few appdata directories
- Behaviour
  - Utilise input apis from windows to troll the user
    ~~- Block input~~
    - Change keyboard layout
    ~~- Send a few keystrokes~~
    - Set double click threshold to crazy high so everything become doubleclick
    - Swap mouse buttons
    - etc.etc.
  - Create annoying 'adware' (actually just cat image) popups
  - Redirects / forced rickrolls
  
~~BATCH SCRIPT~~ CANCELED - Implemented persistence via task scheduler instead
~~- Simply run the first instance of the python script it can find~~
~~- Python script should handle replacing deleted copies already.~~
