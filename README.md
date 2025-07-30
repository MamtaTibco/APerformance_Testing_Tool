# APerformance_Testing_Tool
💻 Running the App:
 streamlit run main.py


                     API-Performance_Testing_Tool/
                    ├── components/
                    │   ├── __init__.py
                    │   ├── api_request.py
                    │   ├── locust_runner.py
                    │   └── sidebar.py
                    │
                    ├── locustfile/
                    │   ├── .env
                    │   ├── __init__.py
                    │   ├── locust.conf
                    │   ├── locust_payload.json
                    │   └── locustfile.py
                    │
                    ├── utils/
                    │   ├── __init__.py
                    │   ├── env_writer.py
                    │   └── history.py
                    │
                    ├── venv/                     # Virtual environment (optional to include in repo)
                    │
                    ├                    
                    ├── history_tibcoresponse.json
                    ├── install.bat
                    ├── main.py
                    ├── requirements.txt
                    ├── streamlit_requirements.txt
                    ├── ui.css


## 💡 Features

- ✅ Send **GET**, **POST**, **PUT**, **DELETE** requests
- ✅ Input custom headers and JSON body
- ✅ Supports **Bearer Token** and **Basic Auth**
- ✅ Run **Locust** performance test with parameters
- ✅ Request **history tracking**, **replay**, and **delete**
- ✅ Clean UI with `ui.css` overrides
- ✅ Modular and extensible codebase



### 1️⃣ Install dependencies

pip install -r requirements.txt


post:Test Bearer Token:

url:https://urbn--staging.sandbox.my.salesforce.com/services/apexrest/Customers
body:
{"customerAccount":{"RecordType":{"Name":"Terrain"},"PersonEmail":"testmay1@yopmail.com","Preferred_Language__c":"en-US","Ecometry_Migration__c":true,"Primary_Digital_Customer_ID__c":"TRtestmay1@yopmail.com","MC_Send_Flag__c":true},"Emails":[{"Email_Address__c":"testmay1@yopmail.com","Current_Email__c":"true","MC_Send_Flag__c":true}],"Sites":[{"Site_ID__c":"tr-us","Website_Site_ID__c":"terrain","Marketing_Eligible__c":true,"MC_Send_Flag__c":true,"Email_preference__c":true,"Email_Preference_Date__c":"2025-07-18T08:05:47","Email_Preference_Source__c":"Signup - US"}]}

Token :00DWA000000gAfh!AQEAQAB5fUPNhjDKmn0nl3hbqx2qCsK5wsfLupzqnBxVJR6EP0M.3KquVwUP66PRKR.zIJolpgZ62OnWpJgiQ3ifKtz.wbcp


URL: https://postman-echo.com/basic-auth

Method: GET

Auth Type: Basic Auth

Username: postman

Password: password
body:{ "hello": "world" }

GET:
url:http://tibcostage.urbanout.com:8023/orderInquiry/v6
body:
{
  "orderNo": "N300005412",
  "organizationcode": "UO",
  "source": "CCSUP"
}






post:

url:http://localhost:8023/priceAdjustment/v1


{
  "order" : {
    "storeCurrency" : "USD",
    "source" : "Salesforce",
    "requestPurpose" : "MagicButton",
    "refundShipFeePercent" : null,
    "refundAllTaxes" : "N",
    "refundAllSmartLabelFee" : "N",
    "refundAllShipFees" : null,
    "refundAllReturnRestockFee" : "N",
    "refundAllGiftWrap" : "N",
    "refundAllFlatRateShipping" : "N",
    "recalculatePrices" : "N",
    "Promotions" : null,
    "pricingTime" : "16:18:02",
    "pricingDate" : "2025-07-10",
    "orderNo" : "A213167733",
    "orderKey" : null,
    "orderHeaderKey" : "202108231333514834037617",
    "orderDate" : "2025-07-10",
    "Item" : [ {
      "sku" : "40595720",
      "percentOff" : "15",
      "newPrice" : "0",
      "lineNo" : "2",
      "lineKey" : "202108231333514834037620",
      "amountOff" : "0"
    }, {
      "sku" : "23640048",
      "percentOff" : null,
      "newPrice" : null,
      "lineNo" : "1",
      "lineKey" : "202108231333514834037618",
      "amountOff" : null
    } ],
    "id" : null,
    "enterpriseCode" : "01",
    "customerZipCode" : "19010",
    "channel" : "Web",
    "brand" : null,
    "award" : ""
  }
}  	




