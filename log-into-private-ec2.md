# Log into public ec2

```sh
ssh -i ~/.ssh/<instance-key>.pem ubuntu@<ec2-public-instance-ip>
```

# Log into private ec2

You should log into the private ec2 from the private ip addess, which means you should log into public ec2 first. And then from there, log into the private ec2.

1. Copy private key

```sh
cat ~/.ssh/<private-key-of-private-ec2>.pem | pbcopy
```

2. Log into public ec2
3. Create a pem.

```sh
vim ~/.ssh/<private-key>.pem
# :set paste in vim to paste private key
# :wq
```

5. Log in

```sh
ssh -i ~/.ssh/<private-key>.pem ubuntu@<ec2-public-instance-ip>
```

# Error

> @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
>
> @ WARNING: UNPROTECTED PRIVATE KEY FILE! @
>
> @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
>
> Permissions 0640 for '/home/y/.ssh/<instance-key>.pem' are too open.
>
> It is required that your private key files are NOT accessible by others.
>
> This private key will be ignored.
>
> Load key "/home/y/.ssh/<instance-key>.pem": bad permissions

If you get this error, run below:

```sh
chmod 0600 <instance-key>.pem
```
