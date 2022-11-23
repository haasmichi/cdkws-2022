# AWS CDK Workshop 2022

## Preparation
Before attending the workshop some preparation has to be made.  
The installation instructions have been tested on MacOS and **WSL2**.

### WSL2 (Windows)
If you are running Windows as OS, activate / install Windows Subsystem for Linux v2 (**WSL2**) via the software distribution system. 
Ubuntu as a **WSL2** distribution has been tested. Debian should also work.
The rest of the needed software should be installed into your **WSL2** environment.

### Install Python

Install a current Python version using packages from [python.org](https://www.python.org/) or using your package manager.  
Note: Anaconda distributions are not tested or known to work when doing the workshop.

**WSL2**: `sudo apt update && sudo apt install python3 python3-venv python3-pip python3-setuptools -y`

Check: `python3 -V` should give you something like `Python 3.10.8`

### Install AWS CLI

Install the AWS CLI v2 following [these instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

**WSL2**:
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

### AWS Account

An AWS Account called "CdkXX Training Account" has already been created for you. You can access it via our [landing page](https://btelligent.awsapps.com/start).
Try to login using your AD credentials and assume the role, "BtPowerUserAccessCustomizable" (click on `Management console`).
On the landing page click `Command line or programmatic access` and copy the AWS account id (2nd row).

### Configure AWS CLI

Add a new profile to your AWS CLI configuration file by editing ~/.aws/config
```
[profile $SHORTNAME@cdkws]
sso_start_url = https://btelligent.awsapps.com/start
sso_region = eu-central-1
sso_account_id = $ACCOUNT_ID
sso_role_name = BtPowerUserAccessCustomizable
region = eu-central-1
output = json
```
$SHORTNAME is the b.telligent common four letter abbreviation of your name, like sifu.
The $ACCOUNT_ID is the one you have copied in the previous step.

Note: You can name the profile, whatever you want. $SHORTNAME@cdkws is just a suggestion.

### Test programmatic access

In your terminal application do
```
export AWS_PROFILE=$SHORTNAME@cdkws
aws sso login
```
Your browser should open a window requesting app authorization. Click `Allow`.  
Go back to the terminal. You should see a line like this one: `Successfully logged into Start URL: https://btelligent.awsapps.com/start"`.  
Now check, if the correct AWS profile is used.

```
aws sts get-caller-identity | cat
```
This should put out some json document like

```
{
    "UserId": "ABCDE1F2GHIJJJKL3MN4O:your.name@btelligent.com",
    "Account": "123456789012",
    "Arn": "arn:aws:sts::123456789012:assumed-role/AWSReservedSSO_BtPowerUserAccessCustomizable_12345a6bc789def0/your.name@btelligent.com"
}
```
### Install NodeJs

As the AWS CDK comes as a NodeJs package, we need a decent NodeJs installation. Versions 18.0.0+, 16.3.0+ and 14.6.0+ are supported. Version 19.0.1 is not officially supported but didn't throw any errors during testing the workshop.  
Use your package manager to install NodeJS or go to [nodejs.dev](https://nodejs.dev/) and follow the instructions. The NodeJs installation should include the runtime itself and the package manager, npm. Check both on the commandline:

```
node --version
v18.12.1
npm --version
8.19.2
```
**WSL2** (Ubuntu): `curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - && sudo apt-get install -y nodejs`
**WSL2** (Debian as root): `curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && apt-get install -y nodejs`

### Install AWS CDK
The AWS CDK comes as a node package. You can install it via npm.
```
npm install -g aws-cdk
```

Check the cdk version.

```
cdk version
2.51.0 (build a87259f)
```

Done! Youre prepared for the workshop.

