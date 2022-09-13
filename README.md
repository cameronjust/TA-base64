# Splunk App to provide a base64 functionality search command
----------------------------------------
* Original Author: Cedric Le Roux
* Author: Cameron Just
* Source type(s): 
* Has index-time operations: No
* Input requirements: None
* Supported product(s): 8.x, 9.x
* Version: 2.1.1
* Deployable: Yes

-------------------------------
## Description

Provides custom search command for base64 encoding and decoding.

This app is an updated version of Cedrid Le Roux's app to make it compatible with later versions of Splunk.

Original App Splunkbase URL: https://splunkbase.splunk.com/app/1922/

-------------------------------
## Changelog:

* 1.1   - Initial Splunk 6.3 version from Splunkbase
* 2.0.0 - Upgraded splunklib and b64.py to be Splunk 8.x compatible
* 2.0.1 - Added in the ability for carriage return and line feed passthrough + Added fixing up of incorrect padding
* 2.0.2 - Updated Splunklib and fixed up encode commands
* 2.1.0 - Updated Splunklib
* 2.1.1 - Moved splunklib into bin directory to appease appinspect

-------------------------------
## Example Searches

```
| makeresults 
| eval encodedField = "ZnJlZA==", otherEncodedField="YmFycnkK" 
| base64 action=decode field=encodedField mode=append 
| base64 action=decode field=otherEncodedField mode=append 
| eval toEncode = "this is to be encoded"
| base64 action=encode field=toEncode mode=append
| table _time encodedField* otherEncodedField* *
```

-------------------------------
## Problems and fixes:


-------------------------------
## App Inspect Results:

```
[root@primary apps]# splunk-appinspect inspect TA-base64
Enable Python analyzer.
Validating: TA-base64 Version: 2.1.1
..........................................................................
..............................................................................
.................................................................
................................................................................
...........

A default value of 25 for max-messages will be used.


TA-base64 Report Summary:

         error:  0
       failure:  0
       skipped:  0
  manual_check: 23
not_applicable: 149
       warning:  3
       success: 156
-------------------
         Total: 331

Please note that more issues could be found out later during the optional manual review process.
```

Full json output of appinspect can be found in the README directory.
