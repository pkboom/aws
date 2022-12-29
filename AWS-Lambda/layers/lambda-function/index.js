const { S3Client, ListObjectsCommand } = require("@aws-sdk/client-s3");

const s3Client = new S3Client({
  region: "us-east-2",
  version: "latest",
  // profile: 'your-profile',
});

// Search for CreateBucketCoomandInput to see input
// to pass to CretaeBucketCommand

const Bucket = "keunbae-artifacts";

exports.handler = async (event, context) => {
  const response = await s3Client.send(new ListObjectsCommand({ Bucket }));
  console.log(response);

  return context.logStreamName;
};
