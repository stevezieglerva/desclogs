# desclogs
Presents a list of AWS logs matching a filter pattern (if provided) and then runs awslogs against the users chosen selection

## Prerequisites
* pip install boto3
* pip install [awslogs](https://github.com/jorgebastida/awslogs)

## Usage
```
> . run.sh lutils-
        1. /aws/codebuild/lutils-pipeline
        2. /aws/lambda/lutils-DownloadURLLambda-G037ZJBI5DRW
        3. /aws/lambda/lutils-DownloadURLSeleniumLambda-1N7LNZIS00OVZ
        4. /aws/lambda/lutils-FanDBStreamHandlerTestLambda-CgdwzbPhPZaD
        5. /aws/lambda/lutils-FanHandlerLambda-1A26TSO0GPE3U

        6. /aws/lambda/lutils-FanHandlerLambdaTest-O8GKGW9XQ780
        7. /aws/lambda/lutils-FanLogEventsLambda-1H0Y9A5TNFMKV
        8. /aws/lambda/lutils-FanTestClientLambda-188RA74H5SZAC
        9. /aws/lambda/lutils-FanTestE2ECompletedLambda-PV4C2V3KJOQW
        10. /aws/lambda/lutils-FanTestE2EConsumerLambda-1VQQ5T0QWZE1S

        11. /aws/lambda/lutils-FanTestE2EProducerLambda-16TK8GUNEGFED
        12. /aws/lambda/lutils-S3FilenamesToSNSLambda-377JS6VENM1F
        13. /aws/lambda/lutils-S3TextLinesToSNSLambda-1C769T8AL5I0P
        14. /aws/lambda/lutils-S3TextLinesToSNSLambda-709E47USJ8LX
        15. /aws/lambda/lutils-S3TextLinesToSNSLambda-8Q74TMJXLPRZ


Select log number: 2

Getting logs for: /aws/lambda/lutils-DownloadURLLambda-G037ZJBI5DRW

...

Re-run command:
awslogs get /aws/lambda/lutils-DownloadURLLambda-G037ZJBI5DRW --start 10m

```

On a Mac, the re-run command is copied to the clipboard for easy re-execution.