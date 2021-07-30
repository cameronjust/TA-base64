# TA-base64

## Addon to provide Encode/DecodeBase64 custom search command 

Original Author: Cedric Le Roux

Author: Cameron Just (upgraded for Splunk 8.x compatibility)

Version: 2.0.2

Splunkbase URL: https://splunkbase.splunk.com/app/1922/

Description: Provides custom command for base64 encoding and decoding

## Changelog
- 1.1   - Initial Splunk 6.3 version from Splunkbase
- 2.0.0 - Upgraded splunklib and b64.py to be Splunk 8.x compatible
- 2.0.1 - Added in the ability for carriage return and line feed passthrough + Added fixing up of incorrect padding
- 2.0.2 - Updated Splunklib and fixed up encode commands


###### Example Search #####

| makeresults 
| eval encodedField = "ZnJlZA==", otherEncodedField="YmFycnkK" 
| base64 action=decode field=encodedField mode=append 
| base64 action=decode field=otherEncodedField mode=append 
| eval toEncode = "this is to be encoded"
| base64 action=encode field=toEncode mode=append
| table _time encodedField* otherEncodedField* *


 

___________________________________________________________________
**Splunklib doesn't pass Splunk Upgrade Readiness App Checker**

Ref: https://community.splunk.com/t5/Developing-for-Splunk-Enterprise/Splunklib-Python-SDK-doesn-t-pass-Splunk-8-x-Upgrade-Readiness/td-p/503646
___________________________________________________________________

Hi All,

I'm in the process of upgrading this app to be 8.x compatible - https://splunkbase.splunk.com/app/1922/

Now this app used the Python Splunklib SDK so I also downloaded the latest from here and replaced it - 
https://github.com/splunk/splunk-sdk-python

I've got it working and it passes appinspect

Only problem is it doesn't pass Splunk's 8.x Upgrade Readiness Checker App - https://splunkbase.splunk.com/app/4698/

The culprit seems to be the latest splunklib Python SDK. I'm sure it will be fine just thought I would ping the devs to either fix the warnings or get the Upgrade Readiness devs to exclude the warnings for splunklib.
