Fido3
=====

A small wrapper around the urllib3 library to ease the use 
and lessen the amount of code that needs to be written each 
time.

Methods
-------

#### GET

```python
import fido
from pprint import pprint

f = fido.Fetch()
f.get("https://httpbin.org/get")
```

Then you will be able to access the following.

```python
print(f.status)
print(f.text)
pprint(f.json())
```

#### POST

Sending data in the body, the data will automatically be json encoded.

```python
import fido
from pprint import pprint

f = fido.Fetch()
f.post("https://httpbin.org/post", body={"hello":"world"})
```

Then you will be able to access the following.

```python
print(f.status)
print(f.text)
pprint(f.json())
```

Sending form data.

```python
import fido
from pprint import pprint

f = fido.Fetch()
f.post("https://httpbin.org/post", 
        form={"username":"jsmith", "password":"abc123"})
```

Then you will be able to access the following.

```python
print(f.status)
print(f.text)
pprint(f.json())
```

