from flask import Flask, request
import json
import sys

app = Flask(__name__)

@app.route('/prequal',methods=['POST'])
def OMFprequal():
    response_str=the_prequal_meat_function()
    return response_str

@app.route('/decision',methods=['POST'])
def OMFdecision():
    response_str=the_meat_function()
    return response_str

def the_prequal_meat_function():
    try:
        inputJson = request.get_json()
    except:
        responseJson= """ "OMF_decision_model_Response": {
  "response": {
	"status": 1, "errMsg" : "request is not valid json"
	} }
	"""
        return responseJson
    fico=0
    
    #bureau example
    if 'BOR_FICO' in inputJson["bureau"]:
        fico=int(inputJson["bureau"]["BOR_FICO"]["fieldValue"])

    
    #print(fico)
    responseJson=''
    if fico > 650:
        ## Need a response record for each Tier, per product for: Application(chnum=0), Borrower(chnum=1), and SecondaryApplicant (chnum=2)
        responseJson= """ "OMF_decision_model_Response": {
    "response": {
        "status": 0,
        "tiers": [
            {"tierId":4,"chnum":0,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":4,"chnum":0,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":4,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":4,"chnum":1,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":4,"chnum":1,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":4,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":4,"chnum":2,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":4,"chnum":2,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":4,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":5,"chnum":0,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":0,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":5,"chnum":1,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":1,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":5,"chnum":2,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":2,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":6,"chnum":0,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":0,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":6,"chnum":1,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":1,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":6,"chnum":2,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":2,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":7,"chnum":0,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":0,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":7,"chnum":1,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":1,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":7,"chnum":2,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":2,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":8,"chnum":0,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":0,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":8,"chnum":1,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":1,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":8,"chnum":2,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":2,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"}
         ]
    } }
"""
    else:
        responseJson= """ "OMF_decision_model_Response": {
    "response": {
        "status": 0,
        "tiers": [
            {"tierId":4,"chnum":0,"decision":"D","productType":"HII","maxPayment":0,"maxDTI":0,"stipRsn":"D03"},
            {"tierId":4,"chnum":0,"decision":"D","productType":"HIS","maxPayment":0,"maxDTI":0,"stipRsn":"D05"},
            {"tierId":4,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":4,"chnum":1,"decision":"D","productType":"HII","maxPayment":0,"maxDTI":0,"stipRsn":"D07"},
            {"tierId":4,"chnum":1,"decision":"D","productType":"HIS","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":4,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":4,"chnum":2,"decision":"D","productType":"HII","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":4,"chnum":2,"decision":"D","productType":"HIS","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":4,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":5,"chnum":0,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":0,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":5,"chnum":1,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":1,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":5,"chnum":2,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":2,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":5,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":6,"chnum":0,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":0,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":6,"chnum":1,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":1,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":6,"chnum":2,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":2,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":6,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":7,"chnum":0,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":0,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":7,"chnum":1,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":1,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":7,"chnum":2,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":2,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":7,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":8,"chnum":0,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":0,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":0,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":8,"chnum":1,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":1,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":1,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"},
            {"tierId":8,"chnum":2,"decision":"A","productType":"HII","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":2,"decision":"A","productType":"HIS","maxPayment":123.45,"maxDTI":23,"stipRsn":null},
            {"tierId":8,"chnum":2,"decision":"D","productType":"HIN","maxPayment":0,"maxDTI":0,"stipRsn":"D04"}
         ]
    } }
"""
        
    return responseJson

def the_meat_function():

    try:
        inputJson = request.get_json()
    except:
        responseJson= """ "OMF_decision_model_Response": {
  "response": {
	"status": 1, "errMsg" : "request is not valid json"
	} }
	"""
        return responseJson
    fico=0
    refnum=0

    #bureau example
    if 'BOR_FICO' in inputJson["bureau"]:
        fico=int(inputJson["bureau"]["BOR_FICO"]["fieldValue"])
    #premier attributes
    if 'PREMIER_ATTR' in inputJson["bureau"]:
        premierJson=json.loads(inputJson["bureau"]["PREMIER_ATTR"]["fieldValue"])
        ALL8423=int(premierJson["ALL8423"])
    #application example
    if 'PRODUCT_TYPE' in inputJson['application']:
        product_type=inputJson['application']["PRODUCT_TYPE"]["fieldValue"]
    #borrower data example
    if 'DOB' in inputJson['applicants'][0]["applicant"]:
        bor_dob=inputJson['applicants'][0]["applicant"]["DOB"]["fieldValue"]
    #coborrower data example
    if len(inputJson['applicants']) > 1 and 'DOB' in inputJson['applicants'][1]["applicant"]:
        cob_dob=inputJson['applicants'][1]["applicant"]["DOB"]["fieldValue"]
    #refnum
    if 'refnum' in inputJson:
        refnum=inputJson["refnum"]

    
    #print(fico)
    responseJson=''
    if fico > 650:
        responseJson= """ "OMF_decision_model_Response": {
        "response": {
	"status": 0,
	"decisionCode": "APPROVE",
	"creditLimit" : 54321,
	"term" : 123,
	"rate" : 12.345,
	"AdverseAction" : { "code1" :"D11" , "code2" :"D11" , "code3" :"D11" , "code4" :"D11" },
	"StipList" : "STIP111,STIP222,STIP333"
	}
        }
        """
    else:
         responseJson= """ "OMF_decision_model_Response": {
        "response": {
	"status": 0,
	"decisionCode": "DECLINE",
	"creditLimit" : 0,
	"term" : 0,
	"rate" : 12.345,
	"AdverseAction" : { "code1" :"D11" , "code2" :"D11" , "code3" :"D11" , "code4" :"D11" },
	"StipList" : "STIP111,STIP222,STIP333"
	}
        }
        """

    return responseJson

if __name__ == '__main__':
   app.run(debug = True)
