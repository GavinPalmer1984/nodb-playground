# nodb-playground
building learning tests for nodb

## setup

```
git clone git@github.com:heroLFG/nodb-playground.git
cd nodb-playground
virtualenv .virtual

# windows:
.virtual/Scripts/activate.bat
linux:
source .virtual/Scripts/activate

pip install -r requirements.txt
python -m unittest discover
```
