# Update a lambda function

```sh
npm init

npm install @aws-sdk/client-s3

zip -r9q index.zip . -x 'output.json'
# -x: exclude
# -r: recursively

# update lambda function
aws lambda [--profile <your-profile>] update-function-code \
--function-name my_func_nodejs \
--zip-file fileb://index.zip \
--publish

# invoke
aws lambda invoke \
--function-name my_func_nodejs \
--invocation-type RequestResponse \
output.json

cat output.json
```

> Go to 'cloudwatch' and see the logs of this lambda function

> You will see the list of files in the bucket 'keunbae-artifacts'.
