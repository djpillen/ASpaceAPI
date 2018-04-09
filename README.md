# ArchivesSpace API wrapper

Work in progress.

## Installation

`pip install git+https://github.com/djpillen/ASpaceAPI.git`

## Use

```python
from aspaceapi import ASpaceAPIClient
aspace = ASpaceAPIClient()
aspace.get_archival_object(1234)
```