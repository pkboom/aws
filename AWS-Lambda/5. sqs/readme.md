<img src="doc/sqs1.png" />
<img src="doc/sqs2.png" />
<img src="doc/sqs3.png" />
<img src="doc/sqs4.png" />
<img src="doc/sqs7.png" />
<img src="doc/sqs5.png" />
<img src="doc/sqs6.png" />
<img src="doc/sqs8.png" />
<img src="doc/sqs9.png" />

```python
import json

def lambda_handler(event, context):
    print(event)
    records = event['Records']

    for record in records:
        body = record['body']
        print(body)
```
