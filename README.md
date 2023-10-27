# ZOHO CRM PYTHON SDK 5.0 for API version 5

The Python SDK for Zoho CRM allows developers to easily create Python applications that can be integrated with Zoho CRM. This SDK serves as a wrapper for the REST APIs, making it easier to access and utilize the services of Zoho CRM. 
Authentication to access the CRM APIs is done through OAuth2.0, and the authentication process is streamlined through the use of the Python SDK. The grant and access/refresh tokens are generated and managed within the SDK code, eliminating the need for manual handling during data synchronization between Zoho CRM and the client application.

This repository includes the Python SDK for API v5 of Zoho CRM. Check [Versions](https://github.com/zoho/zohocrm-python-sdk-5.0/releases) for more details on the versions of SDK released for this API version.

License
=======

    Copyright (c) 2021, ZOHO CORPORATION PRIVATE LIMITED 
    All rights reserved. 

    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License. 
    You may obtain a copy of the License at 
    
        http://www.apache.org/licenses/LICENSE-2.0 
    
    Unless required by applicable law or agreed to in writing, software 
    distributed under the License is distributed on an "AS IS" BASIS, 
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
    See the License for the specific language governing permissions and 
    limitations under the License.

## Latest Version

- [1.0.0](/versions/1.0.0/README.md)

    - Added new key in FileStore and DBStore

    - Python SDK upgraded to support v5 APIs.

    - Python SDK improved to support the following new APIs

        - [User Groups API](https://www.zoho.com/crm/developer/docs/api/v5/associated-user-count-user-group.html)
        - [Fiscal Years](https://www.zoho.com/crm/developer/docs/api/v5/get-fiscal-year.html)
        - [Timeline API](https://www.zoho.com/crm/developer/docs/api/v5/timeline-of-a-record.html)
        - [Transfer and Delete Users](https://www.zoho.com/crm/developer/docs/api/v5/transfer_records-delete_user.html)
        - [Territories](https://www.zoho.com/crm/developer/docs/api/v5/add-territories.html)
        - [Territories Users](https://www.zoho.com/crm/developer/docs/api/v5/associate-users-territory.html)
        - [Organization API](https://www.zoho.com/crm/developer/docs/api/v5/delete-org-img.html)
        - [Record Locking API](https://www.zoho.com/crm/developer/docs/api/v5/get-record-locking-info.html)


For older versions, please [refer](https://github.com/zoho/zohocrm-python-sdk-5.0/releases).


## Including the SDK in your project
You can include the SDK to your project using:

- For including the latest [version](https://github.com/zoho/zohocrm-python-sdk-5.0/releases/tag/1.0.0)

    - Install **Python** from [python.org](https://www.python.org/downloads/) (if not installed).

    - Install **Python SDK**
        - Navigate to the workspace of your client app.
        - Run the command below:

        ```sh
        pip install zohocrmsdk5_0
        ```
    - The Python SDK will be installed in your client application.

For more details, kindly refer [here](/versions/1.0.0/README.md).