# Create a function

> Handler field: function_filename.actual_function_name

```sh
rm index.zip

# zip everything in this directory.
zip -r9q index.zip . -x README.md -x output.json -x images/\*

# publish
aws lambda create-function \
--function-name lambda_to_invoke \
--runtime python3.9 \
--handler index.py \
--role arn:aws:iam::460417962015:role/service-role/my_func_asdf-role-2sbdz99a \
--zip-file fileb://index.zip


# update
rm index.zip

zip -r9q index.zip . -x README.md -x output.json -x images/\*

aws lambda update-function-code \
--function-name lambda_to_invoke \
--zip-file fileb://index.zip \
--publish

# invoke
aws lambda invoke \
--function-name lambda_to_invoke \
--invocation-type RequestResponse \
--cli-binary-format raw-in-base64-out \
--payload '{"customer_id": "1111"}' \
output.json

# change lambda function handler
aws lambda update-function-configuration \
--function-name lambda_to_invoke \
--handler index.lambda_handler
```
