# Add a policy to a bucket

<img src="image1.png" />
<img src="image2.png" />
<img src="image3.png" />
<img src="image4.png" />
<img src="image6.png" />
<img src="image7.png" />
<img src="image8.png" />
<img src="image9.png" />
<img src="image10.png" />

All actions on s3 are denied specifically on this resource `folder1/*` under the certain condition that if you have a boolean value of `false` associated with `MultiFactorAuthPresent`.

If you have `true`, you have access to it.

It applies to all pricipals.

Based on this policy, user1 can't open the file. But user2 can open the file.
