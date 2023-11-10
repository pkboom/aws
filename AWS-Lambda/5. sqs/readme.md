<img src="sqs1.png" />
<img src="sqs2.png" />
<img src="sqs3.png" />
<img src="sqs4.png" />
<img src="sqs7.png" />
<img src="sqs5.png" />
<img src="sqs6.png" />
<img src="sqs8.png" />
<img src="sqs9.png" />
<img src="sqs10.png" />

```python
import json

def lambda_handler(event, context):
    print(event)
    records = event['Records']

    for record in records:
        body = record['body']
        print(body)
```
