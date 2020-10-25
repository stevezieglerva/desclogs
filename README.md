# desclogs
Presents a list of AWS logs matching a filter pattern (if provided) and then runs awslogs against the users chosen selection

## Prerequisites
* boto3
* [awslogs](https://github.com/jorgebastida/awslogs)

## Usage
```
> . run.sh lutils
    1. /aws/codebuild/lutils
    2. /aws/codebuild/lutils-pipeline
    3. /aws/lambda/lutils-DownloadURLLambda-G037ZJBI5DRW
    4. /aws/lambda/lutils-DownloadURLSeleniumLambda-1N7LNZIS00OVZ
    5. /aws/lambda/lutils-S3FilenamesToSNSLambda-377JS6VENM1F
    6. /aws/lambda/lutils-S3TextLinesToSNSLambda-1C769T8AL5I0P
    7. /aws/lambda/lutils-S3TextLinesToSNSLambda-709E47USJ8LX
    8. /aws/lambda/lutils-S3TextLinesToSNSLambda-8Q74TMJXLPRZ

Select log number: 8

Getting logs for: /aws/lambda/lutils-S3TextLinesToSNSLambda-8Q74TMJXLPRZ

/aws/lambda/lutils-S3TextLinesToSNSLambda-8Q74TMJXLPRZ 2020/10/25/[$LATEST]f8b13ee2711e4b29b9e99cb876b9a77d 2020-10-25T19:30:03.193Z Finished at 2020-10-25 19:30:03.193336
/aws/lambda/lutils-S3TextLinesToSNSLambda-8Q74TMJXLPRZ 2020/10/25/[$LATEST]f8b13ee2711e4b29b9e99cb876b9a77d 2020-10-25T19:30:03.216Z END RequestId: 15d1b730-7d3f-4b46-b28e-b76b97fc6087
/aws/lambda/lutils-S3TextLinesToSNSLambda-8Q74TMJXLPRZ 2020/10/25/[$LATEST]f8b13ee2711e4b29b9e99cb876b9a77d 2020-10-25T19:30:03.216Z REPORT RequestId: 15d1b730-7d3f-4b46-b28e-b76b97fc

```

