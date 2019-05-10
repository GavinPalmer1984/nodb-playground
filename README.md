# nodb-playground
building learning tests for nodb

## nodb thoughts
- only one client can write to a s3 object at a time
- many clients can read from an s3 object but may be slightly outdated

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
