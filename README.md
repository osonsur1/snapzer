# snapzer
Manage AWS EC2 instance snapshots

## About

Uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

snappy uses the configuration file created by the AWS CLI. e.g.

`aws configure --profile snappy`

## Running

`pipenv run python snappy/snappy.py <command> <subcommand> </subcommand><--project=PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional